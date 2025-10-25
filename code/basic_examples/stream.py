from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

battery_level = tello.get_battery()
print(f"Batería: {battery_level}")

# Iniciar el stream del video
tello.stream_on()

# Obtener el objeto de lectura de frames
frame_read = tello.get_frame_read()

print("Presiona 'q' para salir del video")

while True:

    # Leer el frame actual
    frame = frame_read.frame

    # Desplegar el frame
    cv2.imshow("Tello Camera", frame)

    # Oprimir tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
tello.end()
cv2.destroyAllWindows()