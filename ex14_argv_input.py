from sys import argv    #argv is the argument variable

script, use_name = argv #this are the parameters that will be inputed in the command line
prompt = '> '           #This variable is just to create the feeling of an old gaming interface

print(f"Hi {use_name}, I'm the {script} script.")
print("I'd like to ask you a few questions. ")
print(f"Do you like me {use_name}?")
like = input(prompt)


print(f"Where do you live {use_name}?")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"""
Alrigth, so you said {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
