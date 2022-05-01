from Person import Person
import datetime

if __name__ == "__main__":
    dob = datetime.datetime(1993, 6, 19, 0, 0, 0, 0, None)
    print(dob)
    person = Person("Parag", "Gunjal", dob)
    print(person)
    print(person.get_age())
    # datetime.datetime.

