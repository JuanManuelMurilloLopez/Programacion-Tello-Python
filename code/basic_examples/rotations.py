from djitellopy import Tello
import time

# Creación del objeto Tello
tello = Tello()

# Conexión con el Dron
tello.connect()

# Mostramos el nivel de batería del Dron
battery_level = tello.get_battery()
print(f"Batería: {battery_level}")

# Despegue
tello.takeoff()

tello.move_up(40)

tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)

# Aterrizaje
tello.land()
