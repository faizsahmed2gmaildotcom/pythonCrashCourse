def makeAlbum(artistName, albumTitle):
    print(f"Artist: {artistName.title()}\nAlbum: {albumTitle.title()}")

quitInput = 'no'

while quitInput == 'no':
    nameInput = input("Artist name?")
    albumInput = input("Album title?")
    makeAlbum(nameInput, albumInput)
    quitInput = input("Quit? (<return> to quit, or 'no' to repeat)")
