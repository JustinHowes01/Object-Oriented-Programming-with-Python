from employee import Manager, Attendant, Cook, Mechanic

employees = [
    Manager('Vera', 'Scmidt', 2000),
    Attendant('Chuck', 'Norris', 1800),
    Attendant('Samantha', 'Carrington', 1800),
    Cook('Roberto', 'Jacketti', 2100),
    Mechanic('Dave', 'Dreibig', 2000),
    Mechanic('Tina', 'River', 2200),
    Mechanic('Ringo', 'Rama', 2300),
    Mechanic('Chuck', 'Rainey', 1800)
]


def print_accounting_report():
    print('Accounting\n==========')
    for e in employees:
        print(f'{e.first_name} {e.last_name}, ${e.salary}')


def print_staffing_report():
    print('Staffing\n========')
    for e in employees:
        print(f'{e.first_name} {e.last_name}, {e.job_title}')


print_accounting_report()
print()  # empty line
print_staffing_report()
