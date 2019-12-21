weight= input('enter your weight: ')
unit= input('weight in (L)bs or (K)g: ')
if unit is 'L' or unit is 'l':
    print(f"your weight is {int(weight)*0.45} kg")
elif unit is 'K' or unit is 'k':
    print(f"your weight is {int(weight)/0.45} lbs")