def bond_a_name(firstname, lastname):
    """
    Bond, James Bond
    :param firstname: first name
    :param lastname: last name
    :return: last, first, last
    """
    return f"{lastname}, {firstname}, {lastname}"

def greet(name):
    f"""
    print: The name is {name}
    :param name: The name to use
    :return: nothing
    """

    print(f"the name is: {name}")

greet(bond_a_name())
greet(bond_a_name("Padi","Brown"))
