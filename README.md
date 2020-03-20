<code>

$ virtualenv venv --python=python3 (I might need to create the virtual env outside of the webpages folder)

$ source venv/bin/activate

$ which python

$ python -m http.server

$ hostname -I

hostname:8000 (10.0.0.50)

$ roslaunch rosbridge_server rosbridge_websocket.launch

http://robotwebtools.org/tools.html

- Copy the same local ip address in the script

$ rostopic echo /mobile_base/commands/velocity

</code>
