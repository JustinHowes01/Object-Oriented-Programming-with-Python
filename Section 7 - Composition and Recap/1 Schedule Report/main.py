from employee import Manager, Attendant, Cook, Mechanic
from reporting import AccountingReport, StaffingReport, ScheduleReport
from datetime import time

employees = [
    Manager('Vera', 'Scmidt', 2000, time(8, 00), time(14, 00)),
    Attendant('Chuck', 'Norris', 1800, time(8, 00), time(14, 00)),
    Attendant('Samantha', 'Carrington', 1800, time(12, 00), time(20, 00)),
    Cook('Roberto', 'Jacketti', 2100, time(8, 00), time(14, 00)),
    Mechanic('Dave', 'Dreibig', 2000, time(8, 00), time(14, 00)),
    Mechanic('Tina', 'River', 2200, time(8, 00), time(14, 00)),
    Mechanic('Ringo', 'Rama', 2300, time(12, 00), time(20, 00)),
    Mechanic('Chuck', 'Rainey', 1800, time(12, 00), time(20, 00))
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()  # empty line
