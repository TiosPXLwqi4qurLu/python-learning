# inheritance 遗传
# override 重载

class Father():
	name = "Kyo"
	def eat(self):
		print("I can eat")

class Mother():
	def walk(walk):
		print("I can walk")

class Son(Father,Mother):
	def eat(self):
		print("I eat like son")

littleKyo = Son()
littleKyo.eat()
littleKyo.walk()
git remote add origin git@github.com:TiosPXLwqi4qurLu/python-learning.git