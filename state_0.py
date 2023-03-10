def tasks(calibrated_altitude):
    get_calibration_command()
    #is_system_calibrated()
    while not is_system_calibrated() :
        get_calibration_command()
    get_cx_on_command()
    #cx_on_command_received()
    while not cx_on_command_received() :
        get_cx_on_command()
    get_st_command()
    #st_command_received()
    while not st_command_received() :
        get_st_command()

def get_calibration_command():
    print("Getting Calibration Command...")
    return 
def is_system_calibrated():
    print("System Is Calibrated!!")
    return True
def get_cx_on_command():
    print("Getting CX ON command...")
    return
def cx_on_command_received():
    print("CX ON command Recieved!!")
    return True
def get_st_command():
    print("Getting ST command...")
    return
def st_command_received():
    print("ST command received...")
    return True

