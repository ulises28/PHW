from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on one line, how?
print(f"Copy {from_file} to {to_file}")
(open(to_file, 'w')).write((open(from_file)).read())
print("Alright, all done.")
