class GUIConfig:

    def save_to_disk(self):
        pass

    def load(self, custom_conf_path=None):
        pass

    def __init__(self):
        pass



from ada_hub.lib.gui.models.windows.main import MainWindow
from ada_hub import clean_exit

class GUIApp(object):

    def __init__(self):
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

