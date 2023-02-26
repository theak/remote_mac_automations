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

@app.route("/left")
def left():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'left'])
    return 'OK'

@app.route("/right")
def right():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'right'])
    return 'OK'

@app.route("/up")
def up():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'up'])
    return 'OK'

@app.route("/down")
def down():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'down'])
    return 'OK'

@app.route("/open")
def open():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'open'])
    return 'OK'

@app.route("/kodi")
def kodi():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'kodi'])
    return 'OK'

@app.route("/next")
def next():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'next'])
    return 'OK'

@app.route("/prev")
def next():
    subprocess.Popen(['osascript', SCRIPT_TMP % 'prev'])
    return 'OK'

@app.route("/ping")
def ping():
    return 'OK'

if __name__ == '__main__': 
   app.run(port=8888, host='0.0.0.0')
