import PySimpleGUIQt as Qt
from logging import getLogger

from ada_hub.lib.constants import PROG

from ada_hub.lib.gui.helpers import import_icon_set

# Import Sense Hat interface
from ada_hub.lib.ada_sense import AdaSense

class MainWindow(object):


    def sense_frame_layout(self):
        """

        A static method that returns a layout structure for a frame in PySimpleGUIQt

        Returns:
            frame layout object

        """
        layout = [
                [ Qt.Text('Temperature:', justification='left'),
                  Qt.Text(self.ada_sense.get_temp(), justification='center', key='sense_temp_out'),
                  Qt.Button('Refresh', image_data=self.icons.refresh, key='refresh_sense_temp', enable_events=True,
                            size=(36, 36))],

                [ Qt.Text('Relative Humidity:', justification='left'),
                  Qt.Text(self.ada_sense.get_humidity(), justification='center', key='sense_hum_out'),
                  Qt.Button('Refresh', image_data=self.icons.refresh, key='refresh_sense_hum', enable_events=True, ) ],

                [ Qt.Text('Barometric Pressure:', justification='left'),
                  Qt.Text(self.ada_sense.get_pressure(), justification='center', key='sense_pres_out'),
                  Qt.Button('Refresh', image_data=self.icons.refresh, key='refresh_sense_pres', enable_events=True, ) ]
                ]

        return layout


    def main_layout(self):
        """

        A method that returns a frame layout object for the entire window's frame

        Returns:
            frame layout object

        """
        layout = [
                [ Qt.Frame('Sensor Information', layout=self.sense_frame_layout()) ],
                [ Qt.Button('Quit', enable_events=True, key='quit_button', image_data=self.icons.quit),
                  Qt.Button('Refresh All', enable_events=True, key='refresh_all_button',
                            image_data=self.icons.refresh) ]
                ]

        return layout


    def __init__(self, config):
        """

        Instantiate a new instance of MainWindow

        """

        # Gather the name of the icon set we should be using. We will use this to search the icon set packages
        icon_set_str = config['GUI_PREFS']['icon_set']
        self.icons = import_icon_set(icon_set_str)

        # Create an instance-flag that can be toggled to False or True when this window is active or not respectively
        self.win_active = False

        # Start an instance of the AdaSense class which will allow us to easily interface with the SenseHat
        self.ada_sense = AdaSense(config=config)

        # Create a log-name for this class
        self.log_name = f'{PROG}.GUI.MainWindow'
        log = getLogger(self.log_name)
        log.debug(f'Started logger for {self.log_name}')
        log.debug(f'Initializing AdaHub.GUI.MainWindow...')

        Qt.theme(config['GUI_PREFS']['theme'])

        self.window = Qt.Window('AdaHub Home', layout=self.main_layout(), no_titlebar=True, alpha_channel=0.8,
                                grab_anywhere=True)
