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
# Type: SMU
# Device: Keysight N6705

import numpy as np
from collections import OrderedDict
from EmptyDeviceClass import EmptyDevice
from ErrorMessage import debug


class Device(EmptyDevice):

    description = """
                        Agilent N6705A
                        DC power analyzer
                        
                        Agilent N7605A can be equipped with different modules/options that enable different features.
                        
                        - N678x modules:
                            - voltage compliance is monitored sensing 4-wire terminals
                            
                        - Opt 1A option:
                            - 100 uA measurement range
                            
                        - Opt 2A option:
                            - 200 uA measurement range
                    """

    multichannel = ["CH1", "CH2", "CH3", "CH4"]

    def __init__(self):

        EmptyDevice.__init__(self)

        self.shortname = "Agilent N6705A"

        # remains here for compatibility with v1.5.3
        self.multichannel = ["CH1", "CH2", "CH3", "CH4"]

        self.variables = ["Voltage", "Current", "OVP", "OCP"]
        self.units = ["V", "A", "", ""]
        self.plottype = [True, True, True, True]  # True to plot data
        self.savetype = [True, True, True, True]  # True to save data

        self.port_manager = True
        self.port_types = ["TCPIP", "GPIB"]

        self.channel_model = None

        self.commands = {
            "Voltage [V]": "VOLT",
            "Current [A]": "CURR",
        }

        # voltage autorange supported only by N678x
        self.voltage_ranges = OrderedDict([
            ("51V", "51"),
            ("5.5V", "5.5")
        ])

        # current autorange supported only by N678x
        self.current_ranges = OrderedDict([
            ("3.06A", "3.06"),
            ("100 mA", "0.1"),
            ("200 uA", "0.0002"),
            ("100 uA", "0.0001")
        ])

    def set_GUIparameter(self):
        GUIparameter = {
            "SweepMode": ["Voltage [V]", "Current [A]"],
            "Range": list(self.current_ranges.keys()),
            "RangeVoltage": list(self.voltage_ranges.keys()),
            "Compliance": 100e-6,
            "4wire": False,
            "Speed": ["Medium", "Fast", "Slow"],
            "CheckPulse": False,
            "PulseOnTime": 0.5,
            "PulseOffTime": 0.5,
            "PulseOffLevel": 0.0,
        }

        return GUIparameter

    def get_GUIparameter(self, parameter={}):
        self.source = parameter['SweepMode']
        self.protection = parameter['Compliance']
        self.vrange = self.voltage_ranges[parameter["RangeVoltage"]]
        self.irange = self.current_ranges[parameter["Range"]]
        self.four_wires = parameter["4wire"]
        self.speed = parameter["Speed"]

        self.pulse = parameter['CheckPulse']  
        self.ton = float(parameter["PulseOnTime"])
        self.toff = float(parameter["PulseOffTime"])
        self.pulseofflevel = parameter['PulseOffLevel']

        self.device = parameter['Device']
        self.channel = self.device[-1]

    def initialize(self):
        self.port.port.read_termination = '\n'
        self.port.port.write_termination = '\n'
        # once at the beginning of the measurement
        self.port.write("*RST")

    def configure(self):

        self.port.write(f"SYST:CHAN:MODEL? (@{self.channel})")
        self.channel_model = self.port.read()

        if self.source == "Voltage [V]":
            # 4 wires
            if self.four_wires:
                self.port.write(f"VOLT:SENSE:SOURCE EXT, (@{self.channel})")
            else:
                self.port.write(f"VOLT:SENSE:SOURCE INT, (@{self.channel})")
            # sourcemode fix
            self.port.write(f"VOLT:MODE FIX, (@{self.channel})")
            #
            # voltage protection (OVP) level
            # VOLT:PROT value, (@ch)
            #
            # compliance
            if self.channel_model.startswith('N678'):
                self.port.write(
                    f"CURR:LIMIT {self.protection}, (@{self.channel})")
            else:
                self.port.write(f"CURR {self.protection}, (@{self.channel})")
                self.port.write(f"CURR:PROT:STAT ON, (@{self.channel})")
            # pulse
            if self.pulse == True:
                self.pulsemode = "VOLTAGE"

        if self.source == "Current [A]":
            # sourcemode fix
            self.port.write(f"CURR:MODE FIX, (@{self.channel})")
            #
            # current protection (OCP) level
            # CURR:LIMIT value, (@ch)   (N678x)
            # CURR value, (@ch)         (other)
            # CURR:PROT:STAT ON, (@ch)
            #
            # compliance
            if self.channel_model.startswith('N678'):
                self.port.write(
                    f"VOLT:PROT:REMOTE {self.protection}, (@{self.channel})")
            else:
                self.port.write(
                    f"VOLT:PROT {self.protection}, (@{self.channel})")
            # pulse
            if self.pulse == True:
                self.pulsemode = "CURRENT"

        # pulse
        if self.pulse == True:
            self.port.write(f"{self.pulsemode}:MODE ARB, (@{self.channel})")
            self.port.write(f"ARB:FUNC:SHAPE PULSE, (@{self.channel})")
            self.port.write(f"ARB:FUNC:TYPE {self.pulsemode}, (@{self.channel})")
            self.port.write(f"ARB:COUNT INF, (@{self.channel})")

        self.port.write(f"SENSE:VOLT:RANGE {self.vrange}, (@{self.channel})")
        self.port.write(f"SENSE:CURR:RANGE {self.irange}, (@{self.channel})")
        

        self.npoints = 3906;        # 50 Hz power line  (= medium)
        #self.npoints = 3255;        # 60 Hz power line (= medium)

        if self.speed == "Fast":
            # 0.1 NPLC
            self.npoints = int(self.npoints/10)
        elif self.speed == "Slow":
            # 10 NPLC
            self.npoints *= 10

        self.port.write(f"SENSE:SWEEP:POINTS {self.npoints}, (@{self.channel})")

    def poweron(self):
        if self.pulse == True:
            self.port.write(f"ARB:COUNT INF, (@{self.channel})")
            self.port.write(f"TRIG:ARB:SOURCE IMM")
            self.port.write(f"OUTP ON, (@{self.channel})")
            self.port.write(f"INIT:TRAN (@{self.channel})")
        else:
            self.port.write(f"OUTP ON, (@{self.channel})")

    def poweroff(self):
        self.port.write(f"OUTP OFF, (@{self.channel})")
        if self.pulse == True:
            self.port.write(f"ABORT:TRAN (@{self.channel})")

    def apply(self):
        # pulse
        if self.pulse == True:
            self.port.write(f"ABORT:TRAN (@{self.channel}); *WAI")  # wait for pending abort                       
            self.port.write(f"ARB:{self.pulsemode}:PULSE:START:TIME {float(self.toff/2)}, (@{self.channel})")
            self.port.write(f"ARB:{self.pulsemode}:PULSE:START:LEVEL {self.pulseofflevel}, (@{self.channel})")
            self.port.write(f"ARB:{self.pulsemode}:PULSE:TOP:TIME {self.ton}, (@{self.channel})")
            self.port.write(f"ARB:{self.pulsemode}:PULSE:TOP:LEVEL {self.value}, (@{self.channel})")
            self.port.write(f"ARB:{self.pulsemode}:PULSE:END:TIME {float(self.toff)/2}, (@{self.channel})")
            self.port.write(f"INIT:TRAN (@{self.channel})")
        else:
            self.port.write(f"{self.commands[self.source]} {self.value}, (@{self.channel})")

    def call(self):
        self.port.write(f"MEAS:VOLT? (@{self.channel})")
        voltage = float(self.port.read())

        # modules N6761A and N6762A have simultaneous V/I measurement
        if self.channel_model.startswith('N676'):
            self.port.write(f"FETCH:CURR? (@{self.channel})")
        else:
            self.port.write(f"MEAS:CURR? (@{self.channel})")

        current = float(self.port.read())

        # check questionable status condition register
        self.port.write(f"STAT:QUES:COND? (@{self.channel})")
        regvalue = int(self.port.read())
        
        return [voltage, current, bool(regvalue & (1)), bool(regvalue & (1<<1))]
