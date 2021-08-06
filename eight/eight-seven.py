def makeAlbum(artistName, albumTitle):
    artist = {
        'name': str(artistName),
        'album': str(albumTitle),
    },
    for number, info in range(2):
        print(f"Artist: {info['name'].title()}\nAlbum: {info['album'].title()}")

nameInput = input("Artist name?")
albumInput = input("Album title?")
makeAlbum(str(nameInput), str(albumInput))

# test