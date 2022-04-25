from oop.experiences import vExperience


class Person:
    """
        Person's personal details - name, age, address, gender, phonenumber
    """
    def __init__(self, name, age, address, gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.experiences = list()

    def __str__(self):
        return f"{self.name}, {self.gender} with age {self.age} lives in/at {self.address}"

    def add_experience(self, experience: vExperience.Experience):
        self.experiences.append(exper ience)



if __name__ == '__main__':
    vishal = Person("Vishal", 28, "Pune", "Male")
    print(vishal)