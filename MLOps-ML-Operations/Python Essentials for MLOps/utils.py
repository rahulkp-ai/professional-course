def str_to_bool(val):
    """
    Convert a string represenation of truth to True or False
    Ture values are 'y', 'yes' or ''; case-insensitive
    False values are 'n' or 'no'; case-insensitive
    Raise ValuesError if 'val' is anything else.
    """

    true_vals = ['yes', 'y', '']
    false_vals = ['no', 'n']

    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("Invalid input vales: %s" % val)