# -*- coding: utf-8 -*-

from tornado import escape
from model.models import User, AvatarChange
from handlers.base import BaseHandler
from utils import gravatar
from utils import weibo
from datetime import datetime
import re, StringIO, time
from PIL import Image

class IndexHandler(BaseHandler):
    def get(self):
        user_email = self.get_current_user()
        user = self.session.query(User).filter_by(uemail = user_email).first()
        self.render('index.html', user = user, avatar_base=gravatar.gravatar_base)

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', next=self.get_argument("next", "/"))
        
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        
        user = self.session.query(User).filter_by(uemail = email).first()
        if user and user.upwd == self.pwdEncrypt(email, password):
            self.set_current_user(user.uemail)
            self.redirect("/")
        else:
            self.redirect("/index/login")
            
class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")
        
class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html", next=self.get_argument("next", "/"))
    
    def post(self):
        
        username = self.get_argument('username')
        email = self.get_argument('email')
        password1 = self.get_argument('password1')
        password2 = self.get_argument('password2')
        
        wrong_tips = [''] * 4
        zerotip = '这个字段是必填项'
        if len(username) == 0:
            wrong_tips[0] = zerotip
        else:
            user = self.session.query(User).filter_by(uname = username).first()
            if user:
                wrong_tips[0] = '称号已被注册'
        if len(email) == 0:
            wrong_tips[1] = zerotip
        else:
            user = self.session.query(User).filter_by(uemail = email).first()
            if user:
                wrong_tips[1] = '用户已经存在'
        if len(password1) == 0:
            wrong_tips[2] = zerotip
        elif len(password1) < 6:
            wrong_tips[2] = '确保该值不少于 6 个字符 (现在有 ' + str(len(password1)) + ' 个)'
        if len(password2) == 0:
            wrong_tips[3] = zerotip
        elif password2 != password1:
            wrong_tips[3] = '密码不匹配'
        
        status = 'error'
        if wrong_tips == ['']*4:
            status = 'success'
            encryptPwd = self.pwdEncrypt(email, password1)
            user = User()
            user.uname = username
            user.uemail = email
            user.upwd = encryptPwd
            user.uavatar = gravatar.getGravatarHash(email)
            user.ucreatedate = datetime.now()
            
            self.session.add(user)
            self.session.commit()
            self.set_current_user(user.uemail)
            
        self.write(escape.json_encode({'status':status, 'wrong_tips':wrong_tips}))
        
class GravatarHandler(BaseHandler):
    def get(self):
        email = self.get_argument('email')
        email_reg = '^\\s*\\w+(?:\\.{0,1}[\\w-]+)*@[a-zA-Z0-9]+(?:[-.][a-zA-Z0-9]+)*\\.[a-zA-Z]+\\s*$'
        if re.search(email_reg, email) == None:
            status = 'error'
            info = u'哎呀～您所输入的邮件格式有误，请重新输入'
            gravatar_url = ''
        else:
            status = 'success'
            info = u'哈哈～成功根据您的邮箱地址获得gravatar上的头像'
            gravatar_url = gravatar.getGravatarFromEmail(email)
            #"http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
        self.write(escape.json_encode({'status':status, 'info':info, 'gravatar_url':gravatar_url}))

class SignupSuccessHandler(BaseHandler):
    def get(self):
        user_email = self.get_current_user()
        _user = self.session.query(User).filter_by(uemail = user_email).first()
        self.render('signup_success.html', user=_user, avatar_base=gravatar.gravatar_base)

class AvatarUploadHandler(BaseHandler):
    def get(self):
        user_email = self.get_current_user()
        user = self.session.query(User).filter_by(uemail = user_email).first()
        local_avatar = None if None==user else user.ulocalavatar    
        self.render("avatar_upload.html", avatar_href=local_avatar)
    def post(self):
        file_dict_list = self.request.files.get('upavatar')
        user_email = self.get_current_user()
        user = self.session.query(User).filter_by(uemail = user_email).first()
        userid = None if None==user else user.uid
        filename = None
        imgAngle = -int(self.get_argument('hideAngle'))
        if None != file_dict_list and len(file_dict_list) > 0:
            file_dict = file_dict_list[0]
            filename = file_dict["filename"] if None==userid else str(userid)+'.'+file_dict["filename"].split('.').pop()
            filepath = "./static/upload/avatar/"+filename
            f = StringIO.StringIO(file_dict["body"])
            ori_img = Image.open(f)    
            rot_img = ori_img.rotate(imgAngle)
            rot_img.save(filepath)
            
            if None != user:
                user.ulocalavatar = filename
            self.session.commit()
        
        weibo_oacode = self.get_weibo_oacode()
        if None != weibo_oacode:
            client = weibo.PrepareOAuthClient(weibo_oacode)
            post_ret = client.statuses.update.post(status=u'快来看我在鸸鹋上传了新头像！http://www.ermiao.com '+str(datetime.now()))
            time.sleep(2)
            midstr = client.statuses.querymid.get(id=int(post_ret['idstr']), type=1)['mid']

            user_email = self.get_current_user()
            user = self.session.query(User).filter_by(uemail = user_email).first()
            avatar_log = AvatarChange()
            if None != user:
                avatar_log.cuid = user.uid
            avatar_log.cweibourl = 'weibo.com/' + str(post_ret['user']['id']) + '/' + midstr
            self.session.add(avatar_log)
            self.session.commit()
            
        self.render('avatar_upload.html', avatar_href=filename)

class OauthWeiboHandler(BaseHandler):
    def get(self):
        oauth_url = weibo.PrepareOAuthUrl()
        self.redirect(oauth_url)

class WeiboCallbackHandler(BaseHandler):
    def get(self):
        oauth_code = self.get_argument('code')
        self.set_weibo_oacode(oauth_code)
        self.redirect('/')
        
        
        