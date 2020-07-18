"""

Determine locale

"""
from ada_hub.lib.constants import PROG

from logging import getLogger
import requests


# Start a logger for debugging


def get_by_ip(conf):
    """



    Args:
        conf ():

    Returns:

    """

    url = 'https://ipapi.co/json/'

    res = requests.get(url)

    status = res.status_code

    if not status == 200:
        raise ConnectionError(f'Unable to connect to {url}. (Received a status code of {status}')

    data = res.json()

    conf.set('LOCATION', 'city', data[ 'city' ])
    conf.set('LOCATION', 'region', data[ 'region' ])
    conf.set('LOCATION', 'country', data[ 'country_name' ])
    conf.set('LOCATION', 'postal', data[ 'postal' ])
    conf.set('LOCATION', 'lat', data[ 'latitude' ])
    conf.set('LOCATION', 'lon', data[ 'longitude' ])


def determine(conf, address: str = None, coords: tuple = None, postal: int = None, force_ip_search: bool = False,
              forbid_ip_search: bool = False, alt_ip: int = None, alt_address: str = None):
    """

    Args:
        conf ():
        address ():
        coords ():
        postal ():
        force_ip_search ():
        forbid_ip_search ():
        alt_ip ():
        alt_address ():

    Returns:

    """
    args = [ address, coords, postal, forbid_ip_search, alt_address ]
    loc_conf = conf[ 'LOCATION' ]

    # A LAT,LNG pair is a pretty accurate triangulation for weather. Give it up, here.
    if (loc_conf[ 'lat' ] and loc_conf[ 'lon' ]) or coords:
        final_coords = (loc_conf[ 'lat' ], loc_conf[ 'lon' ])
        return final_coords

    opts = [
            loc_conf[ 'city' ],
            loc_conf[ 'region' ],
            loc_conf[ 'country' ],
            loc_conf[ 'postal' ]
            ]

    loc_indicated = False

    for opt in opts:
        if opt:
            loc_indicated = True

    return
