def __init__(self, name, age):
	self.__age = age
	self.name = name

	def set_age(self, age):
		if age >= 0:
			self.__age = age
		else:
			print("invalid age")

	def get_age(self):
		return self.__age
	



