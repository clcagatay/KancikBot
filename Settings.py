HOST = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:bu2dutjvs3ltxr5dlx402hbhf56j4y"
IDENT = "kancikbot"
CHANNEL = "kancikosman"
LASTFMUSER = "cagataycol"

messagesList = ["bu bir auto mesajdir","bu baska bir auto mesajdir", "en auto mesaj budur"]
lastfm_api_url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + LASTFMUSER + "&api_key=1d0d46c77cdf69e4ebd62f2b3b638dc3&limit=1&format=json"
twitch_uptime_api_url = "https://api.rtainc.co/twitch/channels/" + CHANNEL + "/uptime?format=[1]&units=2"

"""
LASTFM CREDENTIALS
Application name	KancikBot
API key	1d0d46c77cdf69e4ebd62f2b3b638dc3
Shared secret	b1beeaa0be47233ea40f2189bb1b1198
Registered to	cagataycol
"""
