from datetime import datetime


class Person:

    def __init__(self, name: str, surname: str, dob: datetime):
        """

        :rtype: object
        """
        self.name = name
        self.surname = surname
        self.date_of_birth = dob
        self._age = self.__calculate_age()

    def __calculate_age(self):
        delta = datetime.now() - self.date_of_birth
        print(delta)
        print(type(delta))
        return f"Your age in {delta.days // 365} years"
        # return (datetime.now() - self.date_of_birth) // 365

    def get_age(self):
        print(f"the type of age is {type(self._age)}")
        return self._age

    """
    # TODO :- Add your understanding. 
    
    def __str__(self):
        print(f"In class, Name is {self.name}, surname is {self.surname} and age is {self._age} ")
        return ""
    """

    def __str__(self):
        return f"In class, Name is {self.name}, surname is {self.surname} and age is {self._age}"