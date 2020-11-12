
'''
letra = input("Letra:")
if letra >= "A" and letra <= "Z":
	print("mayuscula")
elif letra >= "a" and letra <= "z":
	print("minuscula")
else:
	print("otro caracter")
'''

'''
numero = int(input("numero:"))
for cont in range(1,11):
	print("%d * %d = %d" % (numero,cont,numero*cont) )
'''

'''
numero = int(input("numero:"))
fact=1
for i in range(2,numero+1):
	fact*=i
print("res:",fact)
'''

'''
import os
num_secreto=int(input("numero secreto:"))
os.system("cls")
numero=int(input("numero:"))
while numero!=num_secreto:
	if numero<num_secreto:
		print("el numero es mayor")
	else:
		print("el numero es menor")
	numero=int(input("numero:"))
print("has adivinado el numero")
'''

'''
num=int(input("numero:"))
isPrimo=True
for item in range(2,num):
	if num%item==0:
		isPrimo=False
		break
if isPrimo:
	print("Es primo")
else:
	print("No es primo")
'''

'''
num=int(input("numero:"))
if num%2==0:
	print("Es numero par")
else:
	print("Es numero impar")
'''

'''
num=int(input("numero:"))
lista=[]
listaPares=[]
while num>=0:
	lista.append(num)
	if num%2==0:
		listaPares.append(num)
	num=int(input("numero:"))
print("El numero maximo es: %d"%(max(lista)))
print("Los numeros pares son:",sorted(listaPares))
'''

'''
lista=[1,3,5,7,8,9]
#lista2=lista[:]
#lista2.reverse()
lista2=lista[::-1]
print("Lista original",lista)
print("Lista invertida",lista2)
'''

'''
cadena=input("Ingrese cadena:")
lista=["hola","que","tal","juan","hola"]
print("Lista original:",lista)
if cadena in lista:
	print("Cuantas veces esta:",lista.count(cadena))
	cadenaNueva=input("Ingrese nueva cadena:")
	for item in lista:
		if item==cadena:
			index=lista.index(item)			
			#lista.pop(index)
			#lista.insert(index,cadenaNueva)
			lista[index]=cadenaNueva
print("Nueva lista:",lista)
'''

'''
lista=[1,2,3,4,5]
lista2=lista[:]
lista2.sort()
if lista==lista2:
	print("Lista ordenada")
else:
	print("Lista no ordenada")
#flag=True
#for i,j in zip(lista,lista2):
#	if i!=j:
#		print("La lista no esta ordenada")
#		flag=False
#		break
#if flag:
#	print("La lista esta ordenada")
'''

'''
lista=[x**2 for x in [2,3,4]]
lista=list(map(lambda x:x**2,[2,3,4]))
'''

'''
cadena=input("cadena=")
caracter=input("caracter=")
cadena2=caracter.join(cadena)
print(cadena2)
'''

'''
cadena=input("cadena=")
caracter=input("caracter=")
nuevaCadena=''
for item in cadena:
	if item.isdigit():
		nuevaCadena+=caracter
	else:
		nuevaCadena+=item
print(nuevaCadena)
'''

'''
cadena=input("cadena=")
lista=cadena.split(' ')
letraInicialLista=[]
palabraInicialLista=[]
#for item in range(0,len(lista)):
for palabra in lista:
	#letraInicialLista.append(lista[item][0])	
	letraInicialLista.append(palabra[0])	
	#if lista[item][0] =='a':
	if palabra.startswith('a') or palabra.startswith('A'):
		palabraInicialLista.append(palabra)
print(letraInicialLista)
print(cadena.title())
print(palabraInicialLista)
'''

'''
cad1=input("cadena1=")
cad2=input("cadena2=")
if cad1.find(cad2)!=-1:
	print('cadena 2 es subcadena')
else:
	print('no es subcadena')
print(cad1 if cad1<cad2 else cad2)
'''

'''
cadena=input("cadena=")
if cadena==cadena[::-1]:
	print("es un palindromo")
else:
	print("no es palindromo")
'''

'''
cadena=input("cadena=")
lista=cadena.split(" ")
dict1={}
for palabra in lista:	
	dict1[palabra]=lista.count(palabra)
print(dict1)
'''

'''
codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
} 
cadena=input("cadena=")
respuesta=str()
for caracter in cadena.upper():	
	respuesta+=codigo[caracter]
print(respuesta)
'''

'''
persona=input("persona=")
gusto=input("gusto=")
dict1={}

while persona != '-1':
	if persona not in dict1:
		dict1[persona]=[gusto]
	else:
		if gusto not in dict1[persona]:
			dict1[persona].append(gusto)
	persona=input("persona=")
	gusto=input("gusto=")
print(dict1)
'''

'''
divisa=input("divisa=")
dict1={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print(dict1.get(divisa.capitalize(),"La divisa no esta"))
'''

'''
dict1={}
dict1.setdefault('nombre',input("nombre="))
dict1.setdefault('edad',input("edad="))
dict1.setdefault('direccion',input("direccion="))
dict1.setdefault('telefono',input("telefono="))
print("{} tiene {} años, vive en {} y su número de teléfono es {}".\
	format(dict1.get('nombre'),dict1.get('edad'),dict1.get('direccion'),dict1.get('telefono')))
'''

'''
dict1={'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
fruta=input("fruta=").capitalize()
kilos=float(input("kilos="))
if fruta in dict1:
	print("valor total=",dict1.get(fruta)*kilos)
else:
	print("Fruta no encontrada")
'''

'''
import calendar
lista=input("fecha=").split('/')
print("{} de {} de {}".format(lista[0],calendar.month_name[int(lista[1])],lista[2]))
'''

'''
articulo=input("Articulo=")
precio=input("Precio de "+articulo+"=")
dict1={}
while articulo!='-1':
	dict1.setdefault(articulo,precio)
	articulo=input("Articulo=")
	precio=input("Precio de "+articulo+"=")
costo=int()
print("Lista de la compra")
for x,y in dict1.items():
	print(x,y)
	costo+=int(y)
else:
	print("Total es=",costo)
'''

'''
import shutil,os,sys
ruta = os.getcwd()+os.sep
origen = ruta+'origen.txt'
destino = ruta+'destino.txt'
try:
	shutil.copyfile(origen,destino)
	print("Archivo copiado")
except FileNotFoundError as e:
	print("Se ha producido un FileNotFoundError: %s " % e)
except:
	print("Se ha producido un error inesperado:"+sys.exc_info()[0])
'''

'''
file = None
try:
	file = open('ejemplo.txt', 'r')
except IOError as e:
	print(e)
else:
	s = file.read()
	print(s)
finally:
	if file is not None:
		file.close()
'''

'''
import pdb; pdb.set_trace()
def factorial(n):
	resultado=1
	for i in range(1,n+1):
		resultado*=i
	return resultado
if __name__ == '__main__':
	print(factorial(5))
'''

'''
def operar(n1,n2,*,operador='+',respuesta='El resultado es '):
	if operador=="+":
		return respuesta+str(n1+n2)
	elif operador=="-":
		return respuesta+str(n1-n2)
	else:
		return "Error"
'''

'''
def sumar(n,*args):
	resultado=n
	for i in args:
		resultado+=i
	return resultado
'''

'''
def saludar(nombre='pepe',**kwargs):
	cadena=nombre
	for i in kwargs.values():
		cadena+=" "+i
	return "hola "+cadena
'''

'''
def agrupar(files):
	dict1={}
	dict1=dict.fromkeys(files.values())
	for key in dict1.keys():
		lista=[]
		for llave,valor in files.items():
			if key==valor:				
				lista.append(llave)
				dict1[key]=lista
	return dict1
if __name__=='__main__':
	files={'input.txt':'juan','code.py':'diego','output.txt':'juan'}
	print(agrupar(files))
'''

'''
def calculo(fun):	
	def envoltura(numero):
		print("codigo comun para ambas funciones")
		fun(numero)
	return envoltura
@calculo
def potencia(numero):
	print("La potencia es %d" % (numero**2))
@calculo
def cubo(numero):
	print("El cubo es %d" % (numero**3))
'''

'''
def getSegundos(hora,minutos,segundos):
	return((hora*3600)+(minutos*60)+segundos)
def getHoraMinSeg(tsegundos):
	horas=int(tsegundos/3600)
	minutos=int(((tsegundos-(horas*3600))/60))
	segundos=int(tsegundos-(horas*3600+minutos*60))
	return("Hora:%d minutos:%d segundos:%d"%(horas,minutos,segundos))
def getTiempo(*args):
	if len(args)==3:
		return getSegundos(*args)
	elif len(args)==1:
		return getHoraMinSeg(*args)
	else:
		raise TypeError("Se espera 1 o 3 parametros")
'''

'''
def guardar_agenda(l_agenda,**kwargs):
    l_agenda.append(kwargs)
    return l_agenda
def main():
    agenda=[]
    cantidad = int(input("¿Cuántos contactos vas a introducir?"))
    for i in range(cantidad):
        contacto={}
        contacto["nombre"]=input("Indica el nombre:")
        contacto["telefono"]=input("Indica el teléfono:")
        campo=input("Introuzca otro campo:")
        while campo!="*":
            contacto[campo]=input("Introuzca valor:")
            campo=input("Introuzca otro campo:")
        agenda=guardar_agenda(agenda,**contacto)
    print(agenda)   
if __name__ == '__main__':
     main()
'''

'''
import csv
def calc_puntos(s1,s2):
	pg,pe,pp,puntos=0,0,0,0
	if s1>s2:pg=1;puntos=3
	elif s1<s2:pp=1;puntos=0
	else:pe=1;puntos=1
	return pg,pe,pp,puntos
def calc_score(marcador1,marcador2):
	pg,pe,pp,puntos=calc_puntos(marcador1.split('-')[0],marcador1.split('-')[1])
	pg2,pe2,pp2,puntos2=calc_puntos(marcador2.split('-')[0],marcador2.split('-')[1])
	return (pg+pg2),(pe+pe2),(pp+pp2),(puntos+puntos2)
def calc_tabla_pos(equipo,partidos):
	pg,pe,pp,puntos=0,0,0,0
	for item in partidos:
		if item[1]=='Barcelona':
			lpg,lpe,lpp,lpuntos=calc_score(item[3],item[4])
			pg+=lpg;pe+=lpe;pp+=lpp;puntos+=lpuntos
	print(pg,pp,pe,puntos)
def main():
	with open("liga.csv","r") as file:
		partidos=list(csv.reader(file))
	del partidos[0]
	tabla=[]
	for item in list(set([item[1] for item in partidos])):
		dict1={}
		dict1.setdefault('equipo',item)
		dict1.setdefault('pg',0)
		dict1.setdefault('pe',0)
		dict1.setdefault('pp',0)
		dict1.setdefault('puntos',0)
		tabla.append(dict1)
	calc_tabla_pos('Barcelona',partidos)
if __name__ == '__main__':
     main()
'''

'''
import math 
class Punto():
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def distancia(self,otro):
		dx=self.x-otro.x
		dy=self.y-otro.y
		return math.sqrt(dx*dx+dy*dy)
'''

'''
class Circulo():
	def __init__(self,radio):
		self.set_radio(radio)
	def set_radio(self,radio):
		if radio>=0:
			self.__radio=radio
		else:
			raise ValueError("Radio debe ser positivo")
	def get_radio(self):
		return self.__radio
if __name__ == '__main__':     
     cir=Circulo(45)
     print(cir.get_radio())
'''

'''
class Circulo():
	def __init__(self,radio):
		self.radio=radio
	@property
	def radio(self):
		return self.__radio
	@radio.setter
	def radio(self,radio):
		self.__radio=radio
if __name__ == '__main__':  
     cir=Circulo(45)
     print(cir.radio)
'''

'''
class Circulo():
	def __init__(self,radio):
		self._radio=radio
	def __str__(self):
		return "El radio es: {} ".format(self._radio)
if __name__ == '__main__':  
     cir=Circulo(45)
     print(cir)
'''

'''
class gato():
    def hablar(self):
        print("MIAU") 
class perro():
    def hablar(self):
        print("GUAU")
def escucharMascota(animal):
    animal.hablar()
if __name__ == '__main__':
    g = gato()
    p = perro()
    escucharMascota(g)
    escucharMascota(p)
'''

'''
class Animal():
	def __init__(self,nombre,genero):
		self._nombre=nombre
		self._genero=genero
class Perro(Animal):
	def __init__(self,nombre,genero,raza):
		Animal.__init__(self,nombre,genero)
		self._raza=raza
if __name__ == '__main__':
	p1=Perro("pepe","masculino","labrador")
	print(p1._nombre,p1._genero,p1._raza)
'''

'''
class Persona():
	def __init__(self,dni,nombre,edad):
		self.dni=dni
		self.nombre=nombre
		self.edad=edad
	@property
	def dni(self):
		return self._dni
	@dni.setter
	def dni(self,dni):
		self._dni=dni
	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self,nombre):
		self._nombre=nombre
	@property
	def edad(self):
		return self._edad
	@edad.setter
	def edad(self,edad):
		if edad>0:
			self._edad=edad	
		else:
			raise ValueError("Edad incorrecta")
	def __str__(self):
		return self.dni.__str__()+" "+self.nombre+" ("+str(self.edad)+")"
'''