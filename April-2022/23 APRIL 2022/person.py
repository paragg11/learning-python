import datetime

import experience


class Person:

    def __init__(self, name: str):
        self.name = name
        self._list_of_experience = []
        self._total_experience_in_months = 0
        self._total_experience_in_years = 0
        self._total_experience_in_days = 0

    def get_total_experience_in_years(self):
        return self._total_experience_in_days // 365

    def get_total_experience_in_months(self):
        return self._total_experience_in_days // 30

    def get_total_experience_in_days(self):
        return self._total_experience_in_days

    def add_experience(self, exp: experience.Experience = None):
        # TODO :_Check the type of the object
        # print(type(experience))
        # if type(experience) != oop.experiences.experience.Experience:
        #     raise NameError("Please pass the experience object")
        if not isinstance(exp, experience.Experience):
            raise ValueError("Please pass the experience object")
        self._list_of_experience.append(exp)
        if not exp.is_present:
            self._total_experience_in_days = self._total_experience_in_days + self._calculate_experience_days(
                exp)
        else:
            delta = datetime.datetime.now() - exp.start_date
            self._total_experience_in_days = self._total_experience_in_days + delta.days
        # self._total_experience_in_years = self._total_experience_in_years + self._calculate_experience_year(experience)
        # self._total_experience_in_months = self._total_experience_in_months + self._calculate_experience_month(experience)

    def _calculate_experience_month(self, experience: experience.Experience = None):
        if not isinstance(experience, experience.Experience):
            raise NameError("Please pass the experience object")
        delta = experience.end_date - experience.start_date
        print(delta)
        # return 0
        return delta.days // 30

    def _calculate_experience_year(self, experience: experience.Experience = None):
        if not isinstance(experience, experience.Experience):
            raise NameError("Please pass the experience object")
        delta = experience.end_date - experience.start_date
        print(delta)
        # return 0
        return delta.days // 365

    def _calculate_experience_days(self, experience):
        delta = experience.end_date - experience.start_date
        # print(experience.company_name)
        # print(delta)
        # print(delta.days)
        return delta.days

    def currently_in_which_company(self):
        for i in self._list_of_experience:
            if i.is_present:
                return i.company_name
