# This Device Class is published under the terms of the MIT License.
# Required Third Party Libraries, which are included in the Device Class
# package for convenience purposes, may have a different license. You can
# find those in the corresponding folders or contact the maintainer.
#
# MIT License
# 
# Copyright (c) 2018 Axel Fischer (sweep-me.net)
# Copyright (c) 2022 Gennaro Tortone (Istituto Nazionale di Fisica Nucleare - Sezione di Napoli - tortone@na.infn.it)
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
# Device: Agilent_33220A

# Relation between trigger mode and burst parameters
#
# example: 
# - period: 2s
# - signal repetitions: 3
# - burst delay: 8s 
#
# Trigger           Output
# --------------------------------------------------------------------------------
# Internal (INT)    offset/lolevel for 8s at start, loop [ 3 signal (6s), offset/lolevel (2s) ]
# External (EXT)    offset/lolevel up to trigger, @trigger: 3 signal (6s), offset/lolevel (2s) - no repetitions, no delay
# Bus	   (BUS)    signal (6s), offset/lolevel up to next sweep value (apply method)

from EmptyDeviceClass import EmptyDevice
from ErrorMessage import debug

class Device(EmptyDevice):

    def __init__(self):
    
    
        EmptyDevice.__init__(self)
        
        self.idlevalue = None
        
        self.port_manager = True
        self.port_types = ['USB', 'GPIB']
        self.port_identifications = ['Agilent Technologies,33220A']

        self.PERIOD = "Period in s"
        self.FREQUENCY = "Frequency in Hz"
        self.AMPLITUDE = "Amplitude in V"
        self.HILEVEL = "HiLevel in V"
        self.OFFSET = "Offset in V"
        self.LOLEVEL = "LoLevel in V"
        self.DUTYCYCLE = "Duty cycle in %"
        self.PULSEWIDTH = "Pulse width in s"
        self.RISETIME = "RiseTime"
        self.FALLTIME = "FallTime"
        self.NSTEPS = "NumberSteps"
        #
        self.SYMMETRY = "Ramp symmetry"     # not in GUI
        self.SAMPLES = "Waveform samples"   # not in GUI

        self.waveforms = dict()
        # Sine
        self.waveforms['Sine'] = dict()
        self.waveforms['Sine']['label'] = "SIN"
        self.waveforms['Sine'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Sine'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Sine'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        # Square
        self.waveforms['Square'] = dict()
        self.waveforms['Square']['label'] = "SQU"
        self.waveforms['Square'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Square'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Square'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        self.waveforms['Square'][self.DUTYCYCLE] = dict({"command": "FUNC:SQUARE:DCYCLE", "unit": "%"})
        # Ramp
        self.waveforms['Ramp'] = dict()
        self.waveforms['Ramp']['label'] = "RAMP"
        self.waveforms['Ramp'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Ramp'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Ramp'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        self.waveforms['Ramp'][self.SYMMETRY] = dict({"command": "FUNC:RAMP:SYMMETRY", "unit": "%"})
        # Pulse
        self.waveforms['Pulse'] = dict()
        self.waveforms['Pulse']['label'] = "PULS"
        self.waveforms['Pulse'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Pulse'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Pulse'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        self.waveforms['Pulse'][self.PULSEWIDTH] = dict({"command": "PULSE:WIDTH", "unit": "s"})
        self.waveforms['Pulse'][self.RISETIME] = dict({"command": "FUNC:PULSE:TRANS", "unit": "s"})
        # Noise
        self.waveforms['Noise'] = dict()
        self.waveforms['Noise']['label'] = "NOIS"
        self.waveforms['Noise'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Noise'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Noise'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        # DC
        self.waveforms['DC'] = dict()
        self.waveforms['DC']['label'] = "DC"
        self.waveforms['DC'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['DC'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['DC'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        # Arb
        self.waveforms['Arb'] = dict()
        self.waveforms['Arb']['label'] = "USER"
        self.waveforms['Arb'][self.FREQUENCY] = dict({"command": "FREQ", "unit": "Hz"})
        self.waveforms['Arb'][self.AMPLITUDE] = dict({"command": "VOLT", "unit": "V"})
        self.waveforms['Arb'][self.OFFSET] = dict({"command": "VOLT:OFFS", "unit": "V"})
        self.waveforms['Arb'][self.SAMPLES] = dict({"command": "DATA VOLATILE, ", "unit": "samples"})

        self.commands = {
            self.FREQUENCY: {"command": "FREQ", "unit": "Hz"},
            self.PERIOD: {"command": "FREQ", "unit": "s"}, 
            self.AMPLITUDE: {"command": "VOLT", "unit": "V"}, 
            self.OFFSET: {"command": "VOLT:OFFS", "unit": "V"}, 
            self.HILEVEL: {"command": "VOLT", "unit": "V"},  
            self.LOLEVEL: {"command": "VOLT:OFFS", "unit": "V"}, 
            self.DUTYCYCLE: {"command": "FUNC:SQUARE:DCYCLE", "unit": "%"}, 
            self.PULSEWIDTH: {"command": "PULSE:WIDTH", "unit": "s"}, 
            self.RISETIME: {"command": "FUNC:RAMP:SYMMETRY", "unit": "%"}
        }

        self.shortname = 'Agilent-33220A'
        
        self.plottype = [True] # True to plot data
        self.savetype = [True] # True to save data
        
        # These commands require Option 001, External Timebase Reference (see
        # page 258 for more information).
        # PHASe {<angle>|MINimum|MAXimum}
        # PHASe? [MINimum|MAXimum]
        # PHASe:REFerence
        # PHASe:UNLock:ERRor:STATe {OFF|ON}
        # PHASe:UNLock:ERRor:STATe?
        # UNIT:ANGLe {DEGree|RADian}
        # UNIT:ANGLe?

    def get_GUIparameter(self, parameter={}):
        self.sweep_mode                  = parameter['SweepMode'] 
        self.waveform                    = parameter['Waveform'] 
        self.periodfrequency             = parameter['PeriodFrequency']
        self.periodfrequencyvalue        = float(parameter['PeriodFrequencyValue'])
        self.amplitudehilevel            = parameter['AmplitudeHiLevel']
        self.amplitudehilevelvalue       = float(parameter['AmplitudeHiLevelValue'])
        self.offsetlolevel               = parameter['OffsetLoLevel']
        self.offsetlolevelvalue          = float(parameter['OffsetLoLevelValue'])
        self.dutycyclepulsewidth         = parameter['DutyCyclePulseWidth']
        self.dutycyclepulsewidthvalue    = float(parameter['DutyCyclePulseWidthValue'])
        self.risetime                    = float(parameter['RiseTime'])
        #self.delayphase                 = parameter['DelayPhase']
        self.impedance                   = parameter['Impedance']
        self.trigger_mode                = parameter['Trigger']
        self.waveform_file               = parameter['ArbitraryWaveformFile']
        self.burst_enabled               = parameter['BurstShowHide']
        self.burst_signals               = int(parameter['BurstSignalRepetitions'])
        self.burst_period                = float(parameter['BurstDelay'])
        
        if self.sweep_mode == 'None':
            self.variables =[]
            self.units =    []
            self.plottype = []     # True to plot data
            self.savetype = []     # True to save data       
        else:
            self.variables = [self.sweep_mode.split(" ")[0]]
            self.units = [self.commands[self.sweep_mode]['unit']]
            self.plottype = [True]     # True to plot data
            self.savetype = [True]     # True to save data   

    def set_GUIparameter(self):
        GUIparameter = {
                        "SweepMode": [self.FREQUENCY, self.PERIOD, self.AMPLITUDE, self.OFFSET, self.HILEVEL, self.LOLEVEL, self.DUTYCYCLE, self.PULSEWIDTH, self.RISETIME, "None"],
                        "Waveform": list(self.waveforms.keys()),
                        "PeriodFrequency" : [self.PERIOD, self.FREQUENCY],
                        "AmplitudeHiLevel" : [self.AMPLITUDE, self.HILEVEL],
                        "OffsetLoLevel" : [self.OFFSET, self.LOLEVEL],
                        #"DelayPhase": ["Phase [deg]", "Delay [s]"],
                        "DutyCyclePulseWidth": [self.PULSEWIDTH, self.DUTYCYCLE],
                        "PeriodFrequencyValue": 10,
                        "AmplitudeHiLevelValue": 1.0,
                        "OffsetLoLevelValue": 0.0,
                        #"DelayPhaseValue": 0,
                        "DutyCyclePulseWidthValue": 1,
                        self.RISETIME: 1,
                        "Impedance": ["High-Z", "50 Ohm"],
                        "Trigger": ["Internal", "External", "Bus"], 
                        "ArbitraryWaveformFile": "",
                        "BurstShowHide": False,
                        "BurstSignalRepetitions": 1,
                        "BurstDelay": 60,
                        #"BurstRepetitions": 1,
                        }
        return GUIparameter
        
    def initialize(self):
        self.port.write("*RST")
        # Autoranging the voltage port
        self.port.write("VOLT:RANG:AUTO ON")
        
    def configure(self):
        if self.impedance == "High-Z":
            self.port.write("OUTP:LOAD INF")
        if self.impedance == "50 Ohm":
            self.port.write("OUTP:LOAD 50")

        if self.burst_enabled:
            self.port.write("BURST:STATE ON")
            self.port.write(f"BURST:NCYCLES {self.burst_signals}")
            # burst delay > period * signal repetitions
            self.port.write(f"BURST:INTERNAL:PERIOD {self.burst_period}")

        if self.trigger_mode == "Internal":
            self.port.write("TRIG:SOURCE IMM")
        elif self.trigger_mode == "External":
            self.port.write("TRIG:SOURCE EXT")
        elif self.trigger_mode == "Bus":
            self.port.write("TRIG:SOURCE BUS")
        
        if self.waveform == 'Sine':
            self.set_sine_params()
        elif self.waveform == 'Square':
            self.set_square_params()
        elif self.waveform == 'Ramp':
            self.set_ramp_params()
        elif self.waveform == 'Pulse':
            self.set_pulse_params()
        elif self.waveform == 'Noise':
            self.set_noise_params()
        elif self.waveform == 'DC':
            self.set_dc_params()
        elif self.waveform == 'Arb':
            self.set_arb_params()
                        
    def deinitialize(self):
        self.port.write("*RST")
        self.port.write("SYST:LOC")
         
    def poweron(self):
        # arbitrary waveform FUNC must be set after data upload
        if self.waveform != 'Arb':
            self.port.write(f"FUNC {self.waveforms[self.waveform]['label']}")
        self.port.write("OUTP ON")
        
    def poweroff(self):
        self.port.write("OUTP OFF")

    def set_parameter(self, param, value):
        if self.waveforms[self.waveform].get(param, False):
            self.port.write(f"{self.waveforms[self.waveform][param]['command']} {value}; *WAI")
            return True
        else: return False
                                 
    def apply(self):
        if self.sweep_mode != 'None':
            self.update_sweep_params(self.value)                       
            # reconfigure waveform
            self.configure()
            if self.trigger_mode == "Bus":
                self.port.write("TRIG")
                       
    def measure(self):
        if self.sweep_mode != 'None':
            self.port.write("%s?" % (self.commands[self.sweep_mode]['command']))
            
    def call(self):
        if self.sweep_mode == 'None':
            return []
        else:
            self.realvalue = float(self.port.read())
            if self.sweep_mode == self.PERIOD:
                return [1/self.realvalue]
            elif self.sweep_mode == self.OFFSET:
                return [self.realvalue]
            elif self.sweep_mode == self.HILEVEL:
                return [self.amplitudehilevelvalue]
            elif self.sweep_mode == self.LOLEVEL:
                return [self.offsetlolevelvalue] 
            elif self.sweep_mode == self.RISETIME:
                return [self.realvalue]
            elif self.sweep_mode == self.DUTYCYCLE:
                return [self.realvalue]
            else: return [self.realvalue]
        
    # convenience functions

    def update_sweep_params(self, value):
        if self.sweep_mode == self.PERIOD or self.sweep_mode == self.FREQUENCY:
            self.periodfrequencyvalue = value
        elif self.sweep_mode == self.AMPLITUDE or self.sweep_mode == self.HILEVEL:
            self.amplitudehilevelvalue = value
        elif self.sweep_mode == self.OFFSET or self.sweep_mode == self.LOLEVEL:
            self.offsetlolevelvalue = value
        elif self.sweep_mode == self.DUTYCYCLE or self.sweep_mode == self.PULSEWIDTH:
            self.dutycyclepulsewidthvalue = value
        elif self.sweep_mode == self.RISETIME:
            self.risetime = value

    # SINE 

    def get_sine_params(self):
        if self.periodfrequency == self.PERIOD:
            self.frequency = 1 / self.periodfrequencyvalue
        else:
            self.frequency = self.periodfrequencyvalue

        if self.offsetlolevel == self.OFFSET:
            self.offset = self.offsetlolevelvalue
            if self.amplitudehilevel == self.AMPLITUDE:
                self.amplitude = self.amplitudehilevelvalue
            else: # self.amplitudehilevel == self.HILEVEL
                # amplitude = (hilevel - offset) * 2
                self.amplitude = (self.amplitudehilevelvalue - self.offset) * 2
        
        else: # self.offsetlolevel == self.LOLEVEL:
             if self.amplitudehilevel == self.AMPLITUDE:
                self.amplitude = self.amplitudehilevelvalue
                # offset = lolevel + amplitude/2
                self.offset = self.offsetlolevelvalue + self.amplitude/2
             else:   # self.amplitudehilevel == self.HILEVEL
                 # amplitude = hilevel - lolevel
                 self.amplitude = self.amplitudehilevelvalue - self.offsetlolevelvalue
                 # offset = lolevel + (amplitude / 2)
                 self.offset = self.offsetlolevelvalue + (self.amplitude / 2)

        return { self.FREQUENCY: self.frequency, self.AMPLITUDE: self.amplitude, self.OFFSET: self.offset, self.PERIOD: float(1/self.frequency) }

    def set_sine_params(self):
        params = self.get_sine_params()
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])

    # SQUARE

    def get_square_params(self):
        params = self.get_sine_params()
        
        if self.dutycyclepulsewidth == self.DUTYCYCLE:
            self.dcycle = self.dutycyclepulsewidthvalue
        elif self.dutycyclepulsewidth == self.PULSEWIDTH:
            # dutycycle = pulsewidth * 100 / period
            self.dcycle = self.dutycyclepulsewidthvalue * 100 / params[self.PERIOD]

        params.update({self.DUTYCYCLE: self.dcycle})

        return params

    def set_square_params(self):
        params = self.get_square_params()
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])
        self.set_parameter(self.DUTYCYCLE, params[self.DUTYCYCLE])

    # RAMP

    def get_ramp_params(self):
        params = self.get_sine_params()

        # symmetry represents the amount of time per cycle that the ramp wave is rising
        self.symmetry = float(self.risetime / params[self.PERIOD] * 100)

        params.update({self.SYMMETRY: self.symmetry})

        return params

    def set_ramp_params(self):
        params = self.get_ramp_params()
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])
        self.set_parameter(self.SYMMETRY, params[self.SYMMETRY])

    # PULSE

    def get_pulse_params(self):
        params = self.get_sine_params()

        if self.dutycyclepulsewidth == self.PULSEWIDTH:
            self.pulsewidth = self.dutycyclepulsewidthvalue
        elif self.dutycyclepulsewidth == self.DUTYCYCLE:
            # pulsewidth = dutycycle / 100 * period
            self.pulsewidth = self.dutycyclepulsewidthvalue / 100 * params[self.PERIOD]

        # edge time for rising and falling edges is 5 ns by default (max 100 ns)
        params.update({self.RISETIME: self.risetime})
        params.update({self.PULSEWIDTH: self.pulsewidth})

        return params

    def set_pulse_params(self):
        params = self.get_pulse_params()
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])
        self.set_parameter(self.PULSEWIDTH, params[self.PULSEWIDTH])
        self.set_parameter(self.RISETIME, params[self.RISETIME])

    # NOISE

    def get_noise_params(self):
        params = self.get_sine_params()

        return params

    def set_noise_params(self):
        params = self.get_noise_params()
        # default noise frequency is 10 MHz - frequency parameter has no effect
        # but must specify a value or 'DEFault'
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])

    # DC

    def get_dc_params(self):
        params = self.get_sine_params()

        return params

    def set_dc_params(self):
        params = self.get_dc_params()
        # frequency parameter has no effect but must specify a value or 'DEFault'
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        # amplitude parameter has no effect but must specify a value or 'DEFault'
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])

    # ARB

    def get_arb_params(self):
        params = self.get_sine_params()

        return params

    def set_arb_params(self):
        params = self.get_arb_params()
        self.set_parameter(self.FREQUENCY, params[self.FREQUENCY])
        self.set_parameter(self.AMPLITUDE, params[self.AMPLITUDE])
        self.set_parameter(self.OFFSET, params[self.OFFSET])

        with open(self.waveform_file, 'r') as f:
            self.set_parameter(self.SAMPLES, f.read())

        self.port.write("FUNC:USER VOLATILE")
        self.port.write(f"FUNC {self.waveforms[self.waveform]['label']}")
