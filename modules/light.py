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

def toggleLight(deviceId,deviceAddress,localKey):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)
    infoData = light.state()

    if(infoData["is_on"]==False):

        light.turn_on()
    else:

        light.turn_off()

def checkStatus(deviceId,deviceAddress,localKey):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)
    infoData = light.state()
    
    if(infoData['is_on']==True):
        print('on')
        return 1
    else:
        print('off')
        return 0

def turnLightOnFun(deviceId,deviceAddress,localKey):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)
    infoData = light.state()
    light.turn_on()

def turnLightOffFun(deviceId,deviceAddress,localKey):
    light = tinytuya.BulbDevice(deviceId,deviceAddress,localKey)
    light.set_version(3.3)
    light.set_socketPersistent(True)
    infoData = light.state()
    light.turn_off()