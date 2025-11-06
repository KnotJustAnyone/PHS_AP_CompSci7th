#creates and empty playlist
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

#prints the playlist with song name and artist
def display_playlist():
     for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")
    #Megan Vuong suggested album cover jpeg displayed too

#Save Playlist Function
def save_playlist(filename):
    """Saves the current playlist to a JSON file."""
    data = []

    # Convert each Song object to a dictionary
    for song in playlist:
        song_dict = {
            "title": song.title,
            "artist": song.artist,
            "album": song.album,
            "cover_image": song.cover_image
        }
        data.append(song_dict)

    # Write to JSON file with indentation for readability
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Playlist saved to '{filename}'.")
