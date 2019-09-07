typesOfPeople = 10
x = f"There are {typesOfPeople} types of people."

binary = "binary"
doNot = "don't"
y = f'Those who know {binary} and those who {doNot}.'

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False    #declaration for hilarious as a boolean
joke_evaluation = "Isn't that a joke so funny?! {}"     #inserts a black curly brackets that will take the value mentioned below

print(joke_evaluation.format(hilarious))       #Adds the evaluation false to the sentence, false is a boolean, this also works with a string

w = "This is the left side of..."
e = "a string with a right side"

print (w + e) #Concatenate a string
