def make_album(artist_name, album_name, tracks=None):
    """Create a dictionary for a music album."""
    album_data = {'artist': artist_name, 'album': album_name}
    if tracks:
        album_data['tracks'] = tracks
    return album_data

album = make_album('Tool', 'Aenima', '15')
print(album)

album2 = make_album('Miles Davis', 'Bitches Brew', '6')
print(album2)

album3= make_album('Godflesh', 'Hymns')
print(album3)