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
    
    multichannel = ["CH1", "CH2", "CH3", "CH4"]

    description =   """
                        Agilent N6705A
                        DC power analyzer
                    """

    def __init__(self):

        EmptyDevice.__init__(self)

        # remains here for compatibility with v1.5.3
        self.multichannel = ["CH1", "CH2", "CH3", "CH4"]

        self.port_manager = True
        self.port_types = ["TCPIP", "GPIB"]
        
        self.FREQUENCY = "Frequency in Hz"
        self.PERIOD = "Period in s"
        self.OFFSET = "Offset in V"
        self.AMPLITUDE = "Amplitude in V"
        self.STARTTIME = "Start time in s"
        self.STARTLEVEL = "Start level in V"
        self.ENDTIME = "End time in s"
        self.ENDLEVEL = "End level in V"
        self.RISETIME = "RiseTime"
        self.FALLTIME = "FallTime"
        self.NSTEPS = "Number of steps"
        self.PULSEWIDTH = "Pulse width in s"
        self.TCONSTANT = "Time constant"
        
        self.waveforms = dict()
        # Sine
        self.waveforms['Sine'] = dict()
        self.waveforms['Sine']['label'] = "SIN"
        self.waveforms['Sine'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Sine'][self.PERIOD] = dict({"command": "FREQ", "unit": "s"})
        self.waveforms['Sine'][self.OFFSET] = dict({"command": "OFFSET", "unit": "V"})
        self.waveforms['Sine'][self.AMPLITUDE] = dict({"command": "AMPL", "unit": "V"})
        # Step
        self.waveforms['Step'] = dict()
        self.waveforms['Step']['label'] = "STEP"
        self.waveforms['Step'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        self.waveforms['Step'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        self.waveforms['Step'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})
        # Ramp
        self.waveforms['Ramp'] = dict()
        self.waveforms['Ramp']['label'] = "RAMP"
        self.waveforms['Ramp'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        self.waveforms['Ramp'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        self.waveforms['Ramp'][self.RISETIME] = dict({"command": "RTIME", "unit": "s"})
        self.waveforms['Ramp'][self.ENDTIME] = dict({"command": "END:TIME", "unit": "s"})
        self.waveforms['Ramp'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})
        # Staircase
        self.waveforms['Staircase'] = dict()
        self.waveforms['Staircase']['label'] = "STAIRCASE"
        self.waveforms['Staircase'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        self.waveforms['Staircase'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        self.waveforms['Staircase'][self.RISETIME] = dict({"command": "TIME", "unit": "s"})
        self.waveforms['Staircase'][self.NSTEPS] = dict({"command": "NSTEPS", "unit": "num"})
        self.waveforms['Staircase'][self.ENDTIME] = dict({"command": "END:TIME", "unit": "s"})
        self.waveforms['Staircase'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})
        # Pulse
        #self.waveforms['Pulse'] = dict()
        #self.waveforms['Pulse']['label'] = "PULSE"
        #self.waveforms['Pulse'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        #self.waveforms['Pulse'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        #self.waveforms['Pulse'][self.xxx] = dict({"command": "TOP:TIME", "unit": "s"})
        #self.waveforms['Pulse'][self.xxx] = dict({"command": "TOP:LEVEL", "unit": "V"})
        #self.waveforms['Pulse'][self.ENDTIME] = dict({"command": "END:TIME", "unit": "s"})
        #self.waveforms['Pulse'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})
        # Trapezoid
        #self.waveforms['Trapezoid'] = dict()
        #self.waveforms['Trapezoid']['label'] = "TRAPEZOID"
        #self.waveforms['Trapezoid'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        #self.waveforms['Trapezoid'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        #self.waveforms['Trapezoid'][self.RISETIME] = dict({"command": "RTIME", "unit": "s"})
        #self.waveforms['Trapezoid'][self.xxx] = dict({"command": "TOP:TIME", "unit": "s"})
        #self.waveforms['Trapezoid'][self.xxx] = dict({"command": "TOP:LEVEL", "unit": "V"})
        #self.waveforms['Trapezoid'][self.FALLTIME] = dict({"command": "FTIME", "unit": "s"})
        #self.waveforms['Trapezoid'][self.ENDTIME] = dict({"command": "END:TIME", "unit": "s"})
        #self.waveforms['Trapezoid'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})
        # Exponential
        self.waveforms['Exponential'] = dict()
        self.waveforms['Exponential']['label'] = "EXP"
        self.waveforms['Exponential'][self.STARTTIME] = dict({"command": "START:TIME", "unit": "s"})
        self.waveforms['Exponential'][self.STARTLEVEL] = dict({"command": "START:LEVEL", "unit": "V"})
        self.waveforms['Exponential'][self.RISETIME] = dict({"command": "TIME", "unit": "s"})
        self.waveforms['Exponential'][self.TCONSTANT] = dict({"command": "TCONSTANT", "unit": "s"})
        self.waveforms['Exponential'][self.ENDLEVEL] = dict({"command": "END:LEVEL", "unit": "V"})

    def set_GUIparameter(self):
        GUIparameter = {
            "SweepMode": [self.FREQUENCY, self.PERIOD, self.OFFSET, self.AMPLITUDE, self.STARTTIME, self.STARTLEVEL, self.ENDTIME, self.ENDLEVEL, \
                self.RISETIME, self.FALLTIME, self.NSTEPS, self.PULSEWIDTH, self.TCONSTANT, "None"],
            "Waveform": list(self.waveforms.keys()),
            "PeriodFrequency": [self.STARTTIME, self.FREQUENCY, self.PERIOD],
            "AmplitudeHiLevel": [self.ENDLEVEL, self.AMPLITUDE],
            "OffsetLoLevel": [self.STARTLEVEL, self.OFFSET],
            "DelayPhase": [self.NSTEPS, self.TCONSTANT],
            "DutyCyclePulseWidth": [self.ENDTIME, self.PULSEWIDTH],
            "PeriodFrequencyValue": 2,
            "AmplitudeHiLevelValue": 1.0,
            "OffsetLoLevelValue": 0.0,
            "DelayPhaseValue": 10,
            "DutyCyclePulseWidthValue": 5,
            self.RISETIME: 1,
            self.FALLTIME: 1
        }

        return GUIparameter

    def get_GUIparameter(self, parameter={}):
        self.sweep_mode = parameter['SweepMode'] 
        self.waveform = parameter['Waveform']
        
        self.periodfrequency          = parameter['PeriodFrequency' ]
        self.periodfrequencyvalue     = float(parameter['PeriodFrequencyValue'])
        self.amplitudehilevel         = parameter['AmplitudeHiLevel']
        self.amplitudehilevelvalue    = float(parameter['AmplitudeHiLevelValue'])
        self.offsetlolevel            = parameter['OffsetLoLevel']
        self.offsetlolevelvalue       = float(parameter['OffsetLoLevelValue'])
        self.delayphase               = parameter['DelayPhase']
        self.delayphasevalue          = float(parameter['DelayPhaseValue'])
        self.dutycyclepulsewidth      = parameter['DutyCyclePulseWidth']
        self.dutycyclepulsewidthvalue = float(parameter['DutyCyclePulseWidthValue'])
        self.risetime                 = float(parameter['RiseTime'])
        self.falltime                 = float(parameter['FallTime'])

        self.device = parameter['Device']
        self.channel = self.device[-1]
        self.shortname = "AgilentN6705A CH" + self.channel
        
        if self.sweep_mode == 'None':
            self.variables =[]
            self.units =    []
            self.plottype = []     # True to plot data
            self.savetype = []     # True to save data
        else:
            index_to_split_unit = self.sweep_mode.rfind(" ")
            self.variables = [self.sweep_mode[:index_to_split_unit]]
            self.units =     [self.waveforms[self.waveform][self.sweep_mode]['unit']]
            self.plottype =  [True]     # True to plot data
            self.savetype =  [True]     # True to save data
        
    def initialize(self):
        self.port.port.read_termination = '\n'
        self.port.port.write_termination = '\n'
        # once at the beginning of the measurement
        self.port.write("*RST")

    def deinitialize(self):
        pass

    def poweron(self):
        # TODO: include current operation mode
        self.port.write(f"VOLT:MODE ARB, (@{self.channel})")
        self.port.write(f"ARB:FUNC:TYPE VOLT, (@{self.channel})")
        self.port.write(f"ARB:FUNC:SHAPE {self.waveforms[self.waveform]['label']}, (@{self.channel})")
        # TODO: number of signal repetitions
        self.port.write(f"ARB:COUNT INF, (@{self.channel})")
        self.port.write(f"TRIG:ARB:SOURCE IMM")
        self.port.write(f"OUTP ON, (@{self.channel})")
        self.port.write(f"INIT:TRAN (@{self.channel})")

    def poweroff(self):
        self.port.write(f"OUTP OFF, (@{self.channel})")
        self.port.write(f"ABORT:TRAN (@{self.channel})")
        
    def set_parameter(self, param, value):
        arb_prefix = f"ARB:VOLTAGE:{self.waveforms[self.waveform]['label']}"
        # handle period value
        if param == self.PERIOD:
            value = 1/value
        if self.waveforms[self.waveform].get(param, False):
            self.port.write(f"{arb_prefix}:{self.waveforms[self.waveform][param]['command']} {value}, (@{self.channel}); *WAI")
            return True
        else: return False
            
    def configure(self):
        self.set_parameter(self.periodfrequency, self.periodfrequencyvalue)
        self.set_parameter(self.amplitudehilevel, self.amplitudehilevelvalue)
        self.set_parameter(self.offsetlolevel, self.offsetlolevelvalue)
        self.set_parameter(self.dutycyclepulsewidth, self.dutycyclepulsewidthvalue)
        self.set_parameter(self.delayphase, self.delayphasevalue)
        self.set_parameter('RiseTime', self.risetime)
        self.set_parameter('FallTime', self.falltime)

    def apply(self):
        if self.sweep_mode == 'None':
            pass
        else:
            self.port.write(f"ABORT:TRAN (@{self.channel}); *WAI")  # wait for pending abort                       
            if self.set_parameter(self.sweep_mode, self.value) is False:
                raise Exception(f"Sweep on {self.sweep_mode} is not supported for {self.waveform}")
            self.port.write(f"INIT:TRAN (@{self.channel})")

    def trigger(self):
        pass

    def measure(self):
        if self.sweep_mode != 'None':
            arb_prefix = f"ARB:VOLTAGE:{self.waveforms[self.waveform]['label']}"
            self.port.write(f"{arb_prefix}:{self.waveforms[self.waveform][self.sweep_mode]['command']}? (@{self.channel})")
        
    def call(self):
        if self.sweep_mode == 'None':
            return []
        else:
            returnvalue = float(self.port.read())
            # handle period value
            if self.sweep_mode == self.PERIOD:
                returnvalue = 1/returnvalue
            return [returnvalue]