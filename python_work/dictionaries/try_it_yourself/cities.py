cities = {
	'bowie': {'county': 'prince george', 'population': 20_000, 'fact': 'black',},
	'silver spring': {'county': 'mountgemary', 'population': 25_000, 'fact': 'mix',},
	'warldorf': {'county': 'charles', 'population': 45_000, 'fact': 'white',},
	}
for city, info in cities.items():
	city = city.title()
	county = info['county']
	population = info['population']
	fact = info['fact']
	print(f"{city} is in {county} county. It has a population of {population} people and it is {fact}.")