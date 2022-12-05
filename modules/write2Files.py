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
            "deviceId" : clientId,
            "deviceAddress" : ipAddres,
            "localKey":localKey
        }
        
        file.write(json.dumps(json_file))