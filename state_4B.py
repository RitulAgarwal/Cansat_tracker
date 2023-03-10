from common_utils import collect_data, recieve_PXa_command, payload_released,capture_release_PXa,capture_descent_PXa

def tasks(calibrated_altitude):
    payload_released(2)
    payload_2_altitude=calibrated_altitude
    print("payload 2 altitude is {}".format(payload_2_altitude))
    recieve_PXa_command(2)
    capture_release_PXa(2)
    capture_descent_PXa(2)
    collect_data()
    
