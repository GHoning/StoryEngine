class action:
	discription = "action"
	goto = 0
	
	def __init__(self, d, g) :
		self.description = d
		self.goto = g
		
class room:
	id = 0
	options = [action("do stuff", 1)]
	description = "testroom"