#creates and empty playlist
playlist = []
import random

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

#prints the playlist with song name and artist
def display_playlist():
     for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")
    #Megan Vuong suggested album cover jpeg displayed too

#Landon Blain-Count # of songs
def count_songs():
    print(f"Total songs in playlist: {len(playlist)}")

#Search for songs
def search_song(name):
    results = [song for song in playlist if name.lower() in song.lower()]
    if results:
        print("Found these songs:")
        for song in results:
            print(song)

#Shuffle 
    else:
        print("No songs found with that name.")     
def shuffle_playlist():
    random.shuffle(playlist)
    print("Playlist shuffled.")


