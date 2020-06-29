import PySimpleGUIQt as Qt
from logging import getLogger

from ada_hub.lib.constants import PROG


class MainWindow(object):


    @staticmethod
    def sense_frame_layout():
        """

        A static method that returns a layout structure for a frame in PySimpleGUIQt

        Returns:
            frame layout object

        """
        from ada_hub.media.icons import sensor_refresh

        layout = [
                [ Qt.Text('Temperature:', justification='left'),
                  Qt.Text('', justification='center', key='sense_temp_out'),
                  Qt.Button('Refresh', image_data=sensor_refresh, key='refresh_sense_temp', enable_events=True,
                            size=(36, 36))],

                [ Qt.Text('Relative Humidity:', justification='left'),
                  Qt.Text('', justification='center', key='sense_hum_out'),
                  Qt.Button('Refresh', image_data=sensor_refresh, key='refresh_sense_hum', enable_events=True, ) ],

                [ Qt.Text('Barometric Pressure:', justification='left'),
                  Qt.Text('', justification='center', key='sense_pres_out'),
                  Qt.Button('Refresh', image_data=sensor_refresh, key='refresh_sense_pres', enable_events=True, ) ]
                ]

        return layout


    def main_layout(self):
        from ada_hub.media.icons import quit_icon
        """

        A method that returns a frame layout object for the entire window's frame

        Returns:
            frame layout object

        """
        layout = [
                [ Qt.Frame('Sensor Information', layout=self.sense_frame_layout()) ],
                [ Qt.Button('Quit', enable_events=True, key='quit_button', image_data=quit_icon),
                  Qt.Button('Refresh All', enable_events=True, key='refresh_all_button') ]
                ]

        return layout


    def __init__(self, config):
        """

        Instantiate a new instance of MainWindow

        """

        # Create an instance-flag that can be toggled to False or True when this window is active or not respectively
        self.win_active = False

        # Create a log-name for this class
        self.log_name = f'{PROG}.GUI.MainWindow'
        log = getLogger(self.log_name)
        log.debug(f'Started logger for {self.log_name}')
        log.debug(f'Initializing AdaHub.GUI.MainWindow...')

        Qt.theme(config['GUI_PREFS']['theme'])

        self.window = Qt.Window('AdaHub Home', layout=self.main_layout())
