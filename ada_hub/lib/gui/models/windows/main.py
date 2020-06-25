import PySimpleGUIQt as Qt
from logging import getLogger

from ada_hub.lib.constants import PROG

class MainWindow(object):

    def sense_frame_layout(self):
        layout = [
                [Qt.Text('Temperature:', justification='left'),
                 Qt.Text('', justification='right', key='sense_temp_out'),
                 Qt.Button('', image_data=)],

                [Qt.Text('Relative Humidity:', justification='left'),
                 Qt.Text('', justification='right', key='sense_hum_out')],

                [Qt.Text('Barometric Pressure:', justification='left'),
                 Qt.Text('', justification='right', key='sense_pres_out')],

        ]

    def __init__(self):

        # Create an instance-flag that can be toggled to False or True when this window is active or not respectively
        self.win_active = False

        # Create a log-name for this class
        self.log_name = f'{PROG}.GUI.MainWindow'
        log = getLogger(self.log_name)
        log.debug(f'Started logger for {self.log_name}')
        log.debug(f'Initializing AdaHub.GUI.MainWindow...')


