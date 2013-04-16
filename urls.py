from handlers.index import *

urls = [
    (r'/', IndexHandler),
    (r'/index/login', LoginHandler),
    (r'/index/logout', LogoutHandler),
    (r'/index/register', RegisterHandler),
    (r'/index/gravatar', GravatarHandler),
    (r'/index/signup/success', SignupSuccessHandler),
]
