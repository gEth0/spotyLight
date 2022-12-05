try:
    import requests
except:
    print("Make sure you have installed all the dependencies")
def getCurrentSong(link,accessToken):
    response = requests.get(link,headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {accessToken}"
    })

    json_response = response.json()

    try:
        song = {
            "name":json_response["item"]["name"],
            "album":json_response["item"]["album"]["name"],
            "imageUrl":json_response["item"]["album"]["images"][2]["url"],
            "artist":json_response["item"]["album"]["artists"][0]["name"]
        }
    except:
        print("Make sure the song is currently playing")
        exit()
    return song