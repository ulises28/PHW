def Greeting():
    print("Hi this is an imported module", __name__) #__name__ global variable that shows the path, __main__ is the dunder 
                                                     #which means where you are placing at.

def Maths(a,b):
    print(f"{a}+{b} =", a + b)
    print(f"{a}*{b} =", a * b)
    print(f"{a}/{b} =", a / b)
    print(f"{a}%{b} =", a % b)