class car_oop:
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.__year = year

	def get_age(self):
		return self.__age

	def show_details(self):
		print(f"{self.brand} {self.model} {self.year}")