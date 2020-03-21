def make_album(artist_name, album_title):
	artist_info = {'name': artist_name, 'album': album_title}
	return artist_info

while True:
	print("\nPlease tell me about artist and album:")
	print("(enter 'q' at any time to quit)")

	name = input("Arist name: ")
	if name == 'q':
		break
	album = input("Album title: ")
	if album == 'q':
		break

	artist_album = make_album(name, album)
	print(artist_album)