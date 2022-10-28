def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    i = 0
    s = 0
    for i in range(A, B):
        s += i
        i += 1
        
    return s

print(main(3, 6))