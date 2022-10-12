def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    from collections import Counter
    valueList = [k for k, v in Counter(nums).items() if v>1]
    if not valueList:
        return None
    return valueList[0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()