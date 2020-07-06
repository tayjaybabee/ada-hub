from ada_hub.lib.constants import PROG

from logging import getLogger


def c_to_f(temp):
    # Start logger...
    log_name = str(f'{PROG}.AdaSense.convert_temp_to_f')
    log = getLogger(log_name)

    log.debug(f'Received request to convert {temp} into degrees Fahrenheit...')

    notation = '°F'

    # Do maths
    new_temp = (temp * 1.8) + 32

    # Round new_temp
    r_temp = round(new_temp)

    # Append our notation
    f_temp = str(f'{r_temp} {notation}')

    # Return f_temp to the caller
    return f_temp
