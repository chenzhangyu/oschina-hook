# encoding=utf-8

import redis
from subprocess import call



def automate():
    r = redis.StrictRedis()
    p = r.pubsub()
    p.subscribe("webhook-channel")
    for m in p.listen():
        print m
        if m["type"] == "message":
            call(["bash", "./automate.sh"])


if __name__ == "__main__":
    automate()
