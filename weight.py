weight = input('weight: ')
unit = input("(L)bs or (K)gs? ")

if unit.upper() == "L":
    weight = int(weight) * 0.45
    print(f'you weight is {weight} kgs.')
else:
    weight = int(weight) * 2.2
    print(f'you weight is {weight} lbs.')200