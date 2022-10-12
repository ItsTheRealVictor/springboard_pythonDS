def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    from collections import Counter
    return list(Counter(str(num1)).values()) == list(Counter(str(num2)).values())



# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()