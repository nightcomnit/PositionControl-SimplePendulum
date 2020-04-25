# PositionControl-SimplePendulum

Position control of a simple pendulum (One DOF) with architecture implemented in [LabVIEW FPGA](https://www.ni.com/es-mx/shop/select/labview-fpga-module) and Python through the [nifpga-python library]().

# Methodology
A servomotor, controlled by means of an h-bridge is used for the change of rotation, to which a rotary encoder was included (Figure 1). Through this the desired pendulum position is controlled, in Labview a module was implemented to read the pulses of the rotary encoder by means of an [X4 coding](http://www.ni.com/tutorial/7109/es/) and to be able to control the position of the servomotor with the help of the h-bridge.
<center>
  <figure>
    <img src="images\Rotatory encoder - servo motor.jpg?raw=true"
    alt="Figure 1"
    width="200"
    height="150">

  <figcaption>Figure 1. Namiki rotary encoder servo motor.</figcaption>
  </figure>
</center>
