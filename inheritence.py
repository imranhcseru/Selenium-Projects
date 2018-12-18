class car:
	def __init__(self):
		print("Car instance")
	def drive(self):
		print("Car can drive")
	def stop(self):
		print("Car can be stoped")

class BMW(car):
	def __init__(self):
		print("BMW instance")
	def drive(self):
		super(BMW,self).drive()
		print("You are driving BMW")


c = car()
c.drive()
c.stop()
print("*"*40)
b= BMW()
b.drive()
b.stop()