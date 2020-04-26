# PositionControl-SimplePendulum

Position control of a simple pendulum (One DOF) with architecture implemented in [LabVIEW FPGA](https://www.ni.com/es-mx/shop/select/labview-fpga-module) and Python through the [nifpga-python library](https://github.com/ni/nifpga-python).

# Methodology
A servomotor, controlled by means of an h-bridge is used for the change of rotation, to which a rotary encoder was included (Figure 1). Through this the desired pendulum position is controlled, in LabVIEW a module was implemented to read the pulses of the rotary encoder by means of an [X4 coding](http://www.ni.com/tutorial/7109/es/) and to be able to control the position of the servomotor with the help of the h-bridge.

<center>
  <figure>
    <img src="images\Rotatory encoder - servo motor.jpg?raw=true"
    alt="Figure 1"
    width="200"
    height="150">

  <figcaption>Figure 1. Namiki rotary encoder servo motor.</figcaption>
  </figure>
</center>

A model was designed in CAD for the structure where the servomotor and circuits were mounted (Figure 2,3).
<center>
  <figure>
    <img src="images\CAD design front view.jpg?raw=true"
    alt="Figure 2"
    width="200"
    height="250
    ">

  <figcaption>Figure 2. CAD design front view.</figcaption>
  </figure>
</center>

<center>
  <figure>
    <img src="images\CAD design back view.JPG?raw=true"
    alt="Figure 3"
    width="200"
    height="250
    ">

  <figcaption>Figure 3. CAD design back view.</figcaption>
  </figure>
</center>

The programming in LabVIEW is oriented to graphic programming called ["G"](https://wiki.c2.com/?GraphicalProgrammingLanguage), for which the programming was carried out in such a way that the signal of the rotary encoder is received, to know the position in which the axis of the servomotor is located. For this, in the programming logic, a calibration is performed to determine how many number of pulses of the rotary encoder correspond to 0 ° and 90 ° before entering a desired position in degrees. All this was done on a [screen](../master/Documentation/Screen) (Figure 4), using the [LabVIEW PID module](http://www.ni.com/tutorial/6931/en/) to control the position of the axis of the servomotor to which a bar is attached. By means of a PWM signal the speed of the motor shaft is controlled, this signal is generated based on the error and the PID.

<center>
  <figure>
    <img src="images\Screen.PNG?raw=true"
    alt="Figure 3"
    width="600"
    height="250
    ">

  <figcaption>Figure 4. Screen LabVIEW to controlled position and proof signals.</figcaption>
  </figure>
</center>

When the position control and test signals were performed on the LabVIEW Screen, the following steps were followed, taking as reference figure 4 for the virtual buttons:
1. "Prueba On/Off" button must be off.
2. Reset the encoder count value to 0 with "Reset Enc" button.
3. Manually place the end of the bar in the 90 ° position (using a protractor).
4. Press the "Calibrar" button to generate the conversion value
5. Leave "qd" at 0.
5. Turn on the "Prueba On/Off" button to return to position 0 automatically.
7. Start test signals (Step, Sine Wave).

The same idea was carried out in Python with the nifpga-python library, for this it is required to generate a .lvbitx file of the main program to perform the same functions as the Screen but in the Python terminal. The [Simple Pendulum - Python project](../master/Simple-Pendulum-Python/) when running the [main](../master/Simple-Pendulum-Python/Main/Main.py) file shows the following in the terminal:
```sh
Wave-Functions to simple pendulum
	1 - Sinusoidal Signal
	2 - Square Signal
	3 - Step Signal
	4 - Calibration Mode
	5 - Exit
Insert the number of the function to be tested:
```
