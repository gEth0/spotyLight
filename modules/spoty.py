try:
    import requests
    import time
    from notify import *
except:
    print("Make sure you have installed all the dependencies")

def getCurrentSong(link,accessToken):
    response = requests.get(link,headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {accessToken}"
    })
    
    return response



def getSongFormatted(link,accessToken):
    counter = 0
    response = getCurrentSong(link, accessToken)
   
    try:
        json_response = response.json()
    except:
        sendNotification("spotyLight","Make sure one song is currently playing")
    print(json_response)
    if(response.status_code == 204 or json_response=="" or json_response["currently_playing_type"]=="ad"):
        boolVar = True
        while (boolVar):
            try:
                if(json_response["currently_playing_type"]=="ad"):
                    sendNotification("spotyLight", "An Ad Is Currently Playing")
                else:
                    sendNotification("spotyLight","Make sure one song is currently playing")
            except:
                print("Make sure one song is currently playing")
            response=getCurrentSong(link, accessToken)
            if(response.status_code == 200):
                json_response = response.json()
            if(response.status_code == 204 or json_response["currently_playing_type"]=="ad"):
                if (counter >9):
                    print("TimeOut: You are listening music no more \n Exit")
                    exit()
                else:
                    counter +=1
            else:

                boolVar=False
            time.sleep(10)

    json_response = response.json()


    song = {
            "name":json_response["item"]["name"],
            "album":json_response["item"]["album"]["name"],
            "imageUrl":json_response["item"]["album"]["images"][2]["url"],
            "artist":json_response["item"]["album"]["artists"][0]["name"]
        }        
    
    return song

