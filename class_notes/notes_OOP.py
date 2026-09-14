class Person():
	def __init__(self, name, age, favorite_colors, hw_scores=[100,100,100]):
		self.name = name
		self.age = age
		self.favorite_colors = favorite_colors
		self.hw_scores = hw_scores

	def __str__(self): 
		return self.name + "is" + str(self.age) + "years old, and favorite color(s) are:" + str(self.favorite_colors)
		
	def calc_avg_grades(self):
		return np.mean(self.hw_scores)
	
	def set_name(self, name):
		self.name = name


alex_person = Person("alex", 43, ["sage green", "forest green"], [95,85,92])

print(alex_person)



