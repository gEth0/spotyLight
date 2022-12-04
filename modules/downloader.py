import requests 

def downloadCover(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("./images/cover.jpg","wb") as cover:
            cover.write(response.content)