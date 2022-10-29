def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    odd = 0
    sum = 0
    for odd in range(1, N, 2):
        sum += odd
        odd += 1
    return sum

print(main(12))