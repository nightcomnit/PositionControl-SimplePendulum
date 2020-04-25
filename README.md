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

The programming in LabVIEW is oriented to graphic programming called ["G"](https://wiki.c2.com/?GraphicalProgrammingLanguage), for which the programming was carried out in such a way that the signal of the rotary encoder is received, to know the position in which the axis of the servomotor is located. For this, in the programming logic, a calibration is performed to determine how many number of pulses of the rotary encoder correspond to 0 ° and 90 ° before entering a desired position in degrees. All this was done on a [screen](../master/Documentation/Screen) (Figure 4), using the [LabVIEW PID module](http://www.ni.com/tutorial/6931/en/) to control the position of the axis of the servomotor to which a bar is attached.
