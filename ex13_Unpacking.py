# You need to call this script in the command line like this
# PS C:\Users\ulise\PythonHardWay> python ex13_Unpacking.py first 2nd 3rd
from sys import argv    #argv is the argument variable
#reah the WYSS section for how to run this

script, first, second, third = argv
fourth = input("Enter the fourth variable: ")
print("The script id called: ", script)
print("The first variable is: ", first)
print("The second variable is: ", second)
print("The third variable is: ", third)
print("The fourth variable is: ", fourth)
