from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #this method set the pointer were you want, in this case at the beginning, because if you read the file you move the pointer

def print_a_line(line_count, f):
    print(line_count, f.readline()) #each time you read the line the pointer moves

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) #current file opens the file given in the command line_count

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line
= current_line + 1
print_a_line(current_line, current_file)
