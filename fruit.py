class Fruit:
	def __init__(self):
		print("This is a Fruit")
	def nutrition(self):
		print("This is a nutritious fruuit")
	def fruit_shape(self):
		print("Fruit got a round shape")
class Orange(Fruit):
	def __init__(self):
		print("This is an orange")
	def nutrition(self):
		super(Orange,self).nutrition()
		print("This fruit got vitamin C inside")
	def color(self):
		print("The fruit got orange color when it ripe")
f = Fruit()
f.nutrition()
f.fruit_shape()
print("*"*40)
o = Orange()
o.nutrition()
o.color()