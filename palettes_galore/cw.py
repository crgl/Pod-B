import colorcet as cc


def cw(v):
    '''
    A function that encodes different place values
    of a number less than 1 in the r, g, and b channels
    in a color.
    '''

    r = ((v * 10) % 10) / 10
    g = ((v * 100) % 10) / 10
    b = ((v * 1000) % 10) / 10

    return (r, g, b)