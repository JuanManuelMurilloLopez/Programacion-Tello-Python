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
tello.move_down(20)

tello.move_left(20)
tello.move_right(20)

tello.move_back(20)
tello.move_forward(20)

# Aterrizaje
tello.land()
