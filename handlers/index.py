# -*- coding: utf-8 -*-

from tornado import escape
from model.models import User
from handlers.base import BaseHandler
from utils import gravatar
from datetime import datetime
import re

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
            self.redirect("/login")
            
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
        