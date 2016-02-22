from tkinter import *
		
class Example():
	def __init__(self):
		self.testvariable = 10		

	def change_value(self):
		self.testvariable = 100


class Example2():
	def __init__(self):
		self.ex = Example()
		self.ex.change_value()
		self.return_value()

	def return_value(self):
		print(self.ex.testvariable)
		
		
poop = Example2()
poop.return_value()