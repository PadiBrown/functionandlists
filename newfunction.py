def dragon(heat, damage=10):
    """
    Creates a mean dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: how hard dragn bites (1-50)
    :return: the sum of heat and damage
    """
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("You must use numbers for dragon attributes")
        return
    #here is the body of the function
    print(f'You are creating a dragon with fire power of {heat} and bite power of {damage}')
    return heat+damage

dragon1 = dragon(100, 490)
dragon2 = dragon(heat=24, damage=69)
if dragon1 > dragon2:
    print("dragon1 is stronger")
else:
    print("Dragon2 is stronger")

dragon3 = dragon(39)