class Student:
	def __init__(self,name):
		self.name=name
	def show(self):
		print("Name\t:"+self.name)
	def random(self):
		print("A random method in the base class")

class RegularStudent(Student):
	def __init__(self,name):##overrides the base class method and calls the base class method
		self.age=22
		Student.__init__(self,name)
	def show(self): ##redefines the base class method
		print("Name (derived class)\t:"+self.name+" Age\t:"+str(self.age))
	def random(self):
		print("Random method in the derived class")

naks = Student("Nakul")
hari = RegularStudent("Harsh")
naks.show()
hari.show()
## The variables can be seen outside the class also
print(naks.name)
print(hari.name) 
  
