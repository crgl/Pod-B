import colorcet as cc


def cg(v):
    '''
    A function that takes a number between 0 and 1 as input and returns a color
    '''
    if v < 0.5:
        return '#bbbbbb'
    else:
        return (0.1, 0.1, 0.1)