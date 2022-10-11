def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    splitStr = [i for i in phrase]
    result = []
    for str in splitStr:
        if to_swap.islower():
            if str.islower() and str == to_swap:
                result.append(str.upper())
            elif str.isupper() and str.lower() == to_swap:
                result.append(str.lower())
            else:
                result.append(str)
        elif to_swap.isupper():
            if str.islower() and str.upper() == to_swap:
                result.append(str.upper())
            elif str.isupper() and str.upper() == to_swap:
                result.append(str.lower())
            else:
                result.append(str)
    return ('').join(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
