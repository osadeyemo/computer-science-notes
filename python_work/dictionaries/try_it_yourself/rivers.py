river_by_country = {
	'nile': 'egypt',
	'yangtze': 'china',
	'zaire river': 'congo'
	}

for river, country in river_by_country.items():
	print(f"\n{river.title()} runs through {country.title()}.")

for river in river_by_country.keys():
	print(f"\n{river.title()}")

for country in river_by_country.values():
	print(f"\n{country.title()}")