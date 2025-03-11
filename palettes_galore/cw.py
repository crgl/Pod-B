import colorcet as cc


def cw(v):
    '''
    A function that takes a number between 0 and 1 as input and returns a color
    Inputs: v, an integer between 0 and 1
    '''

    r = ((v * 10) % 10) / 10
    g = ((v * 100) % 10) / 10
    b = ((v * 1000) % 10) / 10

    return (r, g, b)