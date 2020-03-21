def make_album(artist_name, album_title, number_of_songs= None):
	artist_info = {'name': artist_name, 'album': album_title}
	if number_of_songs:
		artist_info['number of songs'] = number_of_songs
	return artist_info

musician = make_album('dagrin', 'ceo')
print(musician)

musician = make_album('kizz daniel', 'nbs', number_of_songs= 18)
print(musician)

musician = make_album('simi', 'simisola')
print(musician)