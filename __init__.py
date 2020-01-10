class Students():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def walk(self):
		print(self.name, "can walk")
		print(self.name, "is", self.age)

Student1 = Students("inty", 18)
Student1.walk()

Student2 = Students("Kyo", 23)
Student2.walk()