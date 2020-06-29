"""

A module containing various functions that assist in debugging.

"""


def format_members(dir_res, inc_priv=False):
    """

    A module to get a sorted, formatted list of the requesters members

    Args:
        inc_priv (bool): Should this function include exposed private members in it's returned tuple?
        dir_res (list): The list the caller receives after calling 'dir()'

    Returns:
        Tuple: Returns a list of requesters members. Optionally, does not filter private members

    """

    # Prepare an empty list to transfer the received member names to after manipulating it appropriately
    member_list = []

    # Iterate through the received member list
    #   - If we are not including private members in our return we will refrain from adding members that start with
    #     '__' to the end-result
    for member in dir_res:
        if not inc_priv and member.startswith('__'):
            continue
        else:
            member_list.append(member)

    member_list.sort()

    mem_list_str = ','.join(member_list)

    return member_list, mem_list_str
