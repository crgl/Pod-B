import colorcet as cc


def yc(v):
    '''
    A function that takes a number between 0 and 1 as input and returns a color
    '''
    if v < 0.5:
        return '#bbbbbb'
    else:
        return '#00008b'