import json
def writeSpotyCreds(clientId,clientSecret):
    if clientId == "" or clientSecret == "":
        print("Insert Real Values")
        exit()
    with open("spotyCred.json","w",encoding="utf-8") as file:

        json_file = {
            "clientId" : clientId,
            "clientSecret" : clientSecret
        }
        
        file.write(json.dumps(json_file))
def writeDeviceInfo(deviceId,ipAddres,localKey):
    if deviceId == "" or ipAddres == "" or localKey == "":
        print("Insert Real Values")
        exit()
    with open("deviceInfo.json","w",encoding="utf-8") as file:

        json_file = {
            "deviceId" : deviceId,
            "deviceAddress" : ipAddres,
            "localKey":localKey
        }
        
        file.write(json.dumps(json_file))

def storeSpotyToken(tokenObject):
    with open("spotyToken.json","w",encoding="utf-8") as file:
        file.write(json.dumps(tokenObject))

def readSpotyToken():
    with open("spotyToken.json","r",encoding="utf-8") as file:
        return json.loads(file.read())