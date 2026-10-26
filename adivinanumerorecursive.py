from random import *

lownumber = 10
highnumber = 20

def askUser(numeroAleatorio, triesLeft):
    if triesLeft == 0:
        return numeroAleatorio, False
        
    numero = int(input(f"Escoge un número entre {lownumber} y {highnumber}: "))
    
    if numero > numeroAleatorio:
        print("El número es menor")
        return askUser(numeroAleatorio, triesLeft - 1)
    elif numero < numeroAleatorio:
        print("El número es mayor")
        return askUser(numeroAleatorio, triesLeft - 1)
    else:
        return numeroAleatorio, True

numero, result = askUser(randint(lownumber, highnumber), 3)

if result:
    print("¡Adivinaste el numero!")
else:
    print(f"El numero aleatorio era {numero}")