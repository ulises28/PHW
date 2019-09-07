name = "Ulises Saavedra"
age = 29
height = 1.75 # cm
weight = 71 # kgs
eyes = "brown"
hair = "brown"
teeth = "white"
height_inches = (height * 100) / 2.54
weight_pounds = (weight * 2.20462)

print (f"My name is {name}.")       #f before the string indicates that it needs to be formatted
print (f"I'm {age} old")            #the variable inside {} will be embeded
print (f"I'm {height} cm or {round(height_inches)} inches tall")
print (f"My weight is {weight} kgs or {round(weight_pounds)} pounds")
