##oschina-hook

A simple tool to pull code from oschina with webhook of oschina


####Description

This project aims to update your code automatically when you push data to oschina.

This project consists of two parts: The first part listens to a specifical port for **POST** request from
**git-oschina-hook**, and then publish message; The second part subscribes to the channel and executes 
the script(`automate.sh`).


####Useage

1. You need to have redis-server installed(used for message delivery).

2. Install dependences with `pip install -r requirements.txt`(recommend using `virtualenv`).

3. Update the password(reserved in hook on oschina) in `setting_sample.py`, then rename to `setting.py`.

4. Edit `automate.sh`(script which will be executed when you push to remote repo on oschina) as you wish.

5. Run `python2 app.py` and `python automate.py` on your server.
