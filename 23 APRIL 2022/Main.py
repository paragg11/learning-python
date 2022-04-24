import datetime

from oop.experiences.experience import Experience
from oop.experiences.person import Person

if __name__ == "__main__":
    print("This is to check the system is setup fine")


    start_date = datetime.datetime(2019, 4, 1)
    end_date = datetime.datetime(2020, 2, 1)
    exp1 = Experience(start_date,end_date,"ICICI","BSM",False)

    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2022, 2, 2)
    exp2 = Experience(start_date,end_date,"Big basket","Executive",False)

    start_date = datetime.datetime(2022, 3, 2)
    end_date = datetime.datetime(2022, 3, 2)
    exp3 = Experience(start_date,end_date,"Spark Eighteen","Intern",True)
    #
    # parag = Person("Parag")
    # parag.add_experience(exp1)
    # parag.add_experience(exp2)
    # parag.add_experience(exp3)
    #parag.add_experience("Abrar")


    print(sum(exp1,2))
    print(sum("ab","rar"))
    #print(parag.get_total_experience_in_years())
    #print(parag.get_total_experience_in_months())
    print(f"Parag experience in days is {parag.get_total_experience_in_days()}")
    print(f"Parag experience in months is {parag.get_total_experience_in_months()}")
    print(f"Parag experience in years is {parag.get_total_experience_in_years()}")
    exp4 = Experience()
    print(exp1)
    print(exp2)
    print(exp3)
    print(exp4)
