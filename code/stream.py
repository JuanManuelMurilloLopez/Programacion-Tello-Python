from djitellopy import Tello
import time
import cv2

# Creación del objeto Tello
tello = Tello()

# Conexión con el Dron
tello.connect()

# Mostramos el nivel de batería del Dron
battery_level = tello.get_battery()
print(f"Batería: {battery_level}")

# Inicializar cámara
tello.streamon()
print(f"Cámara inicializada")
frame_read = tello.get_frame_read()

# Despegue
tello.takeoff()

# Esperar 2 segundos en el aire
time.sleep(2)

# Tomar fotografía
tello_video_image = frame_read.frame
cv2.imwrite("tello_picture.png", tello_video_image)

# Aterrizaje
tello.land()

# Finalizar cámara
tello.streamoff()

