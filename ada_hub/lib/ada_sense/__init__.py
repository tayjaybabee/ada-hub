from ada_hub.lib.constants import PROG
from ada_hub.lib.helpers.system import gui_capable
from ada_hub.lib.helpers.debug import format_members
from ada_hub.lib.config import write_config

from logging import getLogger


class AdaSense(object):

    def set_temp_units(self, new_val):
        log = getLogger(f'{PROG}.AdaSense.set_temp_units')
        log.debug(f'Received request to change configured default temp reading units to {new_val}')

    def load_sense(self, emulate=False):
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
            # that class while we store
            self.sense = SenseHat()

    @staticmethod
    def add_default_settings(config):
        conf_section = 'ADA_SENSE_SETTINGS'

        log = getLogger(f'{PROG}.AdaSense.add_default_settings')
        log.debug(f'Logger started for {__name__}')

        log.debug('Received request to build default')


        # Add the section
        config.add_section(conf_section)
        log.debug(f'Created config section. The sections contained within the configuration are now as follows: '
                  f'{config.sections()}')

        sense_config = config[conf_section]

        # Fill our new section with some default values.
        config.set(conf_section, 'always_emulate', 'False')
        log.debug(f'Always Emulate: {sense_config["always_emulate"]}')

        config.set(conf_section, 'never_emulate', 'False')
        log.debug(f'Never Emulate: {sense_config[ "never_emulate" ]}')

        config.set(conf_section, 'temp_units', 'c')
        log.debug(f'Temperature Units: {sense_config["temp_units"]}')

        config.set(conf_section, 'always_auto_refresh', 'False')
        log.debug(f'Always auto-refresh readings: {sense_config["always_auto_refresh"]}')

        log.debug('Finished assembling Sense configuration. Writing to disk...')
        write_config(config, config['RUNTIME']['conf_file_path'])
        log.debug('Returned from writing configuration to disk.')

        return config

    def get_humidity(self):
        pass

    def get_temp(self):
        pass

    def convert_temp_to_f(self):
        pass

    def __init__(self, config, emulate=False, temp_units=None):

        log_name = str(f'{PROG}.AdaSense')
        log = getLogger(log_name)
        log.debug(f'Started logger for {log_name}')

        log.debug(f'Initializing class.')

        log.debug('Attempting to load configuration from the config object received.')

        # If we're not able to find the 'ADA_SENSE_SETTINGS' section in the config file, we should go ahead and
        # create one, add it, and fill it with defaults.
        if 'ADA_SENSE_SETTINGS' not in config.sections():
            self.config = self. add_default_settings()

        log.debug(f'Setting up attributes.')

        # Declare some attributes with default values

        # Declare an attribute containing a list of acceptable temperature reading scales. This will be useful to
        # validate against later if/when we receive a request to read back ambient temperature
        self.valid_temp_scales = [
                'c',
                'celsius',
                'f',
                'fahrenheit',
                'k',
                'kelvin'
                ]
        log.debug(f'Set up the following list of acceptable values for the units the temperature is read in: '
                  f'{",".join(self.valid_temp_scales)}')

        # If the caller provided a value for the temp_units parameter we check to make sure that what we were given
        # matches an item on our list of valid temperature units (or 'valid_temp_scales').
        if temp_units is not None:
            if temp_units.lower() in self.valid_temp_scales:
                log.debug('The "temp_units" parameter contains a valid option, using this for this session.')
                self.temp_units = temp_units.capitalize()
                log.debug(f'Attribute set to {self.temp_units}')

            else:

                # If we were unable to find an item in our list of valid temperature reading scales we warn the user
                # and then fall back on the configuration object which (at the very least) should be loaded and
                # assigned by this point
                log.warning('Caller passed a value to the "temp_units" parameter, but it was invalid. falling back on'
                            ' value specified by the configuration file.')
                self.temp_units = config['ADA_SENSE_SETTINGS']['temp_units']

        else:

            # If the caller did not provide a value for the 'temp_units' parameter we fall-back to fetching this
            # value from the configuration object.
            log.debug('No temperature unit specified in call. Falling back to configuration value')
            self.temp_units = config['ADA_SENSE_SETTINGS']['temp_units']

        # Report the final setting for temperature units.
        log.debug(f'Set the temperature units to {self.temp_units}.')

        # Define an attribute named 'sense' with a value of None type. This is to be filled later
        self.sense = None

        # Let's go ahead and fill that attribute by running the 'load_sense' function of this class
        self.load_sense(emulate=emulate)


m_log = getLogger(PROG)

m_log.debug('Imported! (ada_hub.lib.ada_sense.__init__)')
m_log.debug(f'Members introduced with import: {format_members(dir(), False)}')
