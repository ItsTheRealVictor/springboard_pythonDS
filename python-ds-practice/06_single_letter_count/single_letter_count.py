def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    resultMap = {}
    if letter in word.lower():
        for char in word.lower():
            if char not in resultMap:
                resultMap[char] = 1
            else:
                resultMap[char] += 1

        return resultMap[letter]
    return 0



if __name__ == '__main__':
    import doctest
    doctest.testmod()