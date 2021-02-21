from calendar import HTMLCalendar

from projects_and_tasks.models import Task


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
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

    def format_month(self, with_year=True):
        tasks = Task.objects.filter(deadline__year=self.year, deadline__month=self.month)
        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=with_year)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week, tasks)}\n'
        cal += f'</table>'
        return cal
