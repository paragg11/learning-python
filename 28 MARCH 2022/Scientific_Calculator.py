import math

'''
BasicCalculator -> add sub, mul,div
AdvanceCalculator -> negate, reciprocal
TrigonometryCalculator -> sin, cos ,tan
MathematicsCalculator -> square, square_root, cube , cube_root ,exponential
ProgrammerCalculator -> AND, OR, XOR , NOR, RIGHT SHIFT ,LEFT SHIFT, one's compliment, two's compliment , bit flip
Scientific ->BasicCalculator + AdvanceCalculator + TrigonometryCalculator + MathematicsCalculator0
'''


class BasicCalculator:

    def __init__(self, num1, num2):  # constructor
        """
        Used to create the object and set the attributes of first and second number.
        @param num1: num1 is int and used as first number
        @param num2: num2 is int and used as second number
        """
        self.num1 = num1
        self.num2 = num2

    def addition(self):  # methods
        answer = self.num1 + self.num2
        print("SUM is : ", answer)

    def substraction(self):
        answer = self.num1 - self.num2
        print("DIFFERENCE is : ", answer)

    def multiplication(self):
        answer = self.num1 * self.num2
        print("MULTIPLICATIONS is : ", answer)

    def division(self, ):
        answer = self.num1 // self.num2
        print("DIVISION IS : ", answer)


class AdvanceCalculator(BasicCalculator):

    def negate(self):
        self.num1 = -1 * self.num1
        self.num2 = -1 * self.num2

    def reciprocal(self):
        self.num1 = 1 / self.num1
        self.num2 = 1 / self.num2

    def log(self):
        print("This function is applicable for num1")
        answer = math.log(self.num1)
        print(f'Log {self.num1} = {answer}')

    def squareroot(self):
        print("This function is applicable for num1")
        answer = math.sqrt(self.num1)
        print(f'Squareroot {self.num1} = {answer}')


class TrigonometryCalculator(AdvanceCalculator):

    def __degree_to_radain(self, degree):
        return degree * (math.pi / 180)

    def sinrad(self):
        print(f" {dir()} and {globals()}")
        print("This function is applicable for num1")
        answer = math.sin(self.__degree_to_radain(self.num1))
        print(f'Sine {self.num1} = {answer}')

    def cosrad(self):
        print("This function is applicable for num1")
        answer = math.cos(self.__degree_to_radain(self.num1))
        print(f'Cosine {self.num1} = {answer}')

    def tanrad(self):
        print("This function is applicable for num1")
        answer = math.tan(self.__degree_to_radain(self.num1))
        print(f'Tan {self.num1} = {answer}')


class ScientificCalculator(TrigonometryCalculator):
    pass


n1 = int(input('Enter the first number to add : '))
n2 = int(input('Enter the second number to add : '))
sc = ScientificCalculator(n1, n2)
# object instantiation
choice = ""

print('WELCOME TO MY CALCULATOR !!!')
while True:
    print('Here is list of choice : ')
    print('1 : ADD')
    print('2 : SUBTRACTION')
    print('3 : MULTIPLICATION')
    print('4 : DIVISION')
    print('5 : SIN RADIAN')
    print('6 : COS RADIAN')
    print('7 : TAN RADIAN')
    print('8 : LOG')
    print('9 : SQUAREROOT')
    print('10: EXIT')

    try:
        choice = int(input('Enter the number of your choice : '))
    except:
        print('Enter the valid number : ')
    if choice == 1:
        # n1 = int(input('Enter the first number to subtract : '))
        # n2 = int(input('Enter the second number to subtract : '))
        sc.addition()
    if choice == 2:
        # n1 = int(input('Enter the first number to subtract : '))
        # n2 = int(input('Enter the second number to subtract : '))
        sc.substraction()

    elif choice == 3:
        # n1 = int(input('Enter the first number to multiply : '))
        # n2 = int(input('Enter the second number to multiply : '))
        sc.multiplication()

    elif choice == 4:
        # n1 = int(input('Enter the first number to divide : '))
        # n2 = int(input('Enter the second number to divide : '))
        sc.division()

    elif choice == 5:
        # n = int(input('Enter the number to find its SINE in Rad : '))
        sc.sinrad()

    elif choice == 6:
        # n = int(input('Enter the number to find its COS in Rad : '))
        sc.cosrad()

    elif choice == 7:
        # n = int(input('Enter the number to find its TAN in Rad : '))
        sc.tanrad()

    elif choice == 8:
        # n = int(input('Enter the number to find its TAN in Rad : '))
        sc.log()

    elif choice == 9:
        sc.squareroot()

    elif choice == 10:
        print("Thank you for using Calculator!!!")
        break;
