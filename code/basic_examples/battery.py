from djitellopy import Tello

# Creación del objeto Tello
tello = Tello()

# Conexión con el Dron
tello.connect()

# Mostramos el nivel de batería del Dron
battery_level = tello.get_battery()
print(f"Batería: {battery_level}")