try:
    import tinytuya
except:
    print("Make sure you have installed all the dependencies")

def setLightColor(deviceId,deviceAddress,localKey,color):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)
    infoData = light.state()

    light.set_colour(color[0],color[1], color[2])
