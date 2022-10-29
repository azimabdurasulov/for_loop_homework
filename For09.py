def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """ 
    sum = 0
    list1 = []
    for i in range(10):
        sum += price
        list1 += [sum]
    return list1
    
print(main(2.25))