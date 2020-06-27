"""

A module containing various functions that assist in debugging.

"""


def get_members(dir_res, inc_priv=False):
    """

    A module to get a sorted, formatted list of the requesters members

    Args:
        inc_priv ():
        dir_res ():

    Returns:
        list: Returns a list of requesters members. Optionally, does not filter private members

    """
    member_list = []

    for member in dir_res:
        if not inc_priv and member.startswith('__'):
            continue
        else:
            member_list.append(member)

    member_list.sort()

    return member_list
