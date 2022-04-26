import math
from trial_calci import Calculator

if __name__ == "__main__":

    calc = Calculator(30,20,30,5)
    print('**** WELCOME TO CALCULATOR *****')
    print("Here's a list of choices : ")
    print('*' * 100)
    print("1 : Addition  \t\t\t   11 : Sine in degrees")
    print("2 : Subtraction \t\t   12 : Cosine in degrees")
    print("3 : Multiplication\t\t   13 : Tan in degrees")
    print("4 : Division  \t\t\t   14 : Cosecant in degrees")
    print("5 : Sine in radians\t\t   15 : Secant in degrees")
    print("6 : Coisne in radians\t   16 : Cot in degrees")
    print("7 : Tan in radians\t\t   17 : Natural log")
    print("8 : Cosecant in radians\t   18 : Base 10 log")
    print("9 : Secant in radians \t   19 : Log base 'x'")
    print("10 : Cot in radians\t\t   20 : Square root")
    print('*' * 100)

    choice = ""
    while True:
        try:
            choice = int(input('enter a number of your choice from the above list : '))
        except:
            print("Enter a valid number")
        if choice == 1:
            # first_number = float(input('enter the first number to add : '))
            # second_number = float(input('enter the second number to add : '))
            print(f"Sum of two numbers is {calc.addition()}")


        elif choice == 2:
            # first_number = float(input('enter the first number to subtract : '))
            # second_number = float(input('enter the second number to subtract : '))
            print(f"Difference between two numbers is {calc.substract()}")

        elif choice == 3:
            # first_number = float(input('enter the first number to multiply : '))
            # second_number = float(input('enter the second number to multiply : '))
            print(f"Multiplication between two numbers is {calc.multiplication()}")

        elif choice == 4:
            # first_number = float(input('enter the first number to divide : '))
            # second_number = float(input('enter the second number to divide : '))
            print(f"Division of two numbers is {calc.division()}")

        elif choice == 5:
            #n = float(input('enter a number to find its sine in rad: '))
            print(f"sin is {calc.sinrad()}")

        elif choice == 6:
            #n = float(input('enter a number to find its cos in rad: '))
            calc.cosrad()

        elif choice == 7:
            #n = float(input('enter a number to find its tan in rad : '))
            calc.tanrad()

        elif choice == 8:
            #n = float(input('enter a number to find its cosec in rad : '))
            calc.cosecrad()

        elif choice == 9:
           # n = float(input('enter a number to find its sec in rad : '))
            calc.secrad()

        elif choice == 10:
            #n = float(input('enter a number to find its cot in rad : '))
            calc.cotrad()

        elif choice == 11:
            calc.pie()

        elif choice == 12:
            n = float(input('enter a number to find its sine in deg : '))
            calc.sindeg(self.degree)

        elif choice == 13:
            n =float(input('enter a number to find its cos in deg : '))
            calc.cosdeg(n)

        elif choice == 14:
            n = float(input('enter a number to find its tan in deg : '))
            calc.tandeg(n)

        elif choice == 15:
            n =float(input('enter a number to find its cosec in deg : '))
            calc.cosecdeg(n)

        elif choice == 16:
            n = float(input('enter a number to find its sec in deg : '))
            calc.secdeg(n)

        elif choice == 17:
            n = float(input('enter a number to find its cot in deg : '))
            calc.cotdeg(n)

        elif choice == 18:
            n =float(input('enter a number to find its natural deg : '))
            calc.ln(n)

        elif choice == 19:
            n = float(input('enter a number to find its log to base 10 : '))
            calc.logten(n)

        elif choice == 22:
            n = float(input('enter a number  : '))
            po = float(input('enter its power : '))
            calc.powerof(n,po)

        elif choice == 21:
            n = float(input('enter a number to find its square root : '))
            calc.squareroot(n)

        elif choice == 20:
            base = float(input('enter base value : '))
            n = float(input('enter a number to find its log to the given base value: '))
            calc.logbasex(n,base)

        else:
            print("WARNING : Enter a valid input from the list above")