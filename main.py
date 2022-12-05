try:
    import json 
    import sys
    import sys
    sys.path.append(r"modules")
    from spoty import getCurrentSong
    from downloader import downloadCover
    from color import getDominantColor
    from light import setLightColor
    from loginOauth import getSecretToken
    from checkToken import isTokenValid
    import time as t
except:
    print("Make sure you have installed all the dependencies")

currentSongLink = "https://api.spotify.com/v1/me/player/currently-playing"
authLink = "https://accounts.spotify.com/api/token"
redirect_uri = 'https://github.com/geth0/spotyLight'
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
scope = [
     "user-read-currently-playing"
]
try:
    with open("spotyCred.json","r",encoding="utf-8") as credentials:
        data =json.loads(credentials.read())
        clientId = data["clientId"]
        clientSecret = data["clientSecret"]
        credentials.close()
except :
    print("Read the documentation for set up the files")
    exit()
try :
    with open("deviceInfo.json","r",encoding="utf-8") as infosFile:
        info=json.loads(infosFile.read())
        deviceId = info["deviceId"]
        deviceAddress = info["deviceAddress"]
        localKey = info["localKey"]
        infosFile.close()
except:
    print("Read the documentation for set up the files")
    exit()
loginOAuthData=getSecretToken(clientId,clientSecret,redirect_uri, authorization_base_url, token_url, scope)
if(isTokenValid(loginOAuthData)):
        loginOAuthData=getSecretToken(clientId,clientSecret,redirect_uri, authorization_base_url, token_url, scope)
while True:
    if(isTokenValid(loginOAuthData)):
        loginOAuthData=getSecretToken(clientId,clientSecret,redirect_uri, authorization_base_url, token_url, scope)

    else:
        accessToken = loginOAuthData["accessToken"]
        songData = getCurrentSong(currentSongLink, accessToken)
        downloadCover(songData["imageUrl"])
        domColor = getDominantColor()
        setLightColor(deviceId, deviceAddress, localKey, domColor)

    t.sleep(20) #Modify here to set a custom time of refresh