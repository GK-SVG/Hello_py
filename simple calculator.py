print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')
while True:
    choice = input('Enter a choice : ')
    num1 = input('enter 1st number : ')
    num2 = input('enter 2nd number : ')
    if int(choice) ==1:
        print(f"Addition = {int(num1) + int(num2)}")
    elif int(choice) == 2:
        print(f"Addition = {int(num1) - int(num2)}")
    elif int(choice) == 3:
        print(f"Addition = {int(num1) * int(num2)}")
    elif int(choice) == 4:
        print(f"Addition = {int(num1) / int(num2)}")
    elif int(choice) == 5:
        break
    else:
        print('Invalid choice')

