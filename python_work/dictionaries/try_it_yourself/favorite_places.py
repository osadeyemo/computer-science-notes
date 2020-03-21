favorite_places = {
	'labi': ['nigeria', 'london', 'paris'],
	'moji': ['mexico', 'mali'],
	'ife': ['lagos', 'new york', 'chicago'],
	}

for name, places in favorite_places.items():
	name = name.title()
	print(f"What are your favorite places to visit, {name}?")
	print(f"{name.title()}'s favorite places are:")
	for place in places:
		place = (place.title())
		print(f"\t{place}")
