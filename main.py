import readchar


#Proyecto integrador parte 1

jugador = input("Hola, ¿Cual es tu nombre? : ")
print (f"Bienvenido a este maravilloso juego {jugador}")

#Proyecto integrador parte 2


while True:
    tecla = readchar.readkey()
    print(tecla)

    if tecla == '\x1b[A':  # Código de escape para la tecla de flecha hacia arriba
        break