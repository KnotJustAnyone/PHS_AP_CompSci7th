#Creates and empty playlist
playlist = []
import random

#Save playlist
def save_playlist(filename):
    with open(filename, "w") as file:
        json.dump(playlist, file, indent=4)
    print("Playlist saved.")

#instructions to user/how-to message
print("You're ready to start creating your music playlist!")
print("To add a song, type: add <songname>")
print("To delete a song, type: delete <songname>")
print("To shuffle the playlist, type: shuffle")

#creates a variable that stores the user's input
user_input = input()

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

#user input to add song
if user_input.startswith("add "):
    song = user_input[4:]  # everything after "add "
    add_song(song)
    print(f'"{song}" added to playlist.')

#Delete song from playlist
def delete_song(song):
    if song in playlist:
        playlist.remove(song)
        
#Test for delete_song
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

#user input to delete song
if user_input.startswith("delete "):
    song = user_input[7:]
    delete_song(song)
    print(f'"{song}" removed from playlist.')

#reorder songs in playlist
def move_song(song, new_position):
    if song in playlist:
        playlist.remove(song)
        playlist.insert(new_position, song)

# Prints the playlist with song name and artist
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
    # Megan Vuong suggested album cov
    # Megan Vuong suggested album cover jpeg displayed too

def save_playlist(filename):
    """Saves the current playlist to a JSON file."""
    # Check if playlist is empty
    if not playlist:
        print("Cannot save: playlist is empty.")
        return
    
    # Check if filename is provided
    if not filename:
        print("Error: filename is required.")
        return
    
    # Ensure filename ends with .json extension
    if not filename.endswith('.json'):
        filename = filename + '.json'
    
    # Old code - commented out because songs are strings, not objects
    # data = []
    # # Convert each Song object to a dictionary
    # for song in playlist:
    #     song_dict = {
    #         "title": song.title,
    #         "artist": song.artist,
    #         "album": song.album,
    #         "cover_image": song.cover_image
    #     }
    #     data.append(song_dict)
    
    # New code - works with string songs
    # Create a list to store the playlist data
    data = []
    for song in playlist:
        # Since songs are strings, we'll save them directly
        # Could be enhanced later to parse song strings if needed
        data.append(song)
    
    # Write to JSON file with indentation for readability
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Playlist saved successfully to '{filename}'.")
        print(f"Total songs saved: {len(data)}")
    except Exception as e:
        print(f"Error saving playlist: {e}")
#Landon Blain-Count # of songs
def count_songs():
    print(f"Total songs in playlist: {len(playlist)}")

# Search for songs
def search_song(name):
    results = [song for song in playlist if name.lower() in song.lower()]
    if results:
        print("Found these songs:")
        for song in results:
            print(song)

# Shuffle 
    else:
        print("No songs found with that name.")     
def shuffle_playlist():
    if len(playlist) <= 1:
        print("Not enough songs to shuffle.")
        return

    original = playlist.copy()

    while True:
        random.shuffle(playlist)
        if playlist != original:
            break

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

#user input for shuffle
if user_input == "shuffle":
    shuffle_playlist()
