def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    teskari = list(range(A, B + 1))
    return teskari[::-1]

print(main(5, 9))