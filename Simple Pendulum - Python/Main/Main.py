import os
import sys
import numpy as np
from nifpga import Session

from Calibration.Encoder import *
from ProofSignals.Signals import *

with Session("Mybitfile.lvbitx", "rio://172.22.11.2/RIO0") as Session:
    Session.reset()
    Session.run()

    qd = Session.registers['qd']
    qr = Session.registers['qr']
    ResetPID = Session.registers['Reset PID']
    ResetEncoder = Session.registers['Reset Enc']
    PythonMode = Session.registers['Python Mode']

    # PID Gains for Python Mode
    P = Session.registers['P']
    I = Session.registers['I']
    D = Session.registers['D']

    # Gains
    PythonMode.write(True)
    P.write(np.uint16(15))
    I.write(np.uint16(0))
    D.write(np.uint16(8))

    print("Simple Pendulum by means an FPGA")

    # Calibration
    CalibrationValue = calibration(qr, ResetPID, ResetEncoder)
    qd.write(0)
    ResetPID.write(False)


    # Menu
    def menu():
        os.system('cls')
        print("Wave-Functions to simple pendulum")
        print("\t1 - Sinusoidal Signal")
        print("\t2 - Square Signal")
        print("\t3 - Step Signal")
        print("\t4 - Calibration Mode")
        print("\t5 - Exit")


    while True:
        menu()
        MenuOption = input("Insert the number of the function to be tested")

        if MenuOption == '1':
            print("Sinusoidal Signal")
            Amplitude = np.int16(input("Enter the amplitude in degrees"))
            Frequency = np.double(input("Enter the frequency in a range 0 to 1"))
            SimulationTime = np.int16(input("Enter simulation time"))

            sinusoidal(qd, qr, Amplitude, Frequency, SimulationTime, CalibrationValue)
            input("Test signal completed...\nPress a key to continue")

        elif MenuOption == '2':
            print("Square Signal")
            Amplitude = np.int16(input("Enter the amplitude in degrees"))
            Frequency = np.double(input("Enter the frequency in a range 0 to 1"))
            SimulationTime = np.int16(input("Enter simulation time"))

            square(qd, qr, Amplitude, Frequency, SimulationTime, CalibrationValue)
            qd.write(0)
            input("Test signal completed...\nPress a key to continue")

        elif MenuOption == '3':
            print("Step Signal")
            Amplitude = np.int16(input("Enter the amplitude in degrees"))
            Frequency = np.double(input("Enter the frequency in a range 0 to 1"))
            SimulationTime = np.int16(input("Enter simulation time"))

            step(qd, qr, Amplitude, Frequency, SimulationTime, CalibrationValue)
            input("Test signal completed...\nPress a key to continue")

        elif MenuOption == '4':
            CalibrationValue = calibration(qr, ResetPID, ResetEncoder)
            input("Calibration completed...\nPress a key to continue")

        elif MenuOption == '5':
            sys.exit()
            break

    Session.close()
