from ada_hub.lib.constants import PROG
from ada_hub.lib.config import write_config


from logging import getLogger


def add_new(config):
    """

    Receives a ConfigParser object as it's positional argument and constructs a section with some default values
    to be added to the config object that it was passed.

    Args:
        config (object): This should be a ConfigParser object which we can append the section that this function
        creates to

    Returns:
        object: A ConfigParser object with our new section added

    """
    conf_section = 'ADA_SENSE_SETTINGS'

    log = getLogger(f'{PROG}.AdaSense.add_default_settings')
    log.debug(f'Logger started for {__name__}')

    log.debug('Received request to build default')

    # Add the section
    config.add_section(conf_section)
    log.debug(f'Created config section. The sections contained within the configuration are now as follows: '
              f'{config.sections()}')

    sense_config = config[ conf_section ]

    # Fill our new section with some default values.
    config.set(conf_section, 'always_emulate', 'False')
    log.debug(f'Always Emulate: {sense_config[ "always_emulate" ]}')

    config.set(conf_section, 'never_emulate', 'False')
    log.debug(f'Never Emulate: {sense_config[ "never_emulate" ]}')

    config.set(conf_section, 'temp_scale', 'c')
    log.debug(f'Temperature Units: {sense_config[ "temp_scale" ]}')

    config.set(conf_section, 'always_auto_refresh', 'False')
    log.debug(f'Always auto-refresh readings: {sense_config[ "always_auto_refresh" ]}')

    log.debug('Finished assembling Sense configuration. Writing to disk...')
    write_config(config, config[ 'RUNTIME' ][ 'conf_file_path' ])
    log.debug('Returned from writing configuration to disk.')

    return config
