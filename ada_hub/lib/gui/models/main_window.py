import PySimpleGUIQt as qt

def env_layout():
    arrangement = [qt.Text('Temperature'), qt.Text('00.00℉')]

def layout():
    arrangement = [qt.Frame('Environment Data', layout=env_layout())]

