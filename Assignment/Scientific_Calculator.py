import math
#from re import T 

class Calculator:
        
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        answer = self.num1 + self.num2
        print("SUM is : ", answer)
    
    def substraction(self):
        answer = self.num1 - self.num2
        print("DIFFERENCE is : ", answer)
    
    def multiplication(self):
        answer = self.num1 * self.num2
        print("MULTIPLICATIONS is : ", answer)
    
    def division(self,):
        answer = self.num1 // self.num2
        print("DIVISION IS : ", answer)
        
    def sinrad(self):
        print("This function is applicable for num1")
        answer = math.sin(self.num1)
        print(f'Sine {self.num1} = {answer}')
        
    def cosrad(self):
        print("This function is applicable for num1")
        answer = math.cos(self.num1)
        print(f'Cosine {self.num1} = {answer}')
        
    def tanrad(self):
        print("This function is applicable for num1")
        answer = math.tan(self.num1)
        print(f'Tan {self.num1} = {answer}')


n1 = int(input('Enter the first number to add : '))
n2 = int(input('Enter the second number to add : '))
calc = Calculator(n1,n2)            
choice = ""

while True:
    print('WELCOME TO MY CALCULATOR !!!')
    print('Here is list of choice : ')
    print('1 : ADD')
    print('2 : SUBTRACTION')
    print('3 : MULTIPLICATION')
    print('4 : DIVISION')
    print('5 : SIN RADIAN')
    print('6 : COS RADIAN')
    print('7 : TAN RADIAN')
    print('8 : EXit')
    try:
        choice = int(input('Enter the number of your choice : '))
    except:
        print('Enter the valid number : ')        
    if choice == 1:
        # n1 = int(input('Enter the first number to subtract : '))
        # n2 = int(input('Enter the second number to subtract : '))
        calc.addition()
    if choice == 2:
        # n1 = int(input('Enter the first number to subtract : '))
        # n2 = int(input('Enter the second number to subtract : '))
        calc.substraction()
        
    elif choice == 3:
        # n1 = int(input('Enter the first number to multiply : '))
        # n2 = int(input('Enter the second number to multiply : '))
        calc.multiplication()
        
    elif choice == 4:
        # n1 = int(input('Enter the first number to divide : '))
        # n2 = int(input('Enter the second number to divide : '))
        calc.division()
        
    elif choice == 5:
        # n = int(input('Enter the number to find its SINE in Rad : '))
        calc.sinrad()
             
    elif choice == 6:
        # n = int(input('Enter the number to find its COS in Rad : '))
        calc.cosrad() 
    
    elif choice == 7:
        # n = int(input('Enter the number to find its TAN in Rad : '))
        calc.tanrad()
    elif choice == 8:
        # n = int(input('Enter the number to find its TAN in Rad : '))
        print("Thanks for using this calulator")
        break; 
    
    
        
    