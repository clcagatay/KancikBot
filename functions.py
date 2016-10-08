import urllib, json
sarki = ""
sanatci = ""
latestPlaying = ""

def getRecentTracks():
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=cagataycol&api_key=1d0d46c77cdf69e4ebd62f2b3b638dc3&limit=1&format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    sanatci = data["recenttracks"]["track"][0]["artist"]["#text"]
    sarki = data["recenttracks"]["track"][0]["name"]
    latestPlaying = sanatci + " - " + sarki
    return latestPlaying
