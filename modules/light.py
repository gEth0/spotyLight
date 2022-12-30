try:
    import tinytuya
except:
    print("Make sure you have installed all the dependencies")

def initializeLight(deviceId,deviceAddress,localKey):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)

    return light

def setLightColor(deviceId,deviceAddress,localKey,color):
    light = initializeLight(deviceId,deviceAddress,localKey)
    infoData = light.state()
    if(infoData["is_on"] == False):
        light.turn_on()
    light.set_colour(color[0],color[1], color[2])

def toggleLight(deviceId,deviceAddress,localKey):
    light = initializeLight(deviceId,deviceAddress,localKey)
    infoData = light.state()

    light.turn_on() if infoData["is_on"] == False else light.turn_off()


def turnLightOnFun(deviceId,deviceAddress,localKey):
    light = initializeLight(deviceId,deviceAddress,localKey)
    light.turn_on()

def turnLightOffFun(deviceId,deviceAddress,localKey):
    light = initializeLight(deviceId,deviceAddress,localKey)
    light.turn_off()