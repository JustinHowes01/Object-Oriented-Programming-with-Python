from employee import Manager, Attendant, Cook, Mechanic
from reporting import AccountingReport, StaffingReport, ScheduleReport
from shift import MorningShift, AfternoonShift, NightShift

employees = [
    Manager('Vera', 'Scmidt', 2000, MorningShift()),
    Attendant('Chuck', 'Norris', 1800, MorningShift()),
    Attendant('Samantha', 'Carrington', 1800, AfternoonShift()),
    Cook('Roberto', 'Jacketti', 2100, MorningShift()),
    Mechanic('Dave', 'Dreibig', 2000, MorningShift()),
    Mechanic('Tina', 'River', 2200, MorningShift()),
    Mechanic('Ringo', 'Rama', 2300, AfternoonShift()),
    Mechanic('Chuck', 'Rainey', 1800, NightShift())
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()  # empty line
