from collections import Counter

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    letter_count = dict(Counter(phrase))
    return {k:v for k, v in letter_count.items() if k in vowels}



if __name__ == '__main__':
    import doctest
    doctest.testmod()