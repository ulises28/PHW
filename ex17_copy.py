from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on one line, how?
indata = (open(from_file)).read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit ENTER to continue, CTRL +  C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
