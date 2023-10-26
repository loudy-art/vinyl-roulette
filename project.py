
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import config

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id, client_secret=config.client_secret, redirect_uri="http://localhost:3000", scope="user-library-read"))

# Define an array of seed artist IDs (replace with valid artist IDs)
seed_artist_ids = [
    "spotify:artist:2ZvrvbQNrHKwjT7qfGFFUW",
    "spotify:artist:3IKV7o6WPphDB7cCWXaG3E",
    "spotify:artist:5Jgj5Yo5deJ2RPlixBm88u",
    "spotify:artist:5CjlZu8c45u0rRvyONtxsn",
    "spotify:artist:0MaM0yE9EdQEJwDfs6EAZ9"
]

# Define an array of seed tracks (replace with valid track IDs)
seed_tracks = [
    "spotify:track:10Ac6tmpWew75o3yfIo3Xd",
    "spotify:track:6c0ziyel6ZMTQ37vKRooGZ",
    "spotify:track:7r6bRPWi8nxQ3AUu9aOgSY",
]

# Randomly select a seed artist and seed track
random_seed_artist = random.choice(seed_artist_ids)
random_seed_track = random.choice(seed_tracks)

#print("Random Seed Track:")
#print(random_seed_track)

# Perform a search for album recommendations based on the random seed artist and seed track
results = sp.recommendations(seed_artists=[random_seed_artist], seed_tracks=[random_seed_track], limit=1)

# Check if there are album recommendations
if results and 'tracks' in results:
    # Get the first recommended track's album information
    recommended_album = results['tracks'][0]['album']

    # Print the details of the recommended album
    print(f"Album Name: {recommended_album['name']}")
    print(f"Artist: {', '.join([artist['name'] for artist in recommended_album['artists']])}")

    # Fetch the album's ID
    album_id = recommended_album['id']

    # Retrieve the tracks of the album
    album_tracks = sp.album_tracks(album_id)

    if album_tracks:
        # Randomly select and print one song from the recommended album
        random_song = random.choice(album_tracks['items'])
        print(f"Random song: {random_song['name']}")

else:
    print("No recommendations found based on the seed artist and seed track.")