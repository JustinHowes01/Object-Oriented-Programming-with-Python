from employee import Manager, Attendant, Cook, Mechanic
from reporting import AccountingReport, StaffingReport

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

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
]

for r in reports:
    r.print_report()
    print()  # empty line
