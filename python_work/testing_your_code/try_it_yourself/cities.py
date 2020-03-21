from city_functions import city_country

print("Enter 'q' at any time to quit.")
while True:
	city = input("\nPlease give me a city's name: ")
	if city == 'q':
		break
	country = input("What country is this city located? ")
	if country == 'q':
		break

	formatted_city_and_country = city_country(city, country)
	print(formatted_city_and_country)

