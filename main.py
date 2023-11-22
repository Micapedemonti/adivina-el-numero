"""
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas:
Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido.
Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro número. Y así hasta que gane o hasta que se agoten los ocho intentos."""

from random import *

nombre  = input("Por favor ingrese su nombre: ")


print(f"Hola {nombre} He pensado en un numero entre el 1 y el 100 y tienes solo 8 intentos para adivinar")
numero_secreto = randint(1,100)
intentos = 0

while intentos < 8:
    numero_usuario = int(input("Ingresa un numero: "))

    if numero_usuario == numero_secreto:
        print(f"Felicidades, has acertado! y has utilizado {intentos} intentos")
        break
    elif numero_usuario < numero_secreto:
        print("Incorrecto. El número secreto es mayor.")
    else:
        print("Incorrecto. El número secreto es menor.")

        intentos +=1
    if intentos == 8:
        print(f"Lo siento, has agotado todos los intentos, el numero secreto era {numero_secreto}")