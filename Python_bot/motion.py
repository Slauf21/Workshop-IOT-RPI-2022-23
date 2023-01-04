from gpiozero import MotionSensor
import time

pir = MotionSensor(24)

# Aansturen beweginssensor
def motion_det():
    try:
        while True:
            if pir.motion_detected:
                print("Beweging gedetecteerd -> dief!!!!!!!" + " " + (time.strftime("%H:%M:%S")))
                time.sleep(3)
            else:
                time.sleep(3)

    except KeyboardInterrupt:
        print('interrupted!')

motion_det()