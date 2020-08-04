def make_album(artist_name, album_name, tracks=None):
    """Create a dictionary for a music album."""
    album_data = {'artist': artist_name, 'album': album_name}
    if tracks:
        album_data['tracks'] = tracks
    return album_data

while True:
    print("\nPlease enter the artist name.")
    print("\nEnter 'q'at any time to quit.")
    
    f_name = input("Artist name: ")
    if f_name == 'q':
        break
    
    print("\nNow enter the album name.")
    f_album = input("Album title: ")
    if f_album == 'q':
        break

    print("\nFinally the number of tracks.")
    f_tracks = input("Number of tracks: ")
    if f_album == 'q':
        break

    album = make_album(f_name, f_album, f_tracks)
    print("\n")
    print(album)
