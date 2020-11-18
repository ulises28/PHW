def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

students = [
    {'name':'Bob','grades':[75,90,50,85,88]},
    {'name':'Ralph','grades':[]},
    {'name':'Jen','grades':[86,83,15,60,100]},
]

try:
    for student in students:
        name = student['name']
        grade = student ['grades']
        average = divide(sum(grade), len(grade))
        print(f"{name} average {average}")
except ZeroDivisionError:
    print(f"Error {name} has no grades!")
else:
    print("-- All studentes average calculated --")
finally:
    print("-- Thanks for your time --")