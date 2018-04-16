def make_car(fabricante, modelo, **car_info):
	infos = {}
	infos["fabricante"] = fabricante
	infos["modelo"] = modelo
	for key, value in car_info.items():
		infos[key] = value
	return infos

car = make_car("subaru", "outback", color="blue", tow_package="True")
print(car)