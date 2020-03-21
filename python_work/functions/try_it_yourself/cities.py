def describe_city(city_name, city_country= 'the united states'):
	print(f"{city_name.title()} is in {city_country.title()}.")

describe_city('new york')
describe_city(city_name= 'chicago')
describe_city(city_country= 'nigeria', city_name= 'lagos')