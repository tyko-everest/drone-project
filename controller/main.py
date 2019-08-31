from inputs import get_gamepad
import serial
import time

SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

def main():
    # x box one controller uses unsigned 10 bit number for triggers
    # uses 16 bit signed number for joystick axes
    # y is inverted, down is positive from input, it gets inverted immediately
    throttle = 0
    x_vel = 0
    y_vel = 0

    with serial.Serial(SERIAL_PORT, BAUD_RATE) as ser:
        while (1):
            event = get_gamepad()[0]
            # all events that control flight are this type
            if event.ev_type == "Absolute":
                # this is left trigger, used for throttle
                if event.code == "ABS_RZ":
                    throttle = event.state
                # control direction side to side
                if event.code == "ABS_X":
                    x_vel = event.state
                # control direction forward and back
                if event.code == "ABS_Y":
                    y_vel = -1 * event.state

            # message = str(event.ev_type) + "," + str(event.code) + \
            #         "," + str(event.state) + "\n\r"
            message = str(throttle) + "," + str(x_vel) + "," + str(y_vel) + "\n\r"
            ser.write(bytearray(message, "utf8"))

if __name__ == "__main__":
    main()