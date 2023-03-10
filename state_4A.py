
from common_utils import collect_data,payload_released,recieve_PXa_command,capture_descent_PXa,capture_release_PXa

def tasks(calibrated_altitude):
    payload_released(1)
    payload_1_altitude=calibrated_altitude
    print("altitude of payload 1 is {}".format(payload_1_altitude))
    recieve_PXa_command(1)
    capture_release_PXa(1)
    capture_descent_PXa(1)
    collect_data()
    