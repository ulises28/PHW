def Greeting():
    print("Hi this is an imported module from -->", __name__) #__name__ global variable that shows the path, duner __name__ is
                                                              #equal to dunder __main__ in the file you're running the code.

def Maths(a,b):
    print(f"{a}+{b} =", a + b)
    print(f"{a}*{b} =", a * b)
    print(f"{a}/{b} =", a / b)
    print(f"{a}%{b} =", a % b)