

#1 Solución


def longitud_de_ultima_palabra(s):
        words = s.split()
        if len(words) == 0:
            return 0
        return len(words[-1])

print(longitud_de_ultima_palabra("Python Exercises"))
print(longitud_de_ultima_palabra("Python"))
print(longitud_de_ultima_palabra(""))
print(longitud_de_ultima_palabra("  "))




#2
def mayuscula_primer_ultimo_caracter(frase):
    resultado=''
    for p in frase.split():
        resultado += p[0].upper() + p[1:-1] + p[-1].upper() + ' '
    return resultado
texto="python"
print(texto)
print(mayuscula_primer_ultimo_caracter(texto))


#3

class Circle():
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius**2*3.14
        
 
    
NewCircle = Circle(2)
print(NewCircle.area())






#4
class Rectangulo():
    def __init__(self, l, a):
        self.largo = l
        self.ancho = a

    def rectangulo_area(self):
        return self.largo*self.ancho

newRectangulo = Rectangulo(13, 8)
print(newRectangulo.rectangulo_area())

#5


class student:
    def __init__(display,name,registro):
        display.name=name
        display.registro=registro
    def setAge(setAge,edad):
        setAge.edad=edad
    def setNota(setNota,nota):
        setNota.nota=nota
    def display(curso):
        print('name:'+ curso.name)
        print('registro:'+ str (curso.registro))
        print('edad:'+ str (curso.edad))
        print('nota:'+ str (curso.nota))
student_one= student ('lucas',1)
student_one.setAge(12)
student_one.setNota(15)
student_one.display()



#6


while True:
    try:
        numberList = []
        print("ingresar los numeros ',' con separador")

        break
    except:
        print('mensaje:debe escribir un valor valido')
    print()
try:
    numberList = [int(i) for i in input().split(',')]
    print("Average = ", sum(numberList)/len(numberList))
except ZeroDivisionError as e:
    print('error:',e)

#7
def pascal_triangulo(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangulo(5)
#8

import random

for i in range(20):
    print(random.uniform(0, 100))
    


























         










          





