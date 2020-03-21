def make_car(manufacturer, model_name, **car_info):
	"""Build a dictionary containing everything we know about a user."""
	car_info['manufacturer'] = manufacturer
	car_info['model_name'] = model_name
	return car_info

car = make_car('honda', 'accord', color= 'silver', year= '2018')
print(car)