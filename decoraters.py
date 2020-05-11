# def func():
#     print("hello")
# fun = func
# fun()
# del func
# fun() 


# def func(num):
#     if num==0:
#         return print
#     elif num==1:
#         return int
# print(func(0))
# print(func(1))

# def func(fun):
#     fun("hi")
# func(print)

# def dec1(fun):
#     print("you are fine")
#     def executed():
#         print("execute now")
#         fun()
#         print("executed")
#     return executed
# def hello():
#     print("this is hello")

# hello()
# Hello = dec1(hello)
# Hello()

def dec2(fun):
    def executed():
        a=9
        b=9
        print("execute now")
        fun(a,b)
        print("executed")
    return executed

# @dec2
# def hi():
#     print("this is hello")

# hi()

@dec2
def he(a,b):
    print(f"a+b={a+b}")
he()