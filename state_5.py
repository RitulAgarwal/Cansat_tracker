import time


def tasks(calibrated_altitude):
    deactivate_camera()
    activate_buzzer()
    get_cx_off_command()
    cx_off_command_recieved()
    turn_off_telemetry()
    cansat_landing_time = time.time()
    print("--------STOPPING TIME IS {}----------".format(cansat_landing_time))
    return cansat_landing_time


def deactivate_camera():
    print("Camera Deactivated!")
    return
def activate_buzzer():
    print("Activating Buzzer!")
    # activate_buzzer is a boolean variable set to true 
    activate_buzzer = True
    print("activate_buzzer ",activate_buzzer )
    return
def get_cx_off_command():
    print("Getting CX OFF Command!!")
    return
def cx_off_command_recieved():
    print("CX OFF command received!!")
    return True
def turn_off_telemetry():
    print("Turned off Telemetry!")
    return
    