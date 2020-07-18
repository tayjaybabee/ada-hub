from ada_hub.lib.constants import PROG
from ada_hub.lib.helpers.system import gui_capable
from ada_hub.lib.helpers.debug import format_members
from ada_hub.lib.config import write_config
from ada_hub.lib.config.defaults import sense_conf, sense_device as sense_device_conf

# Import exceptions
from ada_hub.lib.ada_sense.errors import InvalidTempScaleError

from logging import getLogger


VALID_TEMP_SCALES = [
        'c',
        'celsius',
        'f',
        'fahrenheit',
        'k',
        ]
""" The strings that will be accepted by the program as valid temp scales to check against when assigning/changing 
the respective option. """


class AdaSense(object):
    """

    A class that handles interaction between the APP and the Sense device.

    """


    def add_to_config(self):
        """

        A function that adds the SENSE and SENSE_DEVICE sections to the config file. Should be rare to use this as
        the config class should have created these sections already.

        Returns:
            ConfigParser object modified.

        """

        log_name = str(f'{self.log_name}.add_to_config')
        log = getLogger(log_name)
        debug = log.debug
        debug(f'Logger started for {log_name}')

        debug('Received call to add sections to config for AdaSense.')

        debug('Gathering the default SENSE section & reading it into the config file')
        self.config.read_dict(sense_conf())
        debug(f'Section, added. Config sections are now: {"".join(self.config.sections())}')

        debug('Gathering the SENSE_DEVICE section and reading it into the config file.')
        self.config.read_dict(sense_device_conf())
        debug(f'Section, added. Config sections are now: {"".join(self.config.sections())}')

        debug('Returning config device to caller')
        return self.config


    def check_scale(self, alt_scale=None):
        """

        Checks the configured temperature scale found in self.temp_scale for validity.

        Returns:
            bool: Will return True if successful

        """

        # Define a logger name, and start it. Then announce that we started it.
        log_name = str(f'{self.log_name}.check_scale')
        log = getLogger(log_name)
        log.debug(f'Started logger for {log_name}')
        log.debug(f'Received request to check the configured temperature units for validity')
        log.debug(f'Current configured temperature unit is: {self.temp_scale}')

        if alt_scale is not None:
            log.debug('Received argument for alt_scale, checking that instead of current configuration')
            if alt_scale not in VALID_TEMP_SCALES:
                raise InvalidTempScaleError()
            else:
                return True

        # If the configured temperature unit is not found in the list of valid temperature scales raise an
        # InvalidTempScaleError exception, otherwise; just return True
        if self.temp_scale not in VALID_TEMP_SCALES:
            raise InvalidTempScaleError()
        else:
            return True


    def change_temp_scale(self, new_scale):
        """

        Change the scale that temperature results will be delivered in moving forward.

        Call on this function to change the scale that temperature results are delivered in, going forward. Part of
        the processes run by this function are to check the string provided by the `new_scale` parameter of this
        function.

        Args:
            new_scale ():

        Returns:
            None

        """

        log_name = str(self.log_name + '.change_temp_scale')
        log = getLogger(log_name)

        log.debug(f'Started logger for {log_name}')
        log.debug(f'Received request to change temp scale from {self.temp_scale} to {new_scale}')

        if self.temp_scale == new_scale:
            log.warn('These are the same values!')
            return

        try:
            self.check_scale(new_scale)
            self.config[ 'SENSE' ][ 'temp_scale' ] = new_scale
            self.temp_scale = new_scale
            write_config(self.config)
        except InvalidTempScaleError as e:
            log.warning(e.message)


    def load_sense(self, emulate=False):
        """

        Load the Sense device interface

        Args:
            emulate (bool): Should the Sense emulator be loaded? True for yes, False for no (default)

        Returns:

        """
        log = getLogger(f'{PROG}.load_sense')
        log.debug('Received request to load AdaSense and it\'s drivers...')

        log.debug('Attempting to load the SenseHat...')

        if not emulate:
            log.debug('Did not receive emulate flag, attempting to load live hardware...')
            try:
                from sense_hat import SenseHat

                log.debug('SenseHat loaded. Not Emulated.')
            except ModuleNotFoundError as e:
                log.warning('Received exception while attempting to load the Sense hardware')
                if 'RTIMU' in e.__str__():
                    log.error('No SenseHat hardware detected. Attempting load again, but with emulator.')
                    self.load_sense(emulate=True)
        else:
            if not gui_capable():
                log.error('This operating system does not have a GUI. The Sense Hat emulator will not initialize '
                          'given such conditions.')
            try:
                from sense_emu import SenseHat

                log.debug('SenseHat loaded. Emulated.')
                log.info('SenseHat Emulator Loaded. Performing test probe to ensure reliable emulator initialization '
                         'occurred.')
                temp_sense = SenseHat()
                sense_temp = temp_sense.temperature

                log.debug(f'Probe test successful! If you\'re curious, we received {sense_temp} as a result. '
                          f'Discarding reading.')

                sense_temp = None

            except OSError as e:
                log.error('Unable to load SenseHat emulator. This is not recoverable as the emulator is only ever '
                          'called explicitly or if loading the hardware failed first.')
                raise

            # Since we've now determined exactly which Sense Hat library we'll use; let's go ahead and initialize
            # that class while we store it in an attribute
            self.sense = SenseHat()



    def get_humidity(self):
        """

        Query the humidity sensor and receive the relative humidity

        Returns:
            str: A string containing the result
        """

        log = getLogger(f'{PROG}.AdaSense.get_humidity')
        log.debug('Received request to fetch relative humidity.')

        hum = round(self.sense.humidity)
        f_hum = str(hum) + "%"

        return f_hum


    def get_temp(self):
        """

        Get the current ambient temperature according to the humidity sensor

        Returns:
            float: The current temperature in celsius, rounded to two decimal places.

        """
        from ada_hub.lib.ada_sense.helpers.converters import c_to_f

        log = getLogger(f'{PROG}.AdaSense.get_temp')
        log.debug('Received request to fetch ambient temperature.')

        temp = self.sense.temperature
        temp = round(temp, 2)

        if self.temp_scale == 'f' or self.temp_scale == 'fahrenheit':
            temp = c_to_f(temp)

        return temp


    def get_pressure(self):
        """

        Query the sense hat for barometric pressure data.

        Returns:
            str: The barometric pressure in millibars

        """

        # Start a logger for debugging
        log_name = str(f'{PROG}.AdaSense.get_pressure')
        log = getLogger(log_name)

        # If we're running in the verbose mode we'll go ahead and announce that we've started the logger and that
        # we're querying the sensor
        log.debug(f'Started logger for {log_name}')
        log.debug('Received request to fetch barometric pressure.')
        log.debug('Querying sensor...')

        # Query the sensor and load the results into a variable
        pres = self.sense.pressure

        # Announce that our sensor query was successful and that we're going to return it to the caller
        log.debug(f'Received {pres} for pressure sensor value. Rounding and appending unit...')

        pres = round(pres)
        pres = str(str(pres) + 'mbar')

        log.debug(f'Returning rounded and formatted pressure reading ({pres}) to caller.')

        # Return formatted and rounded result to the caller
        return pres


    def __init__(self, config):

        self.log_name = str(f'{PROG}.AdaSense')
        """ str: The name of the logger for this class """

        log = getLogger(self.log_name)
        log.debug(f'Started logger for {self.log_name}')

        log.debug(f'Initializing class.')

        log.debug('Attempting to load configuration from the config object received.')
        self.config = config
        """ The config object as passed to this class. """

        # If we're not able to find the 'SENSE' section in the config file, we should go ahead and
        # create one, add it, and fill it with defaults.
        if 'SENSE' not in config.sections():
            self.config = self.add_to_config()
        log.debug(f'Setting up attributes.')

        self.temp_scale = self.config[ 'SENSE' ][ 'temp_scale' ]

        try:
            self.check_scale()
        except InvalidTempScaleError as e:
            log.error(e.message)
            log.info('Falling back to using celsius as our temperature scale.')
            self.change_temp_scale('celsius')

        # Define an attribute named 'sense' with a value of None type. This is to be filled later
        self.sense = None
        """ An instance of SenseHat() 

                    This is either going to be one of two objects:

                        :class:`sense_hat.SenseHat()`
                            This will be returned when the program detects that it is connected to a Sense Hat and 
                            all the 
                            proper packages are installed. This will be the most often initialized class given that the 
                            application will most-often be used in a production environment.

                        :class:`sense_emu.SenseHat()`
                            If the program was explicitly instructed to (using the '--emulate' flag) or, 
                            if the program has had
                            an issue connecting to/finding the actual Sense Hat hardware it will start Sense Emu 
                            which is 
                            SenseHat emulation software to assist in testing and development

                    Note:

                        You can ensure the emulator always/never starts by manipulating the respective option in the 
                        config file! 

                    """

        # Let's go ahead and fill that attribute by running the 'load_sense' function of this class
        self.load_sense()


m_log = getLogger(PROG)

m_log.debug('Imported! (ada_hub.lib.ada_sense.__init__)')
m_log.debug(f'Members introduced with import: {format_members(dir(), False)}')
