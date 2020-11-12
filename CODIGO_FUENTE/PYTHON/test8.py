
def dividir(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		print("no se puede dividir")

def dividir2(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		raise

def nivel(num):
	if num<0:
		raise ValueError("Debe ser un numero positivo: "+str(num))
	else:
		return num

#print(dividir(2,0))
#print(dividir2(2,0))
print(nivel(-1))


'''
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
'''

'''
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'''

'''
try:
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
except (ZeroDivisionError, TypeError, NameError):
print('Your numbers were bogus ...')
'''
