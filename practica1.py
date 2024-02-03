from Crypto.Util import number
import random
print("---------------------------------------------Ejercicio 1---------------------------------------------")
#Ejercicio 1
print('\n', "Ejercicio 1 - Obtener un num aleatorio de 256 bits usando la funcion random",
'\n', '\n', random.getrandbits(256), '\n')

print("---------------------------------------------Ejercicio 2---------------------------------------------")
#Ejercicio 2 obtener num aleatorio primo
i = 0
while(True):
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteración:", i, "se econtró el primo","\n", j, "\n")
        break


print("---------------------------------------------Ejercicio 3---------------------------------------------","\n")
#ejercicio 3 Inversio  multiplicativo
def inversMultiplicativo(x,y):
    print("El inverso multiplicativo de x: ", "\n", x, "\n", "De y: ","\n",  y,  "\n", "es: ", "\n", number.inverse(x,y), "\n")

a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversMultiplicativo(a,b)

print("---------------------------------------------Ejercicio 4---------------------------------------------","\n")
a = 2
b = random.getrandbits(256)
c = j

def poteencia(x,y,z):
    print("La potencia de x: ", "\n", x, "\n", "De y: ","\n",  y,  "\n", "mod z: ", "\n", z, "\n", "es: ", "\n", pow(x,y,z), "\n")

potencia(a,b,c)