formatter = "{} {} {} {}" #The curly brackets must be inside single or double quotes
print (formatter.format(1, 2, 3, 4)) #each time we use a dot we are applying an attribute to a variable
print (formatter.format('one', 'two', 'three', 'four')) #it could be a number or a string, the language automatically gets it
print (formatter.format(True, False, True, False))      #even a boolean!
print (formatter.format(formatter, formatter, formatter, formatter))    # A variable
print (formatter.format("Ulises Saavedra Bermudez", "Raider Fan", "Favorite number #28", "Favorite color black"))
print ("""Este metodo
Permite escribir linea por linea
Sin la necesidad de introducir un salto de linea
""")
