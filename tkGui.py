try:
    import tkinter
    import customtkinter
    import sys
    import json
    from tkinter.colorchooser import askcolor
    sys.path.append(r"modules")
    from light import *
    import subprocess
    from write2Files import *
    import os
    from notify import sendNotification
except:
    print("Make sure you have installed all the dependencies")
    
window = customtkinter.CTk()

clientId = customtkinter.StringVar()
clientSecret = customtkinter.StringVar()
deviceIdVar = customtkinter.StringVar()
ipAddressVar = customtkinter.StringVar()
localKeyVar = customtkinter.StringVar()

def getDeviceInfoVariables():
    try :
        with open("deviceInfo.json","r",encoding="utf-8") as infosFile:
            info=json.loads(infosFile.read())
            deviceId = info["deviceId"]
            deviceAddress = info["deviceAddress"]
            localKey = info["localKey"]
            infosFile.close()
            return deviceId,deviceAddress,localKey
    except:
        print("Read the documentation for set up the files")
        exit()

def turnLightOnDef():
    deviceId,deviceAddress,localKey= getDeviceInfoVariables()
    turnLightOnFun(deviceId, deviceAddress, localKey)
def turnLightOffDef():
    deviceId,deviceAddress,localKey= getDeviceInfoVariables()
    turnLightOffFun(deviceId, deviceAddress, localKey)


isSpotifyMode = False
spotifyCore = ""
def getMode(choice):
    if (choice =="manual"):
        color = askcolor(title="Choose the color you want")
        if color == (None,None):
            colorLabel.configure(bg_color="transparent")
        else:
            deviceId,deviceAddress,localKey= getDeviceInfoVariables()
            colorLabel.configure(bg_color=("hex-color",color[1]),corner_radius=50) 
            setLightColor(deviceId, deviceAddress, localKey, list(color[0]))

    if (choice == "spotify"):
        global spotifyCore
        global isSpotifyMode

        

        if isSpotifyMode:
            sendNotification("spotyLight", "Spotify Core Is Already Running")
        else:
            try:
                isSpotifyMode = True
                if sys.platform.startswith("win"):
                   spotifyCore= subprocess.Popen(["python","main.py"])
                   
                else:
                    spotifyCore =subprocess.Popen(["python3","main.py"])
                    
            except:
                print("Error running spotyLight Core")
                exit()


def updateSpotyCreds():
    writeSpotyCreds(clientId.get(),clientSecret.get())
    clientId.set("")
    clientSecret.set("")

def updateDeviceInfo():
    writeDeviceInfo(deviceIdVar.get(),ipAddressVar.get(),localKeyVar.get())
    deviceIdVar.set("")
    ipAddressVar.set("")
    localKeyVar.set("")

def on_closing():
    global isSpotifyMode
    global spotifyCore
    if(isSpotifyMode):
        spotifyCore.kill()
    window.destroy()


def setConfigFilesDef():
    inputTopLevel = customtkinter.CTkToplevel()
    inputTopLevel.geometry("650x600")
    inputTopLevel.resizable(False,False)
    spotyCredFrame = customtkinter.CTkFrame(master=inputTopLevel,height=250,width=450,corner_radius=20)
    spotyCredFrame.pack_propagate(False)
    spotyCredLabel = customtkinter.CTkLabel(master=spotyCredFrame,text="Insert Here Spotify Credentials",font=("San Francisco",20))
    spotyCredLabel.place(rely=0.2,relx=0.5,anchor=tkinter.CENTER)

    spotyCredClientIdLabel = customtkinter.CTkLabel(master=spotyCredFrame,text="Client Id",font=("San Francisco",14))
    spotyCredClientIdLabel.place(rely=0.4,relx=0.2)

    spotyCredClientSecretLabel = customtkinter.CTkLabel(master=spotyCredFrame,text="Client Secret",font=("San Francisco",14))
    spotyCredClientSecretLabel.place(rely=0.7,relx=0.2)

    spotyClientIdEntry = customtkinter.CTkEntry(master=spotyCredFrame,placeholder_text="Enter Here your Client Id",textvariable=clientId,placeholder_text_color="white")
    spotyClientIdEntry.place(rely=0.4,relx=0.5)
    spotyClientSecretEntry = customtkinter.CTkEntry(master=spotyCredFrame,placeholder_text="Enter Here your Client Secret",textvariable=clientSecret,placeholder_text_color="white")
    spotyClientSecretEntry.place(rely=0.7,relx=0.5)

    spotyCredBtn = customtkinter.CTkButton(master=spotyCredFrame,text="Update",command=updateSpotyCreds)
    spotyCredBtn.place(rely=0.85,relx=0.6)
    spotyCredFrame.pack(pady=10)

    ##############################DIVIDER#################################
    
    deviceInfoFrame = customtkinter.CTkFrame(master=inputTopLevel,height=250,width=450,corner_radius=20)
    deviceInfoFrame.pack_propagate(False)
    deviceInfoLabel = customtkinter.CTkLabel(master=deviceInfoFrame,text="Insert Here Device Info",font=("San Francisco",20))
    deviceInfoLabel.place(rely=0.1,relx=0.5,anchor=tkinter.CENTER)

    deviceInfoId = customtkinter.CTkLabel(master=deviceInfoFrame,text="Device Id",font=("San Francisco",14))
    deviceInfoId.place(rely=0.2,relx=0.2)

    deviceInfoAddress = customtkinter.CTkLabel(master=deviceInfoFrame,text="Device Address",font=("San Francisco",14))
    deviceInfoAddress.place(rely=0.4,relx=0.2)

    deviceInfoKey = customtkinter.CTkLabel(master=deviceInfoFrame,text="Local Key",font=("San Francisco",14))
    deviceInfoKey.place(rely=0.6,relx=0.2)

    deviceInfoIdEntry = customtkinter.CTkEntry(master=deviceInfoFrame,placeholder_text="Enter Here The Device Id",textvariable=deviceIdVar,placeholder_text_color="white")
    deviceInfoIdEntry.place(rely=0.2,relx=0.5)
    deviceInfoAddressEntry = customtkinter.CTkEntry(master=deviceInfoFrame,placeholder_text="Enter Here The Ip Address",textvariable=ipAddressVar,placeholder_text_color="white")
    deviceInfoAddressEntry.place(rely=0.4,relx=0.5)
    deviceInfoKeyEntry = customtkinter.CTkEntry(master=deviceInfoFrame,placeholder_text="Enter Here The Local Key",textvariable=localKeyVar,placeholder_text_color="white")
    deviceInfoKeyEntry.place(rely=0.6,relx=0.5)

    deviceInfoBtn = customtkinter.CTkButton(master=deviceInfoFrame,text="Update",command=updateDeviceInfo)
    deviceInfoBtn.place(rely=0.85,relx=0.6)
    deviceInfoFrame.pack(pady=10)





window.title("SpotyLight")
window.geometry("600x600")
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 
window.resizable(False,False)




switchFrame = customtkinter.CTkFrame(master=window,width=400,height=150,corner_radius=20,)
switchFrame.pack_propagate(False)
switchFrame.pack(pady=20)
modeFrame = customtkinter.CTkFrame(master=window,width=400,height=200,corner_radius=20,)
modeFrame.pack_propagate(False)
modeFrame.pack(pady=20)

statusLabel = customtkinter.CTkLabel(master= switchFrame,text=f"Set Up The Light").place(rely=0.1,relx=0.5,anchor=tkinter.CENTER)
deviceName = customtkinter.CTkLabel(master=switchFrame,height=90,width=100,text="Light",text_color="white",font=("San Francisco",20))
deviceName.place(rely=0.5,relx=0.2,anchor=tkinter.CENTER)
turnLightOn = customtkinter.CTkButton(master= switchFrame,text="Turn on the light",command=turnLightOnDef)
turnLightOn.place(rely=0.5,relx=0.3,anchor=tkinter.CENTER)
turnLightOff = customtkinter.CTkButton(master= switchFrame,text="Turn off the light",command=turnLightOffDef)
turnLightOff.place(rely=0.5,relx=0.7,anchor=tkinter.CENTER)

modeLabel = customtkinter.CTkLabel(master=modeFrame,text="Select the color light's mode",font=("San Francisco",20))
modeLabel.place(rely=0.3,relx=0.5,anchor=tkinter.CENTER)
selectMode = customtkinter.CTkComboBox(master=modeFrame,values=["spotify","manual"],command=getMode)
selectMode.place(rely=0.5,relx=0.5,anchor=tkinter.CENTER)
selectMode.set("-")
colorLabel = customtkinter.CTkLabel(master=modeFrame,height=70,width=70,bg_color=("transparent"),text="")
colorLabel.place(rely=0.8,relx=0.5,anchor=tkinter.CENTER)

setConfigFilesBtn = customtkinter.CTkButton(master=switchFrame,text="Set Config Files",command=setConfigFilesDef)
setConfigFilesBtn.place(rely=0.8,relx=0.5,anchor=tkinter.CENTER)



window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()
