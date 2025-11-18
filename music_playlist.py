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
        
# test for delete_song
def delete_song_test():
    playlist.clear()
    add_song("orion")
    add_song("mango")
    add_song("zenith")

    delete_song("mango")
    if "mango" not in playlist:
        print("deleted existing song")
    else:
        print("could not delete song (fail)")

    before = playlist.copy()
    delete_song("banana")
    if playlist == before:
        print("ignored missing song")
    else:
        print("deleted non-existant song (fail)")

    delete_song("zenith")
    if "zenith" not in playlist:
        print("deleted last song")
    else:
        print("couldn't delete song (fail)")

    delete_song("orion")
    if playlist == []:
        print("deleted final song, playlist empty")
    else:
        print("playlist not empty (fail)")

    print("Final playlist state:", playlist)

#reorder songs in playlist
def move_song(song, new_position):
    if song in playlist:
        playlist.remove(song)
        playlist.insert(new_position, song)

#prints the playlist with song name and artist
def display_playlist():
    if not playlist:
        print("playlist empty")
        return

    print("Playlist:")
    for i, song in enumerate(playlist, start=1):
        title = song.get("title", "Unknown Title")
        artist = song.get("artist", "Unknown Artist")
        print(f"{i}. {title} — {artist}")
    for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")
    #Megan Vuong suggested album cov
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

def shuffle_playlist_test():
    playlist.clear()
    add_song("orion")
    add_song("mango")
    add_song("zenith")
    add_song("ember")
    add_song("nova")

    original = playlist.copy()

    shuffle_playlist()

    if sorted(original) == sorted(playlist):
        print("✔ Shuffle keeps all songs")
    else:
        print("✘ Shuffle lost or duplicated songs (fail)")

    if len(original) == len(playlist):
        print("✔ Playlist length unchanged")
    else:
        print("✘ Playlist length changed (fail)")

    if playlist == original:
        print("⚠ Shuffle resulted in same order — retrying...")
        shuffle_playlist()
        if playlist == original:
            print("✘ Shuffle did NOT change order (fail)")
        else:
            print("✔ Shuffle changed order on retry")
    else:
        print("✔ Shuffle changed order")

    print("Final shuffled playlist:", playlist)
