from sys import argv

script, filename = argv

file1 = open(filename)

print(file1.read())
