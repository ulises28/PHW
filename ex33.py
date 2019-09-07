def exercise33(a, b):
    i = 0
    numbers = []
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)                #Append inserts one value at the end of the list
        i += b
        print(f"Numbers now: {numbers}")#prints the list at each time the loop executes
        print(f"At the bottom i is {i}")


limit = int(input("Enter the limit of the while function: "))
increment = int(input("Enter the increment of the while function: "))
exercise33(limit, increment)
