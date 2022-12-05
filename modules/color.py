try:
    from colorthief import ColorThief
except:
    print("Make sure you have installed all the dependencies")
def getDominantColor():
    importedImage = ColorThief("./images/cover.jpg")
    domColor = importedImage.get_color()
    return list(domColor)