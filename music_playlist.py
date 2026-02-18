#creates an empty playlist
playlist = []

#add song to playlist
def add_song(song):
    playlist.append(song)

def add_song_test():
    add_song("orion")
    if playlist[-1] == "orion":
        print("test works")

    else:
        print("test failed")

    add_song("mango")
    if playlist[-1] == "mango" and playlist[-2] == "orion":
        print("test works")

    else:
        print("test failed")

#delete song from playlist
def delete_song(song):
    if song in playlist:
        playlist.remove(song)

#reorder songs in playlist
def move_song(song, new_position):
    if song in playlist:
        playlist.remove(song)
        playlist.insert(new_position, song)

def move_song_test():
    move_song("mango", 0)
    if playlist[-1] == "mango":
        playlist.remove("mango")
        playlist.insert(0, "mango")

#prints the playlist with song name and artist
def display_playlist():
    #Megan Vuong suggested album cover jpeg displayed too
    return None