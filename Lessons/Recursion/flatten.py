def flatten(my_list):
    result = []

    for element in my_list:
        if isinstance(element, list):
            print("A List is Found.")
            print("Items in list include: {}".format(element))
            flat_list = flatten(element)
            result += flat_list

        else:
            result.append(element)

    return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]


print(flatten(planets))