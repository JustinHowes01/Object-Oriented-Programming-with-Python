class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.salary = int(salary)


class Manager(Employee):
    job_title = "Manager"


class Cook(Employee):
    job_title = "Cook"


class Attendant(Employee):
    job_title = "Station Attendant"


class Mechanic(Employee):
    job_title = "Mechanic"
