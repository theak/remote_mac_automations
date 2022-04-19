Remotely trigger Applescript automations

How it works:
1. Clone the repo
2. Make sure you have Python3 and Flask installed ("pip3 install Flask")
3. Run "chmod +X app.py"
4. Run "./app.py" and make sure it runs locally on port 8888
5. Edit com.ak.chill.plist to add the correct absolute path to app.py on your disk
6. Run "cp com.ak.chill.plist ~/Library/LaunchAgents/"
7. Run "launchctl load ~/Library/LaunchAgents/com.ak.chill.plist" to run this as a daemon
8. To add/modify the automations, modify "app.py", then unload and load the daemon for the changes to take effect
