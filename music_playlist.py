#creates and empty playlist
playlist = []

#add song to playlist
def add_song(song):
    playlist.append(song)

#delete song from playlist
def delete_song(song):
    if song in playlist:
        playlist.remove(song)

#reorder songs in playlist
def move_song(song, new_position):
    if song in playlist:
        playlist.remove(song)
        playlist.insert(new_position, song)

#prints the playlist with song name and artist
def display_playlist():
    #Megan Vuong suggested album cover jpeg displayed too