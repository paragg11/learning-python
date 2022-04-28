import math

class BasicCalculator:

    def __init__(self, first_number, second_number):
        """
        Constructs all the necessary attributes for the Basic Calculator object.
        :param first_number: takes first number as input for Basic Calculator
        :param second_number: takes second number as input for Basic Calculator

        """

        self.first_number = first_number
        self.second_number = second_number

    def __str__(self):
        """

        :return: This is the docstring for this method.
        It describes what the method does, what are its calling conventions and
        what are its side effects
        """
        return f"In Basic Calculator, two numbers are {self.first_number} and {self.second_number}"


    def do_addition(self):
        """

        :return: return argument answer returns the sum of two attributes
        """
        answer = self.first_number + self.second_number
        #print('Sum = ',answer)
        return answer

    def do_substraction(self):
        """

        :return: return argument answer returns the difference of two attributes
        """
        answer = self.first_number - self.second_number
        #print('Difference = ',answer)
        return answer

    def do_multiplication(self):
        """

        :return: return argument answer returns the multiplication of two attributes.
        """
        answer = self.first_number * self.second_number
        #print('Product = ',answer)
        return answer

    def do_division(self):
        """

        :return: return argument answer returns the division of two attributes.
        """
        answer = self.first_number / self.second_number
        #print('Quotient = ',answer)
        return answer

class TrigonometricCalulator(BasicCalculator):

    def __init__(self,first_number, second_number, radian, degree):
        """

        :param radian: takes radian attribute as input for Trigonometric Calculator
        :param degree: takes degree attribute as input for Trigonometric Calculator
        """
        self.radian = radian
        self.degree = degree
        super().__init__(first_number,second_number)
        """
        the super function can be used to gain access to inherited methods – from a parent or sibling class – that has been overwritten in a class object.
        """

    def __str__(self):
        """

        :return: This is the docstring for this method.
        It describes what the method does, what are its calling conventions and
        what are its side effects
        """
        return f"In Trigonometric Calculator, value of radian is {self.radian} and degree is {self.degree}"

    # def __degree_to_radain(self, degree):
    #     return degree * (math.pi / 180)

    # def sine_radian(self):
    #
    #     answer = math.sin(self.__degree_to_radain( self.radian))
    #     #print("Sine (%f) = %f" %(num,answer))
    #     return answer

    def get_sine_radian(self):

        """
        :return: return argument answer returns the sine value of given radian
        """
        answer = math.sin(math.radians( self.radian))
         #print("Sine (%f) = %f" %(num,answer))
        return answer

    def get_cosine_radian(self):
        """

        :return: return argument answer returns the cosine value of given radian
        """

        answer = math.cos(math.radians(self.radian))
        #print("Cosine(%f) = %f" %(num,answer))
        return answer

    def get_tangent_radian(self):
        """

        :return: return argument answer returns the tangent value of given radian
        """
        answer = math.tan(math.radians(self.radian))
        #print("Tan(%f) = %f" %(num,answer))
        return answer

    def get_cosecant_radian(self):
        """

        :return: return argument answer returns the coscecant value of given radian
        """
        answer = 1/(math.sin(math.radians(self.radian)))
        #print("Sine(%f = %f" %(num,answer))
        return answer

    def get_secant_radian(self):
        """

        :return: return argument answer returns the secant value of given radian
        """

        answer = 1/(math.cos(math.radians(self.radian)))
        #print("Sec(%f) = %f" %(num,answer))
        return answer

    def get_cotangent_radian(self):
        """

        :return: return argument answer returns the cotagent value of given radian
        """
        answer = 1/(math.tan(math.radians(self.radian)))
        #print("Cot(%f) = %f" %(num,answer))
        return answer

    def get_sine_degree(self):
        """

        :return: return argument answer returns the sine value of given degree
        """
        answer = math.sin(math.degrees(self.degree))
        #print("Sin(%f) in degrees = %f" %(num,answer))
        return answer

    def get_cosine_degree(self):
        """

        :return: return argument answer returns the cosine value of given degree
        """
        answer = math.cos(math.degrees(self.degree))
       # print("Cos(%f) in degrees = %f" %(num,answer))
        return answer

    def get_tangent_degree(self):
        """

        :return: return argument answer returns the tangent value of given degree
        """
        answer = math.tan(math.degrees(self.degree))
        #print("Tan(%f) in degrees = %f" %(num,answer))
        return answer

    def get_cosecant_degree(self):
        """

        :return: return argument answer returns the cosecant value of given degree
        """
        answer = 1/(math.sin(math.degrees(self.degree)))
        #print("Cosec(%f) in degrees = %f" %(num,answer))
        return answer

    def get_secant_degree(self):
        """

        :return: return argument answer returns the secant value of given degree
        """
        answer = 1/(math.cos(math.degrees(self.degree)))
        #print("Sec(%f) in degrees = %f" %(num,answer))
        return answer

    def get_cotangent_degree(self):
        """

        :return: return argument answer returns the cotangent value of given degree
        """
        answer = 1/(math.tan(math.degrees(self.degree)))
        #print("Cot(%f) in degrees = %f" %(num,answer))
        return answer

class AdvancedCalculator(TrigonometricCalulator):

    def __init__(self,first_number, second_number, radian, degree, x):
        """

        :param x: takes x attribute as input for Advanced Calculator
        """
        self.x = x
        super().__init__(first_number,second_number,degree,radian)
        """
        the super function can be used to gain access to inherited methods – from a parent or sibling class – that has been overwritten in a class object.

        """

    def __str__(self):
        """

        :return: This is the docstring for this method.
        It describes what the method does, what are its calling conventions and
        what are its side effects
        """

        return  f"In Advanced Calculator and the value of x is {self.x}!!!"

    def get_log_ten(self):
        """

        :return: return argument answer means base ten log
        """
        answer = math.log10(self.x)
        #print("log10(%f) = %f" %(num,answer))
        return answer
    def get_square_root(self):
        """

        :return: return argument answer i.e. square root of the mean square
        """
        answer = math.sqrt(self.x)
        #print("Square Root(%f) = %f " %(num,answer))
        return answer


    #TODO - Unittest
    #TODO - Run all options together - DONE
    #TODO - README 
    #TODO - MULTI LEVEL INHERITANCE - DONE
    #TODO - change method names from nouns to verbs/action phrases - DONE
    #TODO - DOC STRING - DONE