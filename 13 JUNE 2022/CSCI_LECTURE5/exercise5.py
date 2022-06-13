"""
Lecture 5 - Python Functions
"""
if __name__ == "__main__":

    print("*" * 100)
    """
    A function to compute area of a circle.
    """
    def area_circle(radius):
        pi = 3.14159
        area = pi * radius **2
        return area

    a = area_circle(1)
    print(a)
    print('A circle with radius 2 has area {:.2f}'.format(area_circle(2)))
    r = 75.1
    a = area_circle(r)
    print("A circle with radius {:.2f} has area {:.2f}".format(r, a))

    print("*" * 100)
    """
    Computing the surface area of a cylinder using two functions. 
    """
    import math

    def area_circle(radius):
        return math.pi * radius ** 2

    def area_cylinder(radius, height):
        circle_area = area_circle(radius)
        height_area = 2 * radius * math.pi * height
        return 2 * circle_area + height_area

    print('The area of a circle of radius 1 is', round(area_circle(1), 2))
    r = 2
    height = 10
    print('The surface area of a cylinder with radius', r)
    print('and height', height, 'is', round(area_cylinder(r, height), 2))

    print("*" * 100)
    """
    Write a function that computes the area of a rectangle. 
    Then, write a second function that calls this function three times 
    to compute the surface area of a rectangular solid.
    """
    def area_rectangle(length, breadth):
        area = length * breadth
        return area

    def get_surface_area(length, breadth, height):
        area1 = area_rectangle(length, breadth)
        area2 = area_rectangle(length, height)
        area3 = area_rectangle(height, breadth)
        surface_area = 2 * (area1 + area2 + area3)
        return surface_area

    a = get_surface_area(40, 20, 20)
    print(a)

    print("*" * 100)
    """
    Write a function that returns the middle value among three integers. 
    (Hint: make use of min() and max()). Write code to test this function with different inputs.
    """

    def get_middle_value(num1, num2, num3):
        if num2 > num1 > num3 or num3 > num1 > num2:
            middle_number = num1
        elif num1 > num2 > num3 or num3 > num2 > num1:
            middle_number = num2
        else:
            middle_number = num3
        return middle_number

    a = get_middle_value(10, 20, 30)
    print(f'Middle number is :', a)

    print("*" * 100)
    """
    Functions: Write the functions from class on your own using the Python interpreter. 
    Try to do it without looking at notes. Can you do it?

    Write a function that returns a value.
    Write a function with no return.
    Write a function where return is not the last statement in the function.
    Call these functions by either printing their result or assigning their results to a value. 
    Here, I’ll get you started.
    """

    def regenerate_doctor(doctor_number):
        return doctor_number + 1

    def regenerate_tardis(doctor_number):
        print("Tardis is now ready for doctor number", doctor_number)

    def eliminate_doctor(doctor_number):
        return 0
      #  print("You will be eliminated doctor", doctor_number)

    print("*" * 100)
    """
    Write a function called convert2fahren that takes a Celsius temperature and converts it to Fahrenheit, 
    returning the answer. 
    Write code that calls the function three times to convert temperatures 0, 32, and 100 to Fahrenheit, 
    printing the result each time. 
    To keep things simple for these exercises, the output should be
    0 -> 32.0
    32 -> 89.6
    100 -> 212.0
    """

    def convert2fahren(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    a = convert2fahren(0)
    print(f'Celsius to Fahrenheit is: ', a)
    a = convert2fahren(32)
    print(f'Celsius to Fahrenheit is: ', a)
    a = convert2fahren(100)
    print(f'Celsius to Fahrenheit is: ', a)

    print("*" * 100)
    """
    Write a function called frame_string that takes a string as an argument. 
    Its job is to print that string with a frame around it, just like in Lab 2. 
    Unlike the other functions we have written frame_string does not need and 
    therefore should not have a return statement. 
    Write code to call the function two times. 
    For the first call pass the string Spanish Inquisition. 
    For the second call, pass the string Ni. 
    Print a blank line between calls. The output should be
    
    """
    def frame_string(string):
        print(f'{string}')


    a = frame_string('** Spanish Inquisition **')
    print("*" * 50)
    #print(a)

    a = frame_string('** Ni **')
    print("*" * 50)
    #print(a)



