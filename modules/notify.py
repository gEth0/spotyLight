try:
    from plyer import notification
except:
    print("Make sure you have installed all the dependencies")

def sendNotification(title,message,time=10):
    notification.notify(title=title,message=message,timeout=time,toast=True)