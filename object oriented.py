# object oriented

class Student():
	name = "Kyo"
	def eat(self, ):
		print(self.name, "can eat")
	@staticmethod
	def study():
		print("student can study")

Student().eat()
Student().study()
