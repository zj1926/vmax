import tornado.ioloop
from server.routes import routes

settings = {
    "cookie_secret": "cat and dog",
    #"xsrf_cookies": True,
}
app = tornado.wsgi.WSGIApplication(routes, **settings)

