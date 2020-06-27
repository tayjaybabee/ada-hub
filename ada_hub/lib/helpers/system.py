import platform
from logging import getLogger

from ada_hub.lib.constants import PROG, ISSUE_URL

# Create a logger for the module as a whole. This is mainly to track import flow.
m_log_name = f'{PROG}.Helpers.System'
members = dir()
m_log = getLogger(m_log_name)
m_log.debug(f'Imported {__name__}! ({__file__})')
m_log.debug(f'')

def x_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0

def get_os_family():

    os_name = platform.platform().lower()


def gui_capable():

    #
