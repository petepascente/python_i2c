name = ""
age = 0
currentYear = 0
yearBorn = 0

name = input("Enter name")
age = int(input("Enter age:"))
currentYear = int(input("Year?"))

yearBorn = currentYear - age
print("You were born: " + str(yearBorn))