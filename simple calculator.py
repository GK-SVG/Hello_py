def addition(a,b):
    print(f'addition {a+b}')
    return


def substract(a,b):
    print(f'substraction {a-b}')
    return


def multiplication(a,b):
    print(f'multiplication {a*b}')
    return


def division(a,b):
    try:
        print(f'division {a/b}')
        return
    except ZeroDivisionError:\
        print("b != 0 invalid devider" )


def switch(task, a, b):
    switcher = {
    1: addition(a,b),
    2: substract(a,b),
    3: multiplication(a,b),
    4: division(a,b),
    5: exit()
    }
    for tas in task:
        switcher.get(tas)



print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')
num1 = int(input('enter 1st number: '))
num2 = int(input('enter second number :'))
task = int(input('enter your choice: '))
switch(task,num1,num2)



