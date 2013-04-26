from handlers.index import *

urls = [
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/index/login', LoginHandler),
    (r'/index/logout', LogoutHandler),
    (r'/index/register', RegisterHandler),
    (r'/index/gravatar', GravatarHandler),
    (r'/index/signup/success', SignupSuccessHandler),
    (r'/index/avatarupload', AvatarUploadHandler),
    (r'/index/oauth_weibo', OauthWeiboHandler),
    (r'/callback/weibo', WeiboCallbackHandler),
]
