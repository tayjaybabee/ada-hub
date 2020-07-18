from ada_hub.lib.constants import PROG
from ada_hub.lib.config import write_config
from ada_hub.lib.helpers.debug import format_members

from logging import getLogger
from importlib import import_module


class GUIConfig:

    @staticmethod
    def merge_default_config(prog_conf):
        """

        Take a configuration structure and add the GUI section to it, as well as some basic/default options.
        After setting the options the function will then return your modified configuration object.

        Args:
            prog_conf (object):  A ConfigParser object that has been previously loaded from the disk or assembled.

        Returns:
            object: The same config that was passed to prog_conf is returned after GUI settings are added.

        """

        # Add our section
        prog_conf.add_section('GUI')

        # Add our basic configuration structure
        prog_conf.set('GUI', 'theme', 'DarkAmber')
        prog_conf.set('GUI', 'icon_set', 'sketch')
        prog_conf.set('GUI', 'grab_anywhere', 'False')
        prog_conf.set('GUI', 'advanced_mode', 'False')

        # Return the modified configuration object
        return prog_conf

    def __init__(self, config):
        """

        Start a new instance of GUIConfig.

        Args:
            config (object): A ConfigParser object that's been previously assembled or loaded from the disk

        """

        # Grab the configuration file's path from the provided configuration object.
        conf_filepath = config['APP']['conf_file_path']

        # Start a logger with an appropriate, descriptive name
        log_name = str(f'{PROG}.GUIConfig')
        log = getLogger(log_name)

        section = 'GUI'

        # Analyze the configuration object's sections to see if 'GUI' is among them. If it's not,
        # we will send our configuration object off to "merge_default_config" to be modified appropriately.
        log.debug('Looking for "GUI" section in configuration')
        if section not in config.sections():
            log.debug('The configuration does not contain a "GUI" section. Creating!')
            config = self.merge_default_config(config)
            log.debug(f'Received the modified configuration object. With these sections: {config.sections()}')
            log.debug('Writing modified configuration to disk.')
            write_config(config, conf_filepath)
            log.debug('Config written!')

        # Go ahead and assign the config to an aptly named attribute
        self.conf = config

        log.debug(f'Initialized GUI config in the following state: {self.conf["GUI"]}')


class GUIApp(object):

    def __init__(self, config, arg_parser):
        """

        Initialize a new instance of GUIApp, load configuration for the GUI

        Args:
            config (object): ConfigParser object

        """
        from ada_hub.lib.ada_sense import AdaSense
        from ada_hub.lib.gui.models.windows.main import MainWindow
        from ada_hub import clean_exit

        log = getLogger(f'{PROG}.Application.GUI')

        log.debug('Loading main GUI application window.')
        # Instantiate an instance of MainWindow which is the main window for the AdaHub application.
        main_win = MainWindow(config)

        # Assign the new instance of MainWindow to an attribute that's appropriately named
        self.main_win = main_win.window

        # Extract the theme indicated by the configuration to an aptly named attribute
        self.theme = config['GUI']['theme']
        icon_set_str = config['GUI']['icon_set']

        # Set up a flag that will be used to indicate the running status of this window
        self.main_active = main_win.win_active

        # If this window is already active don't spawn another one
        if self.main_active:
            return

        # Switch the 'main_active' flag to True to prevent any possibility of window spawn abuse/accidents/bugs
        self.main_active = True

        # Load the sensor and LED matrices and their associated hardware and drivers.
        self.sense_hat =AdaSense(config)

        # Start a while loop (which will be our main loop) to run the 'MainWindow'
        while self.main_active:

            # Grab the event stream, and values of fields.
            # Call the 'read' function on the main window, and have it check back in 100 times a second
            event, vals = self.main_win.read(timeout=100)

            # If we receive an indication that the user pressed either the 'X' or 'Close' buttons we close the window
            # and set the 'main_active' flag to False.
            if event is None or event == 'quit_button':
                self.main_win.close()
                self.main_active = False

            # If the user presses the 'refresh all' button within the sensor reading frame, we refresh all sensor
            # fields.
            if event == 'refresh_all_button':
                log.debug('Received request to refresh all values in the Sensor info frame')

                log.debug('Updating temperature')
                self.main_win['sense_temp_out'].update(self.sense_hat.get_temp())

                log.debug('Updating pressure')
                self.main_win['sense_pres_out'].update(self.sense_hat.get_pressure())

                log.debug('Updating humidity')
                self.main_win['sense_hum_out'].update(self.sense_hat.get_humidity())

                log.debug('Refreshing window!')
                self.main_win.refresh()

            # If the user presses the refresh button in the row associated with the temperature sensor, we'll refresh
            # that reading
            if event == 'refresh_sense_temp':
                log.debug('User pressed "refresh_temp button"')

                log.debug('Updating temperature')
                self.main_win['sense_temp_out'].update(self.sense_hat.get_temp())

                log.debug('Refreshing window!')
                self.main_win.refresh()

            # If the user presses the refresh button in the row associated with the humidity sensor, we'll refresh
            # that reading
            if event == 'refresh_sense_hum':
                log.debug('User pressed button to refresh humidity reading')

                log.debug('Updating humidity')
                self.main_win['sense_hum_out'].update(self.sense_hat.get_humidity())

                log.debug('Refreshing window!')
                self.main_win.refresh()

            # If the user presses the refresh button in the row associated with the pressure sensor, we'll refresh
            # that reading
            if event == 'refresh_sense_pres':
                log.debug('User pressed button to refresh pressure reading')

                log.debug('Updating barometric pressure')
                self.main_win['sense_pres_out'].update(self.sense_hat.get_pressure())

                log.debug('Refreshing window!')
                self.main_win.refresh()

        # Exit the program cleanly
        if not self.main_active:
            clean_exit(0)


m_log_name = str(f'{ PROG }.GUI')
m_log = getLogger(m_log_name)

