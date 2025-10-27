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

# Aterrizaje
tello.land()

# Mostramos el nivel de batería del Dron
battery_level = tello.get_battery()
print(f"Batería: {battery_level}")
