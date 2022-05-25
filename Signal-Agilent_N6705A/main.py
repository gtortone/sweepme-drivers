# This Device Class is published under the terms of the MIT License.
# Required Third Party Libraries, which are included in the Device Class
# package for convenience purposes, may have a different license. You can
# find those in the corresponding folders or contact the maintainer.
#
# MIT License
# 
# Copyright (c) 2022 Gennaro Tortone (gtortone@gmail.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# SweepMe! device class
# Type: Signal
# Device: Agilent N6705A

from EmptyDeviceClass import EmptyDevice
from ErrorMessage import debug

class Device(EmptyDevice):
    
    description =   """
                        Agilent N6705A
                        DC power analyzer
                    """

    def __init__(self):

        EmptyDevice.__init__(self)
        
        self.shortname = "Agilent N6705A"

        # remains here for compatibility with v1.5.3
        self.multichannel = ["CH1", "CH2", "CH3", "CH4"]
        
        self.idlevalue = None
        
        self.port_manager = True
        self.port_types = ["TCPIP", "GPIB"]
        
    def set_GUIparameter(self):
        GUIparameter = {
            "SweepMode": ["Voltage [V]", "Current [A]"],
            "Waveform": ["Step", "Ramp", "Staircase", "Pulse", "Trapezoid", "Exponential"],  # Sine included by default
            
        }

        return GUIparameter
        
    def get_GUIparameter(self, parameter={}):
        debug(parameter)
        self.source = parameter['SweepMode']

        self.device = parameter['Device']
        self.channel = self.device[-1]
        
    def initialize(self):
        self.port.port.read_termination = '\n'
        self.port.port.write_termination = '\n'
        # once at the beginning of the measurement
        self.port.write("*RST")
        
    def deinitialize(self):
        pass

    def poweron(self):
        self.port.write(f"OUTP ON, (@{self.channel})")

    def poweroff(self):
        self.port.write(f"OUTP OFF, (@{self.channel})")

    def apply(self):
        pass
        #self.port.write(f"{self.commands[self.source]} {self.value}, (@{self.channel})")

    def trigger(self):
        pass

    def measure(self):
        pass
    
    def call(self):
        return []