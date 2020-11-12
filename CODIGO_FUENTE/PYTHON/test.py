

class Student():

	def __init__(self,nombre,apellido,edad):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.__password=123

	def get_full_name(self):
		return self.nombre+' '+self.apellido


if __name__ == '__main__':

	st=Student("pepe","moreno",35)

	print(st.get_full_name())
