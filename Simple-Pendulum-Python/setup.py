from setuptools import setup

setup(
    name='Simple Pendulum - Python',
    version='1.1',
    install_requires=['nifpga'],
    packages=['Calibration', 'ProofSignals'],
    url="https://github.com/nightcomnit/PositionControl-SimplePendulum",
    license='MIT',
    author='Alan Sandoval Leon; Ana Isabel Gutierrez Chavez; José Carlos López Arriaga',
    author_email='nightcomnit@gmail.com',
    description='Implementation of two libraries to calibrate and apply test signals to a simple pendulum, previously '
                'programmed in LabVIEW with FPGA.'
)
