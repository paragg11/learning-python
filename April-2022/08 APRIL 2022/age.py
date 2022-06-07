# YOUR AGE IN 2090
# TAKE AGE OR YEAR OR BIRTH AS AN INPUT FROM USER AND TELL THEM WHEN THEY WILL TURN 100 YEARS OLD
# DONT USE ANY KIND OF MODULE LIKE DATETIME
# THEY THEN PROVIDE YEAR AND YOUR AGE IN THAT PARTICULAR YEAR:
# YOU ARE NOT YET BORN
# YOU SEEM TO BE OLDEST PERSON ALIVE
# YOU CAN ALSO HANDLE ANY OTHER ERROR IF POSSIBLE


age = int(input("What is your age/Age of birth???"))
isAge = False
isYear = False

if(len(str(age))) == 5:
    isYear = True
else:
    isAge = True

if(isYear == True):
    print("You seem to be oldest person alive.")
    exit()

if(age>>2022):
    print("You are not born yet.")
    exit()

if isAge:
    age = 2022 - age

print(f"You will be 100 years old in {age + 100}")
