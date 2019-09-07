Name = input("Name? ")          #instead of adding a string with print, we can add it inside parenthesis
print("How old are you?", end=" ") #Tells print to not end the line with a new line character and go to the next line, allows us to write just after the question
age = input()                      #Input instruction is inserted just after the line above because of the concatenation with end=''
print("How tall are you?", end=" ")
height = input()              #If you want an integer number you can use height = int(input())
print("How much do you weight?", end=" ")
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy")

#the use of pydoc, example "python -m pydoc input" it is like a help command that will give all the details of function
