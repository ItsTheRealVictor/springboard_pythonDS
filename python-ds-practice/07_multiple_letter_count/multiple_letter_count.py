def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    charMap = {}
    for letter in phrase:
        if letter not in charMap:
            charMap[letter] = 1
        else:
            charMap[letter] += 1
    return charMap

    # # CHEEKY ALTERNATIVE
    # from collections import Counter
    # return dict(Counter(phrase))

if __name__ == '__main__':
    import doctest
    doctest.testmod()