#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import urllib, json

def getUser(line):
	#separate = line.split(":", 2)
	#user = separate[1].split("!", 1)[0]
	#return user
	parts = string.split(line, ":")
	usernamesplit = string.split(parts[1], "!")
	user = usernamesplit[0]
	return user
def getMessage(line):
	#separate = line.split(":", 2)
	#message = separate[2]
	#return message
	parts = string.split(line, ":")
	if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
		try:
			# Sets the message variable to the actual message sent
			message = parts[2][:len(parts[2]) - 1]
		except:
			message = ""
	return message
def isUserMod(user):
	url = "http://tmi.twitch.tv/group/user/kancikosman/chatters"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	for i in range(0,len(data["chatters"]["moderators"])):
	 	username = data["chatters"]["moderators"][i]
		if user == username:
			return True
		else:
			return False
