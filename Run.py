#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import time, threading, thread
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from functions import getRecentTracks, periodicMessage, upTime, timeCounter
"""
LASTFM CREDENTIALS
Application name	KancikBot
API key	1d0d46c77cdf69e4ebd62f2b3b638dc3
Shared secret	b1beeaa0be47233ea40f2189bb1b1198
Registered to	cagataycol
"""
s = openSocket()
joinRoom(s)
readbuffer = ""
latestPlaying = ""

while True:
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		if timeCounter():
			periodicMessage(s)
		#print(line) debug etmek için falan
		string_parts = string.split(line, ":")
		if (string_parts[0] == "PING"):
			s.send("PONG %s\r\n" % string_parts[1])
		else:
			user = getUser(line)
			message = getMessage(line)
		print user + " typed :" + message
		if "!komutlar" in message:
			sendMessage(s, "Calan sarki icin: !sarki , Yayın suresi icin: !sure")
			break
		elif "!sarki" in message:
			latestPlaying = getRecentTracks()
			sendMessage(s, "KancikOsman pirezents: " + latestPlaying)
			break
		elif "!sure" in message:
			uptime = upTime()
			sendMessage(s, uptime + " dir yayindayiz.")
			break
