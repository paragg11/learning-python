import math

def circle(radius):
    """Compute and return area of a circle"""
    return math.pi * radius**2

def cylinder(radius, height):
    """ Compute and return the surface area of a cylinder"""
    circle_area = circle(radius)
    height_area =  2 * radius * math.pi * height
    return 2*circle_area + height_area

def sphere(radius):
    """Compute and return the surface area of sphere"""
    return 4 * math.pi * radius**2