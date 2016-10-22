#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import time, threading, thread
from Read import getUser, getMessage, isUserMod
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from functions import getRecentTracks, periodicMessage, upTime, timeCounter, beylerCounter, latestPlaying
from daemon import runner

class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/tmp/foo.pid'
		self.pidfile_timeout = 5
	def run(self):
		s = openSocket()#open a socket and connect to server
		joinRoom(s)#join the channel chat stated in settings.py
		readbuffer = ""
		while True:#infinite loop for always listening the chat
			readbuffer = readbuffer + s.recv(1024)#reading the chat
			temp = string.split(readbuffer, "\n")
			readbuffer = temp.pop()
			
			for line in temp:#for every line read loop
				"""if timeCounter():#checks the time for periodic messages
					periodicMessage(s)"""
				#print(line) for debugging purposes
				string_parts = string.split(line, ":")#easyly readable chat
				if (string_parts[0] == "PING"):#to send pong when twitch sends ping this is important to maintain a connection
					s.send("PONG :tmi.twitch.tv\r\n".encode())
				else:#if it is not ping message from twitch
					user = getUser(line)#get the username who sends message
					message = getMessage(line)#get the message which is sent
				print user + " typed :" + message#show in the console who typed what
				#from here on special chat typed commands take part
				if "!komutlar" in message:#to list available commands to users and list them in the chat
					print "!komutlar"
					#sendMessage(s, "Calan sarki icin: !sarki , Yayın suresi icin: !sure")
					break
					"""elif "!sarki" in message:#shows the chat last scrobbled song and artis on lastfm
					latestPlaying = getRecentTracks()
					sendMessage(s, "KancikOsman pirezents: " + latestPlaying)
					break
					"""
					"""elif "!sure" in message:#shows the chat how long is the stream went live
					uptime = upTime()
					sendMessage(s, uptime)
					break
					elif "!addbeyler" in message:#if a user is moderator in the chat, adds +1 to the counter
					if isUserMod(user):
						beyler = beylerCounter()
						print "Beyler Sayaci: " + str(beyler)
					else:
						sendMessage(s, user + " ->  Bu komutu kullanma yetkiniz yok.")
					break
					"""
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
