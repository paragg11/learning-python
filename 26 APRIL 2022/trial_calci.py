import math
class Calculator:

    def __init__(self, degree, first_number, second_number, x):
        self.degree = degree
        self.first_number = first_number
        self.second_number = second_number
        self.x = x

    def addition(self):
        answer = self.first_number + self.second_number
        #print('Sum = ',answer)
        return answer

    def substract(self):
        answer = self.first_number - self.second_number
        #print('Difference = ',answer)
        return answer

    def multiplication(self, first_number, second_number):
        answer = self.first_number * self.second_number
        #print('Product = ',answer)
        return answer

    def division(self, first_number, second_number):
        answer = self.first_number / self.second_number
        #print('Quotient = ',answer)
        return answer

    def sinrad(self):
        answer = math.sin(self.degree)
        #print("Sine (%f) = %f" %(num,answer))
        return answer

    def cosrad(self):
        answer = math.cos(self.degree)
        #print("Cosine(%f) = %f" %(num,answer))
        return answer

    def tanrad(self):
        answer = math.tan(self.degree)
        #print("Tan(%f) = %f" %(num,answer))
        return answer

    def cosecrad(self):
        answer = 1/(math.sin(self.degree))
        #print("Sine(%f = %f" %(num,answer))
        return answer

    def secrad(self):
        answer = 1/(math.cos(self.degree))
        #print("Sec(%f) = %f" %(num,answer))
        return answer

    def cotrad(self):
        answer = 1/(math.tan(self.degree))
        #print("Cot(%f) = %f" %(num,answer))
        return answer

    def sindeg(self):
        answer = math.sin(math.radians(self.degree))
        #print("Sin(%f) in degrees = %f" %(num,answer))
        return answer

    def cosdeg(self):
        answer = math.cos(math.radians(self.degree))
       # print("Cos(%f) in degrees = %f" %(num,answer))
        return answer

    def tandeg(self):
        answer = math.tan(math.radians(self.degree))
        #print("Tan(%f) in degrees = %f" %(num,answer))
        return answer

    def cosecdeg(self):
        answer = 1/(math.sin(math.radians(self.degree)))
        #print("Cosec(%f) in degrees = %f" %(num,answer))
        return answer

    def secdeg(self):
        answer = 1/(math.cos(math.radians(self.degree)))
        #print("Sec(%f) in degrees = %f" %(num,answer))
        return answer

    def cotdeg(self):
        answer = 1/(math.tan(math.radians(self.degree)))
        #print("Cot(%f) in degrees = %f" %(num,answer))
        return answer

    def ln(self):
        answer = math.log(self.degree)
        #print("ln(%f) = %f" %(num,answer))
        return answer

    def logten(self):
        answer = math.log10(self.degree)
        #print("log10(%f) = %f" %(num,answer))
        return answer

    def logbasex(self):
        answer = math.log(self.degree, self.x)
        #print("log base(%f)(%f) = %f" %(x,num,answer))
        return answer

    def squareroot(self):
        answer = math.sqrt(self.first_number)
        #print("Square Root(%f) = %f " %(num,answer))
        return answer

    # def pie(self):
    #     print( 'pi = ',math.pi)
    #
    # def powerof(self,num,raiseby):
    #     answer = math.pow(num,raiseby)
    #     print("%f ^ (%f) = %f" %(num,raiseby,answer) )

