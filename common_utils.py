def set_time():
    print("SETTING Time")

def check_packet_count():
    no_of_packs=[1,2,3]
    print("counting number of packets...")
    
def collect_data():
    print("Collecting Data")
    check_packet_count()

def save_data():
    print("Saving data to SD card")
    
def payload_released(a):
    print("Payload %d is released" % a )
def recieve_PXa_command(a):
    print("Recieve PX%d command and send PX%d to payload!" % (a,a))
def capture_release_PXa(a):
    print("Capture the release of payload %d" % a)
def capture_descent_PXa(a):
    print("Capture the descent of payload %d"%a)

calibrate = int(input("Kindly enter the altitude you are currently on!(calibrate)\n"))

def update_state(state,altitude):
    if state=='0' and altitude < 5 + calibrate:
        return '0'
    elif state=='0' and altitude>=5+calibrate:
        return '1'
    elif state=='1'and altitude < 725+calibrate:
        return '1'
    elif state=='1'and altitude >=725+calibrate:
        return '2'
    elif state =='2':
        return '3'  
    elif state=='3'and altitude >=500+calibrate:
        return '3'
    elif state =='3' and altitude < 500+calibrate:
        return '4A'
    elif state == '4A' and altitude<400+calibrate:
        return '4B'
    elif state == '4A' and altitude>=400+calibrate:
        return '4A'
    elif state == '4B' and altitude >=5+calibrate:
        return '4B'
    elif state == '4B' and altitude < 5+calibrate:
        return '5'


        
    