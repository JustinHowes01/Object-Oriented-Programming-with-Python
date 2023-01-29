class Employee:
    def __init__(self, first_name, last_name, salary, shift):
        self._first_name = first_name  # The underscore indicates that these are not to be accessed (Encapsulation)
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self):
        return f'{self._first_name} {self._last_name}'


class Manager(Employee):
    job_title = "Manager"


class Cook(Employee):
    job_title = "Cook"


class Attendant(Employee):
    job_title = "Station Attendant"


class Mechanic(Employee):
    job_title = "Mechanic"
