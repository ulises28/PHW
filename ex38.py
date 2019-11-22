ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')   #will divide the string into a list on each space (' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: #do the while loop when the lenght of stuff is different from 10, should be lower
    next_one = more_stuff.pop() #pop() removes the last element of the list [-1] and returns it
    print(f"Adding: {next_one}")
    stuff.append(next_one)  #Adds the last value of more_stuff to stuff list at the end
    print(f"There are {len(stuff)} items now, in stuff list.")

print(f"There we go: {stuff}")
print("Let's do some things with stuff.")

print(stuff[1]) #prints the second element of the stuff list, first is [0]
print(stuff[-1])#prints the last element from stuff list
print(stuff.pop())#removes and return the last value of the string
print(' '.join(stuff)) #makes a string of the entire list, it add an space between each index ' '
print('#'.join(stuff[3:5])) #makes a string of the stuff list, from 3 to 5 index and adds an '#' between each index
