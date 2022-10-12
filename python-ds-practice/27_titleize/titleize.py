def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words = [word.title() for word in phrase.split(' ')]
    return (' ').join(words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
    