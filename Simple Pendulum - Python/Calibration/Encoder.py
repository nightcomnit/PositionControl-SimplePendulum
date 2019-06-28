import time


def calibration(qr, ResetPID, ResetEncoder):
    """
    Function to obtain the calibration value of the pendulum, to be able to manipulate the pulses and
    degrees conversation.

    :param qr: Encoder reading to obtain the number of pulses equivalent to 90 degrees, previously
               initialized with the nifpga library.
    :param ResetPID: Variable to control the state of the button that reset the PID in LabVIEW main,
                     previously initialized with the nifpga library.
    :param ResetEncoder: Variable to control the state of the button that reset the encoder count in LabVIEW main,
                         previously initialized with the nifpga library.
    :return: The function return the conversation value to manipulate the data in pulses or degrees.
    """
    ResetPID.write(True)
    ResetEncoder.write(True)

    print("Calibration Mode")
    print("Place the pendulum in 0 degrees")
    time.sleep(10)
    print("Place the pendulum in 90 degrees")
    ResetEncoder.write(False)
    time.sleep(10)

    qr_pulses = qr.read()
    pulses2degrees = (qr_pulses / 90)

    print("Finished")

    return pulses2degrees
