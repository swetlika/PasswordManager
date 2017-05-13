# 460-Final-Project

This is our attempt to create a password manager similar to LastPass or KeePass.
PLEASE DO NOT ACTUALLY USE THIS - IT HAS PLENTY OF SECURITY VULNERABILITIES.

It has a hardcoded master password, "master."

#How to run:
1. Start your server by running: python main.py
2. Install the chrome extension (since it hasn't been packed, it needs to be loaded unpacked, in dev mode)
3. When you navigate to a new website, click the icon at the top right
4. Type in your username and password that you have for that website, and hit enter
5. Now, type in the master password ("master") into a password field of a saved domain
6. Once you type it in, it should replace the username and password fields with your saved username and password
7. You can view a collection of your saved username and passwords by navigating to 127.0.0.1:5000 and entering your master password