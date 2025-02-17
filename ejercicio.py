import RPi.GPIO as GPIO
import time
import random

# Configuración de pines
BOTON_COOPERAR = 17
BOTON_NO_COOPERAR = 27
LED_JUGADOR = 22
LED_MAQUINA = 23

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTON_COOPERAR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BOTON_NO_COOPERAR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_JUGADOR, GPIO.OUT)
GPIO.setup(LED_MAQUINA, GPIO.OUT)

# Variables de puntaje
puntos_jugador = 0
puntos_maquina = 0

pinRed = 5
pinGreen = 6
pinBlue = 13

# Configuración de los pines como salida
GPIO.setup(pinRed, GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue, GPIO.OUT)
# Configura el pin 7 como cooperar
GPIO.setup(pinCoop, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
# Configura el pin 11 como traicionar
GPIO.setup(pinTrai, GPIO.IN, pull_up_down=GPIO.PUD_UP)



rojo = GPIO.PWM(pinRed, 100)
verde = GPIO.PWM(pinGreen, 100)
azul = GPIO.PWM(pinBlue, 100)

rojo.start(0)
verde.start(0)
azul.start(0)

def cambiar_color(r, g, b):
    rojo.ChangeDutyCycle(r)
    verde.ChangeDutyCycle(g)
    azul.ChangeDutyCycle(b)

# Función para encender LED con color (simulando con encendido normal, usar RGB si aplica)
def mostrar_eleccion_jugador(coopera):
    if coopera:
        cambiar_color(0, 255, 0)
    else:
        cambiar_color(0, 0, 255)

def mostrar_eleccion_maquina(coopera):
    if coopera:
        cambiar_color(0, 255, 0)
    else:
        cambiar_color(0, 0, 255)

# Función para calcular puntaje
def calcular_puntaje(jugador, maquina):
    global puntos_jugador, puntos_maquina
    if jugador and maquina:
        puntos_jugador += 3
        puntos_maquina += 3
    elif jugador and not maquina:
        puntos_maquina += 5
    elif not jugador and maquina:
        puntos_jugador += 5
    else:
        puntos_jugador += 1
        puntos_maquina += 1

# Ciclo principal
try:
    while True:
        if GPIO.input(BOTON_COOPERAR) == GPIO.LOW:
            jugador_coopera = True
            mostrar_eleccion_jugador(True)
        elif GPIO.input(BOTON_NO_COOPERAR) == GPIO.LOW:
            jugador_coopera = False
            mostrar_eleccion_jugador(False)
        else:
            continue

        # Elección aleatoria de la máquina
        maquina_coopera = random.choice([True, False])
        mostrar_eleccion_maquina(maquina_coopera)

        # Calcular y mostrar puntaje
        calcular_puntaje(jugador_coopera, maquina_coopera)
        print(f"Puntaje - Jugador: {puntos_jugador} | Máquina: {puntos_maquina}")

        time.sleep(2)
        GPIO.output(LED_JUGADOR, GPIO.LOW)
        GPIO.output(LED_MAQUINA, GPIO.LOW)

except KeyboardInterrupt:
    print("Juego terminado")
    GPIO.cleanup()

