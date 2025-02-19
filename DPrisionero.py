import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)

# Definición de pines
pinCoop = 19
pinTrai = 26

pinRed1 = 17
pinGreen1 = 27
pinBlue1 = 22

pinRed2 = 5
pinGreen2 = 6
pinBlue2 = 13

# Configuración de los pines como salida
GPIO.setup(pinRed1, GPIO.OUT)
GPIO.setup(pinGreen1, GPIO.OUT)
GPIO.setup(pinBlue1, GPIO.OUT)

GPIO.setup(pinRed2, GPIO.OUT)
GPIO.setup(pinGreen2, GPIO.OUT)
GPIO.setup(pinBlue2, GPIO.OUT)

# Configuración de los botones con pull-up
GPIO.setup(pinCoop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinTrai, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Inicialización de puntajes
puntaje1 = 0
puntaje2 = 0

# Configuración de PWM para colores
rojo1 = GPIO.PWM(pinRed1, 100)
verde1 = GPIO.PWM(pinGreen1, 100)
azul1 = GPIO.PWM(pinBlue1, 100)

rojo2 = GPIO.PWM(pinRed2, 100)  # Corregido
verde2 = GPIO.PWM(pinGreen2, 100)  # Corregido
azul2 = GPIO.PWM(pinBlue2, 100)  # Corregido

rojo1.start(0)
verde1.start(0)
azul1.start(0)

rojo2.start(0)
verde2.start(0)
azul2.start(0)

def cambiar_color(player, r, g, b):
    if player == 1:
        rojo1.ChangeDutyCycle(r)
        verde1.ChangeDutyCycle(g)
        azul1.ChangeDutyCycle(b)
    elif player == 2:
        rojo2.ChangeDutyCycle(r)
        verde2.ChangeDutyCycle(g)
        azul2.ChangeDutyCycle(b)

print("Presiona un botón para empezar a jugar")

while True:
    # Lee el estado de los botones (0 = presionado, 1 = no presionado)
    estadoCoop = GPIO.input(pinCoop)
    estadoTrai = GPIO.input(pinTrai)

    # Para activar el juego se debe presionar un botón
    if estadoCoop == 0 or estadoTrai == 0:
        # Jugador
        if estadoCoop == 0:
            print('Jugador coopera')
            cambiar_color(1, 0, 100, 0)  # Verde

        elif estadoTrai == 0:
            print('Jugador traiciona')
            cambiar_color(1, 100, 0, 0)  # Rojo

        time.sleep(2)

        # Máquina elige su jugada
        jugada = random.randint(1, 2)

        if jugada == 1:
            print('Máquina coopera')
            cambiar_color(2, 0, 100, 0)  # Verde
        elif jugada == 2:
            print('Máquina traiciona')
            cambiar_color(2, 100, 0, 0)  # Rojo

        # Suma de puntos (corregido)
        if jugada == 2 and estadoTrai == 0:
            puntaje1 += 3
            puntaje2 += 3
        elif jugada == 2 and estadoCoop == 0:
            puntaje1 += 0
            puntaje2 += 5
        elif jugada == 1 and estadoTrai == 0:
            puntaje1 += 5
            puntaje2 += 0
        elif jugada == 1 and estadoCoop == 0:
            puntaje1 += 1
            puntaje2 += 1

        print('Puntaje Jugador:', puntaje1)
        print('Puntaje Máquina:', puntaje2)

        # Apagar luces después de mostrar el resultado
        time.sleep(1)
        cambiar_color(1, 0, 0, 0)
        cambiar_color(2, 0, 0, 0)
