from pathlib import Path
import configparser
from logging import getLogger as get_logger


def write_config(conf_obj, conf_path):
    with open(conf_path, 'w') as fp:
        conf_obj.write(fp)




class AdaHubConfig(object):

    def read_from_disk(self):
        log_name = f'{self.log_name}.read_from_disk'
        log = get_logger(log_name)
        log.debug(f'Logger started for {log_name}')
        log.debug(f'Received call to read config file from disk: {self.config_file_path}')

        config = configparser.ConfigParser()
        config.read(self.config_file_path)
        log.debug(f'Found config file with these sections: {config.sections()}')

        return config

    def build_default(self):

        conf = configparser.ConfigParser()
        conf['RUNTIME'] = {
                'conf_file_path': self.config_file_path,
                'data_root_path': self.default_data_root,
                'run_dir_path': str(self.default_data_root + 'run/')
                }

        return conf

    def __init__(self, path_to_config=None):
        # Import directly
        import os

        # From * standard library imports
        from pathlib import Path
        from logging import getLogger as get_logger

        # From * local imports
        from ada_hub.lib.constants import PROG, DEFAULT_CONF_FILE_PATH, DEFAULT_DATA_ROOT, DEFAULT_CONF_ROOT
        self.default_data_root = DEFAULT_DATA_ROOT

        # Start a logger
        self.log_name = f'{PROG}.AdaHubConfig'
        log = get_logger(self.log_name)

        log.debug('Started Logger for AdaHubConfig')
        log.debug('Initializing class')

        # Determine and (if log levels permit) announce the default configuration file path
        self.default_conf_file_path = DEFAULT_CONF_FILE_PATH
        log.debug(f'The default config file location is {self.default_conf_file_path}')

        # Check to see if a value for the path_to_config parameter was provided; if so we'll use that instead of the
        # default path found in the constants file.
        log.debug('Checking for non-default path to config...')

        if path_to_config is not None:
            log.debug(f'A custom config path was provided: {path_to_config}')
            config_path = Path(path_to_config)
        else:
            log.debug(f'No custom config filepath provided, falling back on default filepath: {self.default_conf_file_path}')
            config_path = Path(self.default_conf_file_path)

        # Finally, set this path as an attribute of the AdaHubConfig class
        self.config_file_path = config_path

        self.conf_root = self.config_file_path.parent

        if not Path(self.conf_root).exists():
            log.warning(f'Config root not present on system {self.conf_root}')
            os.makedirs(Path(self.conf_root))
            log.info('Directory written!')
        else:
            if Path(self.config_file_path).exists():
                log.debug('Found config file')
                self.config = self.read_from_disk()

            else:
                log.debug('Did not find specified config file. Creating...')
                config_struct = self.build_default()
                write_config(config_struct, config_struct['RUNTIME']['conf_file_path'])
                with open(config_struct['RUNTIME']['conf_file_path'], 'w') as fp:
                    config_struct.write(fp)
                    log.debug('Written')
                self.config = config_struct

            log.debug(f'Sections in config: {self.config.sections()}')


