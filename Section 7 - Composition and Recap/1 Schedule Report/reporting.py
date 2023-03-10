class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list


class AccountingReport(Report):
    def print_report(self):
        print('Accounting\n==========')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, ${e.salary}')


class StaffingReport(Report):
    def print_report(self):
        print('Staffing\n========')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, {e.job_title}')


class ScheduleReport(Report):
    def print_report(self):
        print('Hours\n=====')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, {e.start_time:%H:%M} to {e.end_time:%H:%M}')
