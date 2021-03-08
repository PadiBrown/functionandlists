def check_odd_even(number, odd=True):
    """
    THis function checks whether a number is odd or even
    :param number: the number to checkk
    :param odd: True for ODD, False for even
    :return: None, just prints
    """
    if odd:
        if number % 2 ==1:
            print(f"Correct, number {number} is odd")
        else:
            print(f"Wrong, number {number} is not odd")
    else:
        if number % 2 == 0:
            print(f"Correct, number {number} is even")
        else:
            print(f"Wrong, number {number} is not even")

check_odd_even(7)
check_odd_even(12)
check_odd_even(12, odd=False)
check_odd_even(7, False)