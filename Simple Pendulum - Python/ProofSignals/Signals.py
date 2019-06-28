import time

import matplotlib.pyplot as plt
import numpy as np


def sinusoidal(qd, qr, Amplitude, Frequency, SimulationTime, ConversationValue):
    """
    Sine-wave test function for a simple pendulum given an Amplitude in degrees and a frequency.

    :param qd: Desired position of the pendulum given by the programming logic in LabVIEW and
               previously declared with the nifpga library.
    :param qr: Real position of the pendulum given by the programming logic in LabVIEW obtained
               by a rotary encoder and previously declared with the nifpga library.
    :param Amplitude: Amplitude of the test signal given in degrees
    :param Frequency: Frequency of the test signal with a range of 0 to 1, where for example 0.5
                      would be 50% of the frequency.
    :param SimulationTime: Simulation Time
    :param ConversationValue: Conversion value given by the previously performed conversion function
    :return: The function performs a sinusoidal test signal in real time through the nifpga library,
             in addition to the graph where the behavior of the signals can be observed and compared.
    """

    t = 0.0
    ti = [0.0]
    i = 0
    sin = [0.0]
    qr_data = [0]

    while True:
        time.sleep(0.005)
        t += 0.005
        print(t)
        ti.append(t)

        SignalSin = Amplitude * np.sin(2 * np.pi * ti[i] * Frequency)
        sin.append(SignalSin)

        qd_degrees2pulses = np.int16(SignalSin * ConversationValue)
        qd.write(qd_degrees2pulses)

        qr_real = qr.read()
        qr_data_pulses2degrees = (qr_real / ConversationValue)
        qr_data.append(qr_data_pulses2degrees)

        i += 1
        if t >= SimulationTime:
            break

    plt.title("Graph of the real signal and the sinusoidal signal")
    plt.grid()
    plt.plot(ti, sin, 'b--', label="Sinusoidal signal")
    plt.plot(ti, qr_data, 'k--', label="Real position - $q_r$")
    plt.xlabel("Simulation Time(seconds)")
    plt.ylabel("Amplitude(Degrees)")
    plt.legend()
    plt.show()


def square(qd, qr, Amplitude, Frequency, SimulationTime, ConversationValue):
    """
    Square-wave test function for a simple pendulum given an Amplitude in degrees and a frequency.

    :param qd: Desired position of the pendulum given by the programming logic in LabVIEW and
               previously declared with the nifpga library.
    :param qr: Real position of the pendulum given by the programming logic in LabVIEW obtained
               by a rotary encoder and previously declared with the nifpga library.
    :param Amplitude: Amplitude of the test signal given in degrees
    :param Frequency: Frequency of the test signal with a range of 0 to 1, where for example 0.5
                      would be 50% of the frequency.
    :param SimulationTime: Simulation Time
    :param ConversationValue: Conversion value given by the previously performed conversion function
    :return: The function performs a square test signal in real time through the nifpga library,
             in addition to the graph where the behavior of the signals can be observed and compared.
    """
    global Square
    t = 0.0
    ti = [0.0]
    i = 0
    sqr = [0.0]
    qr_data = [0]

    while True:
        time.sleep(0.005)
        t += 0.005
        print(t)
        ti.append(t)

        S = Amplitude * np.sin(2 * np.pi * ti[i] * Frequency)
        Sqrt = (1 / 2 * Frequency)

        if Sqrt >= S:
            Square = Amplitude
        elif Sqrt <= S:
            Square = 0

        sqr.append(Square)

        qd_degrees2pulses = np.int16(Square * ConversationValue)
        qd.write(qd_degrees2pulses)

        qr_real = qr.read()
        qr_data_pulses2degrees = (qr_real / ConversationValue)
        qr_data.append(qr_data_pulses2degrees)

        i += 1
        if t >= SimulationTime:
            break

    plt.title("Graph of the real signal and the sinusoidal signal")
    plt.grid()
    plt.plot(ti, sqr, 'b--', label="Square signal")
    plt.plot(ti, qr_data, 'k--', label="Real position - $q_r$")
    plt.xlabel("Simulation Time(seconds)")
    plt.ylabel("Amplitude(Degrees)")
    plt.legend()
    plt.show()


def step(qd, qr, Amplitude, Frequency, SimulationTime, ConversationValue):
    """
    Step-wave test function for a simple pendulum given an Amplitude in degrees and a frequency.

    :param qd: Desired position of the pendulum given by the programming logic in LabVIEW and
               previously declared with the nifpga library.
    :param qr: Real position of the pendulum given by the programming logic in LabVIEW obtained
               by a rotary encoder and previously declared with the nifpga library.
    :param Amplitude: Amplitude of the test signal given in degrees
    :param Frequency: Frequency of the test signal with a range of 0 to 1, where for example 0.5
                      would be 50% of the frequency.
    :param SimulationTime: Simulation Time
    :param ConversationValue: Conversion value given by the previously performed conversion function
    :return: The function performs a step test signal in real time through the nifpga library,
             in addition to the graph where the behavior of the signals can be observed and compared.
    """
    global Step
    t = 0.0
    ti = [0.0]
    i = 0
    stp = [0.0]
    qr_data = [0]

    while True:
        time.sleep(0.005)
        t += 0.005
        print(t)
        ti.append(t)

        Step_p = (1 / 2 * Frequency)

        if Step_p >= ti[i]:
            Step = Amplitude
        elif Step_p <= ti[i]:
            Step = 0

        stp.append(Step)

        qd_degrees2pulses = np.int16(Step * ConversationValue)
        qd.write(qd_degrees2pulses)

        qr_real = qr.read()
        qr_data_pulses2degrees = (qr_real / ConversationValue)
        qr_data.append(qr_data_pulses2degrees)

        i += 1
        if t >= SimulationTime:
            break

    plt.title("Graph of the real signal and the sinusoidal signal")
    plt.grid()
    plt.plot(ti, stp, 'b--', label="Step signal")
    plt.plot(ti, qr_data, 'k--', label="Real position - $q_r$")
    plt.xlabel("Simulation Time(seconds)")
    plt.ylabel("Amplitude(Degrees)")
    plt.legend()
    plt.show()
