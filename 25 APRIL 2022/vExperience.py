import datetime


class Experience:
    """
        duration: years/months
        start_date
        end_date
        company
        position
    """

    def __init__(self, start_date, end_date, company, position):
        self.start_date = start_date if (isinstance(start_date, datetime.datetime)) else None
        self.end_date = end_date if (isinstance(end_date, datetime.datetime)) else None
        self.company = company
        self.position = position
        self.duration = self._calculate_duration()

    def _calculate_duration(self):
        if (self.start_date is None) or (self.end_date is None) or (self.end_date < self.start_date):
            self.duration = 0
            print(f"Invalid end & start dates: start_date: {self.start_date}, end_date: {self.end_date}")
        self.duration = self.end_date - self.start_date