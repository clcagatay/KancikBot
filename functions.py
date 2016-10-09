import urllib, json
import time, threading, thread
import datetime
from Socket import sendMessage
sarki = ""
sanatci = ""
latestPlaying = ""
messagesList = ["bu bir auto mesajdir","bu baska bir auto mesajdir", "en auto mesaj budur"]
i = 0
prev_time = datetime.datetime(2016,10,9,0,0,0,0)
def getRecentTracks():
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=cagataycol&api_key=1d0d46c77cdf69e4ebd62f2b3b638dc3&limit=1&format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    sanatci = data["recenttracks"]["track"][0]["artist"]["#text"]
    sarki = data["recenttracks"]["track"][0]["name"]
    latestPlaying = sanatci + " - " + sarki
    return latestPlaying
def periodicMessage(s):
    global i
    if i < len(messagesList):
        #print messagesList[i]
        sendMessage(s, messagesList[i])
        i = i + 1
        return i
    else:
        #print messagesList[0]
        sendMessage(s, messagesList[0])
        i = 1
        return i
def upTime():
    """
    url = "https://api.twitch.tv/kraken/channels/funkefal"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    went_live = data["updated_at"]
    time = went_live.split("T")
    time_hms = time[1].split(":")
    now = datetime.datetime.now()
    #sure_saat = now.hour - time_hms[0]
    print time_hms[0]
    """
    url = "https://api.rtainc.co/twitch/channels/funkefal/uptime?format=[1]&units=2"
    #if ile yayinin olup olmadigina bakip ona gore cevap yazma eklenecek
    response = urllib.urlopen(url)
    uptime_en= str(response.read())

    uptime_tr1 = uptime_en.replace("hours","saat")
    uptime_tr2 = uptime_tr1.replace("minutes","dakika")
    return str(uptime_tr2)
def timeCounter():
    global prev_time
    now = datetime.datetime.now()
    count_lenght = now.second - prev_time.second
    delta = now - prev_time
    if delta > datetime.timedelta(seconds=10) :
        prev_time = datetime.datetime.now()
        return True
    else:
        return False
