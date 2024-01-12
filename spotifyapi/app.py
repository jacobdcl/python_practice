import tkinter as tk
from tkinter import scrolledtext
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_top_tracks():
    artist_name = artist_name_entry.get()
    client_id = "1abcb59f350e4e1896b0adfca7b2f0bb"
    client_secret = "e101e5f0f1ee44f98c3b24208c1f72b5"

    credentials = SpotifyClientCredentials(client_id="1abcb59f350e4e1896b0adfca7b2f0bb", client_secret="e101e5f0f1ee44f98c3b24208c1f72b5")
    spotify = spotipy.Spotify(client_credentials_manager=credentials)

    results = spotify.search(q='artist:' + artist_name, type='artist')
    if results['artists']['items']:
        artist = results['artists']['items'][0]
    else:
        output_text.insert(tk.INSERT, "No artist found with the name " + artist_name + "\n")
        return

    top_tracks = spotify.artist_top_tracks(artist['id'])
    output_text.insert(tk.INSERT, "Top 5 tracks of " + artist_name + ":\n")
    for i, track in enumerate(top_tracks['tracks'][:5]):
        output_text.insert(tk.INSERT, f"{i + 1}. {track['name']}\n")

# Creating the main window
root = tk.Tk()
root.title("Spotify Top Tracks Finder")

# Creating widgets
artist_name_label = tk.Label(root, text="Artist Name:")
artist_name_entry = tk.Entry(root, width=50)


search_button = tk.Button(root, text="Find Top Tracks", command=get_top_tracks)

output_text = scrolledtext.ScrolledText(root, width=60, height=10)

# Placing widgets
artist_name_label.pack()
artist_name_entry.pack()

search_button.pack()

output_text.pack()

# Running the application
root.mainloop()
