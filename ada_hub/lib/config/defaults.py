from ada_hub.lib.constants import PROG, DEFAULT_DATA_ROOT, DEFAULT_CONF_ROOT, DEFAULT_RUN_ROOT

run_root = DEFAULT_RUN_ROOT
conf_root = DEFAULT_CONF_ROOT
root = DEFAULT_DATA_ROOT


conf_file_contents = []


def runtime_conf():

    title = 'APP'

    content = {
            title: {

                    'conf_file_path': run_root,
                    'data_root_path': conf_root,
                    'run_dir_path':   root

                    },
            }

    return content


def runtime_stats():

    title = 'RUNTIME.STATS'

    content = {

            title: {

                    'ada_vise_enabled': 'False',
                    'history_enabled': 'True',

                    },
            }

    return content


def gui_conf():

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

    title = 'SENSE.DEVICE'

    content = {

            title: {

                    'device_name': '',
                    'device_local_ip': '',
                    'has_cam': 'False'

                    },
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


def weather_conf():

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


def create_new_config():
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
