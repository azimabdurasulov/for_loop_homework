def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """ 
    answer = []
    for i in list1:
        answer += [i.title()]
    return list(answer)

print(main(['rustam', 'diyor', 'alisher', 'bektosh']))