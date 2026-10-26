from random import *

lownumber = 10
highnumber = 20
# print("Sumado uno " + str((numero + 1)))
# print(f"Sumado uno {aleatorio + 1}")
# print("El numero que has escogido es: " + str(numero))

tries = 3
acierto = False

def askUser(numeroAleatorio, triesLeft):
    for i in range(0, tries):
        numero = int(input(f"Escoge un número entre {lownumber} y {highnumber}: "))
        if numero > numeroAleatorio:
            print("El número es menor")
        elif numero < numeroAleatorio:
            print("El numero es mayor")
        else:
            return numeroAleatorio, True;
    if triesLeft == 0:
        return numeroAleatorio, False
    return askUser(numeroAleatorio, triesLeft - 1)
    
numero, result = askUser(randint(lownumber, highnumber))

if result:
    print("¡Adivinaste el numero!")
else:
    print(f"El numero aleatorio era {numero}")