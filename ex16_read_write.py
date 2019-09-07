from sys import argv

script, filename = argv #in the command line we'll insert the script and the filename

print(f"We're going to erase {filename} file.") #Give the instructions to the user, and presents the filename
print("If you don't want that, hit CTRL-C (^C).")   #
print("If you do want that, hit ENTER.")

input("?")  #saves the value in the input, but there is no variable

print("Opening the file...")
target = open(filename, 'w') #open the file and save it in the variable target, add the 'W' otherwise the file can't be truncate

print("Truncating the file... Goodbye!")
target.truncate()   #truncate command will erase a file

print("Now I'm going to ask you for three lines")
line1 = input("Line 1: ")   #requests you to input a text and then will be save in the variable Line1
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file. ")
target.write(line1) #Is appliying the command write, so the Line1 content will be added to the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close the file. ")
target.close()  #We close the file
