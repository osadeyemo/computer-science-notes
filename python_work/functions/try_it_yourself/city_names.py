def city_country(city, country):
	string_format = f"{city}, {country}"
	return string_format.title()

city = city_country('chicago', 'united states')
print(city)

city = city_country('lagos', 'nigeria')
print(city)

city = city_country('hong kong', 'china')
print(city)