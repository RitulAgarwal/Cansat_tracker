import state_0 as s0
import state_1 as s1
import state_2 as s2
import state_3 as s3
import state_4A as s4A
import state_4B as s4B
import state_5 as s5
import common_utils as cm



def initialise_system(start):
    print("Initialising System...")
    if start:
        return '0'
    else:
        return '-1'
    
if __name__ == "__main__":
    #setting the start boolean true
    start = True
    #setting state 0 initially
    state = initialise_system(start)
    #dictionary for states to modules
    state_to_module_map = {
        '0':s0,
        '1':s1,
        '2':s2,
        '3':s3,
        '4A':s4A,
        '4B':s4B,
        '5':s5
    }
    
    sample_interval = int(input("Kindly enter the altitude distance after which u wanna monitor its state \nFor example:30 will tell you the state after every 30 metres\n"))
    # 800 is an imaginary value as the maximum altitude of cansat..it can be changed
    altitude_list = list(range(cm.calibrate,800+cm.calibrate))[::sample_interval] + list(range(cm.calibrate,800+cm.calibrate))[::-sample_interval] +[cm.calibrate]
    
    for altitude in altitude_list:
        state = cm.update_state(state,altitude)
        calibrated_altitude = altitude
        outs = state_to_module_map[state].tasks(calibrated_altitude)
        print("==========State : {} ; Altitude : {}==========".format(state,altitude))
        if state == '2':
            cansat_release_time = outs
        elif state == '5':
            cansat_landing_time = outs
    
    time_of_gliding = cansat_landing_time-cansat_release_time
    print("the time of cansat flight is %s" % time_of_gliding)
        
"""errors in flowchart (FC)....
1.in state 1 of FC,if rocket is not rising,we're setting it to state=2 
i think..rocket should be rising and altitude>=725..only then state = 2 must be on
2.in state 4A of FC,if altitude<400,we're not going to state 4B..so i think 
arrow of NO must be directing of capture release and descent..coz payload will be 
released only once in 4A and we'll not be changing the altitude like <500
3.state cannot be an integer variable as it includes 4A and $b

"""

