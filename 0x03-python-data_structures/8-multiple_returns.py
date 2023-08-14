#!/usr/bin/python3
def multiple_returns(sentese):
    """returns the length of a string and its first character."""
    if sentense == '':
        return (0, None)
    return (len(sentence), sentense[0])
