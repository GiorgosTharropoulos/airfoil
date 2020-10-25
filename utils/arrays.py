def is_symmetric(array, i=0):
    """Check if array is symmetric

    Args:
        array (list): array of numerical values
        i (int, optional): looking at now. Defaults to 0.

    Returns:
        boolean
    """

    if i > int(len(array) / 2):
        return True

    elif array[i] != abs(array[len(array) - 1 - i]):
        return False

    else:
        return is_symmetric(array, i + 1)
