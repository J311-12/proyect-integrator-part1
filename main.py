import readchar
import os


#Proyecto integrador parte 1

jugador = input("Hola, ¿Cual es tu nombre? : ")
print (f"Bienvenido a este maravilloso juego {jugador}")

#Proyecto integrador parte 2


while True:
    tecla = readchar.readkey()
    print(tecla)

    if tecla == '\x1b[A':  # Código de escape para la tecla de flecha hacia arriba
        break
    


#Proyecto integrador parte 3

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_numero(numero):
    clear_terminal()
    print(numero)

numero = 0

while numero <= 50:
    tecla = input("Presiona 'n' y luego Enter para continuar: ")

    if tecla == 'n':
        imprimir_numero(numero)
        numero += 1
