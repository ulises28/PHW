print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuiton
and requires an explanation
\n\t\twhere there is none
"""

print('--------------------')
print(poem)
print('--------------------')

five = 8 - 3 + 7 - 3 - 4
print(f"This should be five: {five}")

def secret_formula(started):        #declare function secret_formula with one argument
    jelly_beans = started * 500     #starte argument * 500 stored in jelly beans secret_formula
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates    #return 3 variables

ulises_test = 45678
start_point = 1000  #variable start_point
beans, jars, crates = secret_formula(start_point)   #saves the 3 returned variables given by the function secret_formula
                                                    #An alternate syntax when dealing with multiple return values is to have Python "unwrap"
                                                    #the tuple into the variables directly by specifying the same number of variables on the
                                                    #left-hand side of the assignment as there are returned from the function, e.g.

#remember that this is another way to format a string
print("With a starting point of:{}".format(start_point)) #after the dot we use the format method and add the value of the variable start start_point
print("With a starting point of:{}".format(ulises_test))
#it's just like with an f"" starting
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point /= 10

print('We can also do that this way:')
formula =  secret_formula(start_point)
#This is an easy way to apply a list to a format starting
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #formula variable has the value of the tuple sent with the return command

#The * can also be used for unpacking the containers.
#Its principles is similar to “For using the variadic arguments”  --> *args and *kwargs
#in above. The easiest example is that we have data in the form
#of a list, tuple or dict, and a function take variable arguments
