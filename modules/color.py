from colorthief import ColorThief

def getDominantColor():
    importedImage = ColorThief("./images/cover.jpg")
    domColor = importedImage.get_color()
    return list(domColor)