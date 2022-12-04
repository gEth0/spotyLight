import json 
import sys
import sys
sys.path.append(r"modules")
from spoty import getCurrentSong
from downloader import downloadCover
from color import getDominantColor
from light import setLightColor
link = "https://api.spotify.com/v1/me/player/currently-playing"

with open("spotyCred.json","r",encoding="utf-8") as credentials:
    accessToken =json.loads(credentials.read())["accessToken"]
    credentials.close()
with open("deviceInfo.json","r",encoding="utf-8") as infosFile:
    info=json.loads(infosFile.read())
    deviceId = info["deviceId"]
    deviceAddress = info["deviceAddress"]
    localKey = info["localKey"]
    infosFile.close()
songData = getCurrentSong(link, accessToken)
downloadCover(songData["imageUrl"])
domColor = getDominantColor()
setLightColor(deviceId, deviceAddress, localKey, domColor)