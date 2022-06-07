import math

from trial_calci import AdvancedCalculator
from trial_calci import TrigonometricCalulator
from trial_calci import BasicCalculator

if __name__ == "__main__":

    calc = AdvancedCalculator(100, 200, 90, 90, 100)
    print(calc)
    calc1 = TrigonometricCalulator(100,200,90,90)
    print(calc1)
    calc2 = BasicCalculator(200,200)
    print(calc2)
    print('***** WELCOME TO CALCULATOR *****')
    print("******** List of Choices ********")
    print('*' * 100)
    print("1 : Addition  \t\t\t   10 : Cot in radians")
    print("2 : Subtraction \t\t   11 : Sine in degrees")
    print("3 : Multiplication\t\t   12 : Cosine in degrees")
    print("4 : Division  \t\t\t   13 : Tan in degrees")
    print("5 : Sine in radians\t\t   14 : Cosecant in degrees")
    print("6 : Cosine in radians\t   15 : Secant in degrees")
    print("7 : Tan in radians\t\t   16 : Cot in degrees" )
    print("8 : Cosecant in radians\t   17 : Base 10 log")
    print("9 : Secant in radians \t   18 : Square root")
    print("19 : Print all.")
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
            print(f"Sum of two numbers is {calc.do_addition()}")


        elif choice == 2:
            # first_number = float(input('enter the first number to subtract : '))
            # second_number = float(input('enter the second number to subtract : '))
            print(f"Difference between two numbers is {calc.do_substraction()}")

        elif choice == 3:
            # first_number = float(input('enter the first number to multiply : '))
            # second_number = float(input('enter the second number to multiply : '))
            print(f"Multiplication between two numbers is {calc.do_multiplication()}")

        elif choice == 4:
            # first_number = float(input('enter the first number to divide : '))
            # second_number = float(input('enter the second number to divide : '))
            print(f"Division of two numbers is {calc.do_division()}")

        elif choice == 5:
            #n = float(input('enter a number to find its sine in rad: '))
            print(f"Sine in radians is {calc.get_sine_radian()}")

        elif choice == 6:
            #n = float(input('enter a number to find its cos in rad: '))
            print(f"Cosine in radians is {calc.get_cosine_radian()}")

        elif choice == 7:
            #n = float(input('enter a number to find its tan in rad : '))
            print(f"Tangent in radians is {calc.get_tangent_radian()}")

        elif choice == 8:
            #n = float(input('enter a number to find its cosec in rad : '))
            print(f"Cosecant in radian is {calc.get_cosecant_radian()}")

        elif choice == 9:
           # n = float(input('enter a number to find its sec in rad : '))
            print(f"Secant in radian is {calc.get_secant_radian()}")

        elif choice == 10:
            #n = float(input('enter a number to find its cot in rad : '))
            print(f"Cotangent in radian is {calc.get_cotangent_radian()}")

        # elif choice == 11:
        #     calc.pie()

        elif choice == 11:
           # n = float(input('enter a number to find its sine in deg : '))
            print(f"Sine in degrees is {calc.get_sine_degree()}")

        elif choice == 12:
            #n =float(input('enter a number to find its cos in deg : '))
            print(f"Cosine in degrees is {calc.get_cosine_degree()}")

        elif choice == 13:
            #n = float(input('enter a number to find its tan in deg : '))
            print(f"Tangent in degrees is {calc.get_tangent_degree()}")

        elif choice == 14:
            #n =float(input('enter a number to find its cosec in deg : '))
            print(f"Cosecant in degrees is {calc.get_cosecant_degree()}")

        elif choice == 15:
            #n = float(input('enter a number to find its sec in deg : '))
            print(f"Secant in degrees is {calc.get_secant_degree()}")

        elif choice == 16:
            #n = float(input('enter a number to find its cot in deg : '))
            print(f"Cotangent in degrees is {calc.get_cotangent_degree()}")

        elif choice == 17:
            #n = float(input('enter a number to find its log to base 10 : '))
            print(f"Log to base 10 : {calc.get_log_ten()}")

        elif choice == 18:
            #n = float(input('enter a number to find its square root : '))
            print(f"Square root of a given is : {calc.get_square_root()}")

        elif choice == 19:
            #n = float(input('enter a number to find its square root : '))
            print(f"Sum of two numbers is {calc.do_addition()}")
            print(f"Difference between two numbers is {calc.do_substraction()}")
            print(f"Multiplication between two numbers is {calc.do_multiplication()}")
            print(f"Division of two numbers is {calc.do_division()}")
            print(f"Sine in radians is {calc.get_sine_radian()}")
            print(f"Cosine in radians is {calc.get_cosine_radian()}")
            print(f"Tangent in radians is {calc.get_tangent_radian()}")
            print(f"Cosecant in radian is {calc.get_cosecant_radian()}")
            print(f"Secant in radian is {calc.get_secant_radian()}")
            print(f"Cotangent in radian is {calc.get_cotangent_radian()}")
            print(f"Sine in degrees is {calc.get_sine_degree()}")
            print(f"Cosine in degrees is {calc.get_cosine_degree()}")
            print(f"Tangent in degrees is {calc.get_tangent_degree()}")
            print(f"Cosecant in degrees is {calc.get_cosecant_degree()}")
            print(f"Secant in degrees is {calc.get_secant_degree()}")
            print(f"Cotangent in degrees is {calc.get_cotangent_degree()}")
            print(f"Log to base 10 : {calc.get_log_ten()}")
            print(f"Square root of a given is : {calc.get_square_root()}")

        else:
            print("WARNING : Enter a valid input from the list above")
