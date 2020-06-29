import platform
from logging import getLogger

from ada_hub.lib.constants import PROG, ISSUE_URL
from ada_hub.lib.helpers.debug import format_members

# Create a logger for the module as a whole. This is mainly to track import flow.
m_log_name = f'{PROG}.Helpers.System'
m_log = getLogger(m_log_name)

# If running verbosely let's announce that we've been imported
m_log.debug(f'Imported {__name__}! ({__file__})')

# Set up \\
members = dir()
members = format_members(members, False)

mem_str = members[1]
mem_list = members[0]

m_log.debug(f'I bring the following members: {mem_str}')


def x_is_running():
    """

    If you are in a Unix environment this will check if XServer is installed in your environment. Will return a boolean.

    _A Note About Methodology_:

        *xset*:
            If you're running a linux environment and using certain (graphically oriented) features of this program (
            i.e. the SenseHat emulator) the program will need to check if you are indeed capable of sup0porting such
            features.

            The method by which I determine your ability to support even the most basic of graphical elements of this
            program is to assess the availability of xserver on your system, or more specifically; it's presence (
            namely it's executables) in your PATH. Xset is the command that I utilize to determine GUI capability of
            the host system.

            The unix command 'xset' comes with x11-xserver-utils command and just allows one to either query it for
            configuration information or set options. We're going to call xset with the '-q' flag which simply prints
            out the status of xserver and quits. This is preferred as it makes no changes to the system and is of
            minimal resource drain if xserver is installed.

        *The More You Know*

    Returns:
        bool: Is XServer present? True is yes, False is no.

    """
    from subprocess import Popen, PIPE


    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)

    # Open our Pipe instance
    p.communicate()

    # The call to the returncode, comparing it to a clear exit code of zero. If it fails to match; the return will be
    # False, otherwise the return will be True which should signal OK
    return p.returncode == 0

    # END


def get_os_family():
    """

    Fetch the line of operating systems that the current environment was?

    Returns:
        string: What will be returned will be one of the following: windows, linux, mac

    """
    os_name = platform.platform().lower()

    # Gotta return what we found
    return os_name


def gui_capable():
    """

    Is the current environment able to produce a graphical user interface on-demand?

    Returns:
        bool: Is the system GUI-capable? True for yes, False for no

    """

    os_fam = get_os_family()
    if os_fam == 'windows':
        return True

    if os_fam == 'linux':
        if x_is_running():
            return True
        else:
            return False
