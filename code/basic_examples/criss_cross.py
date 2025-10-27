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

# Esperar 2 segundos en el aire
time.sleep(2)

travel_distance_cm = 20

"""
Flight Pattern
    2     4
    |\   /|
    | \ / |
    |  \  |
    | / \ |
   1 5   3
"""

tello.go_xyz_speed(0, 0, travel_distance_cm, 20)
time.sleep(0.5)
tello.go_xyz_speed(0, 0, travel_distance_cm, -travel_distance_cm, 20)
time.sleep(0.5)
tello.go_xyz_speed(0, 0, travel_distance_cm, 20)
time.sleep(0.5)
tello.go_xyz_speed(0, -travel_distance_cm, -travel_distance_cm, 20)

# Aterrizaje
tello.land()
