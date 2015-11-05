# encoding=utf-8

import tornado.ioloop
import tornado.web
import tornado.options
import time
import datetime
import redis
import json
import setting

from tornado.options import options


r = redis.StrictRedis()


class WebHookHandler(tornado.web.RequestHandler):

    def post(self):
        if self.request.headers.get("User-Agent") == "git-oschina-hook" and \
                self.get_body_argument("hook"):
            hook = json.loads(self.get_body_argument("hook"))
            if hook["password"] != options.hook_password:
                raise tornado.web.HTTPError(403)
            r.publish("webhook-channel", hook)
            self.write("ok " + str(datetime.datetime.now()))
        else:
            raise tornado.web.HTTPError(403)


setting = {
    "debug": True,
}

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/webhook", WebHookHandler),
    ], **setting)
    application.listen(33333)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().start()
