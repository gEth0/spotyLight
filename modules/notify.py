try:
    from plyer import notification
    import sys
except:
    print("Make sure you have installed all the dependencies")

def sendNotification(title,message,time=5):
    if sys.platform.startswith("win"):
        notification.notify(title=title,message=message,timeout=time,toast=True,app_icon="images\guiLogo.ico")
    else:
        notification.notify(title=title,message=message,timeout=time,toast=True)