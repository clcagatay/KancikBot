import urllib, json
import time, threading, thread
import datetime
from Socket import sendMessage
from Settings import messagesList, lastfm_api_url, twitch_uptime_api_url, CHANNEL
sarki = ""
sanatci = ""
latestPlaying = ""

i = 0
beyler_count = 0
prev_time = datetime.datetime(2016,10,9,0,0,0,0)

def getRecentTracks():
    url = lastfm_api_url
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
    url = "https://api.twitch.tv/kraken/channels/kanaladi"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    went_live = data["updated_at"]
    time = went_live.split("T")
    time_hms = time[1].split(":")
    now = datetime.datetime.now()
    #sure_saat = now.hour - time_hms[0]
    print time_hms[0]
    """
    url = twitch_uptime_api_url
    response = urllib.urlopen(url)
    uptime_en= str(response.read())
    uptime_api_response_has = "currently"
    if uptime_api_response_has in uptime_en:
        uptime_status = "Kanal su an yayinda degil."
        return str(uptime_status)
    else:
        uptime_tr1 = uptime_en.replace("hours","saat")
        uptime_tr2 = uptime_tr1.replace("minutes","dakika")
        uptime_status = uptime_tr2 + " suredir yayindayiz."
        return str(uptime_status)
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
def beylerCounter():
    global beyler_count
    beyler_count = beyler_count + 1
    return beyler_count
