try:
    import requests 
except:
    print("Make sure you have installed all the dependencies")
def downloadCover(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("./images/cover.jpg","wb") as cover:
            cover.write(response.content)