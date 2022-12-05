import tkinter
import customtkinter
import sys
import json
from tkinter.colorchooser import askcolor
sys.path.append(r"modules")
from light import *
import subprocess
window = customtkinter.CTk()

with open("deviceInfo.json","r",encoding="utf-8") as infosFile:
        info=json.loads(infosFile.read())
        deviceId = info["deviceId"]
        deviceAddress = info["deviceAddress"]
        localKey = info["localKey"]
        infosFile.close()

def turnLightOnDef():
    turnLightOnFun(deviceId, deviceAddress, localKey)
def turnLightOffDef():
    turnLightOffFun(deviceId, deviceAddress, localKey)

def getMode(choice):
    if (choice =="manual"):
        color = askcolor(title="Choose the color you want")
        if color == (None,None):
            colorLabel.configure(bg_color="transparent")
        else:
            colorLabel.configure(bg_color=("hex-color",color[1]),corner_radius=50) 
            setLightColor(deviceId, deviceAddress, localKey, list(color[0]))
    if (choice == "spotify"):
        subprocess.call("python3 main.py",creationflags=subprocess.CREATE_NEW_CONSOLE)


window.title("SpotyLight")
window.geometry("500x500")
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 
window.resizable(False,False)



value = customtkinter.IntVar(value=checkStatus(deviceId, deviceAddress, localKey))
print(value.get())
switchFrame = customtkinter.CTkFrame(master=window,width=400,height=150,corner_radius=20,)
switchFrame.pack_propagate(False)
switchFrame.pack(pady=20)
modeFrame = customtkinter.CTkFrame(master=window,width=400,height=200,corner_radius=20,)
modeFrame.pack_propagate(False)
modeFrame.pack(pady=20)

statusLabel = customtkinter.CTkLabel(master= switchFrame,text=f"The ligh is {value.get()}").place(rely=0.1,relx=0.5,anchor=tkinter.CENTER)
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

window.mainloop()