class Employee:
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title


employees = [
    Employee('Vera', 2000, 'Manager'),
    Employee('Chuck', 1800, 'Attendant'),
    Employee('Samantha', 1800, 'Attendant'),
    Employee('Roberto', 2100, 'Cook'),
    Employee('Joe', 2000, 'Car Repair'),
    Employee('Dave', 2200, 'Car Repair'),
    Employee('Tina', 2300, 'Car Repair'),
]

for e in employees:
    print(f'{e.name}, ${e.salary}, {e.title}')
