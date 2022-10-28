def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    i = 0
    x = ''
    for i in range(n):
        x += ',' + str(i) 
    return x[1:]

print(main(4))