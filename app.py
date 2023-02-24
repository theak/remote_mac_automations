#!/usr/local/bin/python3

from flask import Flask

import subprocess

SCRIPT_TMP = "/Users/akshayk/dev/remote_mac_automations/%s.scpt"

app = Flask(__name__)

@app.route("/chill")
def chill():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'lofi'])
    return 'OK'

@app.route("/playpause")
def playpause():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'playpause'])
    return 'OK'

@app.route("/next")
def next():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'next'])
    return 'OK'
    
@app.route("/ping")
def ping():
    return 'OK'

if __name__ == '__main__': 
   app.run(port=8888, host='0.0.0.0')
