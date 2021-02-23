from calendar import HTMLCalendar, month_name

from projects_and_tasks.models import Task


class Calendar(HTMLCalendar):
    def __init__(self, user, year=None, month=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    def format_day(self, day, tasks):
        tasks_in_day = tasks.filter(deadline__day=day)
        d = ''
        for task in tasks_in_day:
            d += f'{task.get_html_url}'
        if day != 0:
            return f"<td><p class='date'>{day}</p>{d}</td>"
        return '<td></td>'

    def format_week(self, the_week, tasks):
        week = ''
        for d, weekday in the_week:
            week += self.format_day(d, tasks)
        return f'<tr> {week} </tr>'

    def format_month_name(self, year, month):
        s = '%s %s' % (month_name[month], year)
        return '<tr><th colspan="7" class="text-center">%s</th></tr>' % s

    def format_month(self, with_year=True):
        tasks = Task.objects.filter(
            deadline__year=self.year,
            deadline__month=self.month,
            project__owner__user=self.user
        )
        cal = f'<table class="table table-sm table-bordered bg-primary text-light">\n'
        cal += f'{self.format_month_name(self.year, self.month)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week, tasks)}\n'
        cal += f'</table>'
        return cal
