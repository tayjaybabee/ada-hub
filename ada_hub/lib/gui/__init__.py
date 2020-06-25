from ada_hub.lib.constants import PROG
from ada_hub.lib.config import write_config

from logging import getLogger

class GUIConfig:

    def merge_default_config(self, prog_conf):
        prog_conf.add_section('GUI_PREFS')
        prog_conf.set('GUI_PREFS', 'theme', 'DarkAmber')
        prog_conf.set('GUI_PREFS', 'grab_anywhere', 'False')
        prog_conf.set('GUI_PREFS', 'advanced_mode', 'False')

        return prog_conf

    def save_to_disk(self, config, config_path):

        write_config(config, config_path)

    def load(self, custom_conf_path=None):
        pass

    def __init__(self, config):
        log_name = str(f'{PROG}.GUIConfig')
        log = getLogger(log_name)

        gui_prefs = 'GUI_PREFS'

        if gui_prefs in config.sections():
            log.debug('Found the section "GUI_PREFS" in config file')
            self.conf = config
        if 'runtime'.upper() in config.sections():
            self.save_to_disk(config, config['RUNTIME']['conf_file_path'])

        if gui_prefs not in config.sections():
            config = self.merge_default_config(config)

        self.conf = config




from ada_hub.lib.gui.models.windows.main import MainWindow
from ada_hub import clean_exit

class GUIApp(object):

    def __init__(self, config):
        main_win = MainWindow()
        self.main_win = main_win.window

        self.main_active = main_win.win_active

        if self.main_active:
            return

        self.main_active = True

        while self.main_active:

            event, vals = self.main_win.read(timeout=100)

            if event is None or event == 'quit_button':
                self.main_win.close()
                self.main_active = False

        if not self.main_active:
            clean_exit(0)

