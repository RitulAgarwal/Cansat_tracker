import time
def tasks(calibrated_altitude):
    release_cansat()
    cansat_release_time=time.time()
    print("----------STARTING TIME IS {}----------".format(cansat_release_time))
    return cansat_release_time

def release_cansat():
    print("CANSAT IS RELEASED FROM ROCKET")  
    cansat_released = True
    print("cansat_released ",cansat_released )
    return cansat_released