"""

Author: Taylor-Jayde Blackstone <t.blackstone@inspyre.tech>
since: 1.0a

Description:

    A collection of constructor-functions that will make a new default config file to be filled later.

"""

from ada_hub.lib.constants import PROG, DEFAULT_DATA_ROOT, DEFAULT_CONF_ROOT, DEFAULT_RUN_ROOT
from configparser import ConfigParser

run_root = DEFAULT_RUN_ROOT
conf_root = DEFAULT_CONF_ROOT
root = DEFAULT_DATA_ROOT

def runtime_conf():
    """

    Create a dictionary containing the section 'APP' and define its default options

    Returns:
        dict: A two-deep nested dictionary that makes up the 'APP' section of the application's config

    """

    title = 'APP'

    content = {
            title: {

                    'conf_file_path': conf_root,
                    'data_root_path': run_root,
                    'run_dir_path':   root

                    },
            }

    return content


def runtime_stats():
    """

    Create a nested dictionary containing the 'APP.STATS' section for AdaHub's config

    Returns:
        dict: A two-deep nested dictionary that contains 'APP.STATS' section of AdaHub's config.

    """

    title = 'RUNTIME.STATS'

    content = {

            title: {

                    'ada_vise_enabled': 'False',
                    'history_enabled': 'True',

                    },
            }

    return content


def gui_conf():
    """

    Create a nested dictionary containing the 'GUI' section for AdaHubs config.

    Returns:
        dict:
            A two-deep nested dictionary containing the 'GUI' section and its options

    """

    title = 'GUI'

    content = {

            title: {
                    'theme': 'DarkBlack1',
                    'icon_set': 'midnite',
                    'template': '',
                    'grab_anywhere': 'True',
                    'advanced_mode': 'False'
                    },
            }

    return content


def sense_conf():
    """

    Create a nested dictionary containing the 'SENSE' section and its options for AdaHubs config

    Returns:
        dict:
            A two-deep nested dictionary that contains the 'SENSE' section of the application's config

    """

    title = 'SENSE'

    content = {

            title: {

                    'always_emulate': 'False',
                    'never_emulate': 'False',
                    'temp_scale': 'f',
                    'always_auto_refresh': 'False'

                    },
            }

    return content


def sense_device():
    """

    Create a nested dictionary that contains the 'SENSE.DEVICE' section of the config file and its options

    Returns:
        dict:
            A two-level nested dictionary that contains the 'SENSE.DEVICE' section of the config file and its options

    """

    title = 'SENSE.DEVICE'

    content = {

            title: {

                    'device_name': '',
                    'device_local_ip': '',
                    'has_cam': 'False'

                    },
            }

    return content


def weather_conf():
    """
    
    Create a nested dictionary that contains the 'SENSE.DEVICE' section of the config file and its options
    
    Returns:
        dict:
            A two-level nested dictionary that contains the 'SENSE.DEVICE' section of the config file and its options

    """"""
    
    
    Returns:

    """

    title = 'WEATHER'

    content = {

            title: {

                    'temp_scale': 'metric',
                    'refresh_secs': '900',
                    'allergy': 'False',
                    'show_phase': 'True',
                    'tray_hover': 'True'

                    }

            }

    return content



def weather_notifications():

    title = 'WEATHER.NOTIFICATIONS'

    content = {

            title: {

                    'silence_all': '',
                    'weather_alerts': 'True',
                    'sunset_approaching': '',
                    'sunrise_approaching': '',
                    'full_moon': '',

                    },

            }

    return content


def locale_conf():

    title = 'LOCATION'

    content = {

            title: {

                    'alt_ip': '',
                    'allow_ip_search': '',
                    'steet_address': '',
                    'city': '',
                    'region': '',
                    'country': '',
                    'postal': '',
                    'lat': '',
                    'lon': '',

                    }

            }

    return content


def create_new_config(args):
    """



    Args:
        args ():

    Returns:

    """
    from configparser import ConfigParser

    parser = ConfigParser()

    sections = [

            runtime_conf(),
            runtime_stats(),
            gui_conf(),
            sense_conf(),
            sense_device(),
            weather_conf(),
            weather_notifications(),
            locale_conf()

            ]

    for section in sections:
        parser.read_dict(section)

    return parser
