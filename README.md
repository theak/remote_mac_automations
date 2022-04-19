Remotely trigger Applescript automations

How it works:
1. Clone the repo
2. Make sure you have Python3 and Flask installed ("pip3 install Flask")
3. Edit "app.py" and change SCRIPT_TMP to be the folder for your Applescripts, with %s as the name of the script
4. Run "chmod +X app.py"
5. Run "./app.py" and make sure it runs locally on port 8888
6. Edit com.ak.chill.plist to add the correct absolute path to app.py on your disk
7. Run "cp com.ak.chill.plist ~/Library/LaunchAgents/"
8. Run "launchctl load ~/Library/LaunchAgents/com.ak.chill.plist" to run this as a daemon
9. To add/modify the automations, modify "app.py", then unload and load the daemon for the changes to take effect
