from sys import argv

script, filename = argv #we are going to let the user enter the file name that will be read.

txt = open(filename)    #the usr will input the name of the file in the command line, the argv feature will help us to assign it to the variable filename

print(f"Here's your file {filename}: ")
print(txt.read())         #read the variable txt which have opened the txt file.

print("Type the filename again: ")
file_again = input("> ")    #instead of entering the file name in the command line we can use the input command

txt_again = open(file_again)#This is to open the variable file_again which will have the name of the file inputed by the Users
                            #the command is open(ex15_sample.txt)

print(txt_again.read())    # .read is the function applied to a variable to read the document
