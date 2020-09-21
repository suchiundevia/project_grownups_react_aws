from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Activity


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, activities):
        activities_per_day = activities.filter(activity_start_time__day=day)
        d = ''
        for activity in activities_per_day:
            d += f'<li> {activity.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, activities):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, activities)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        activities = Activity.objects.filter(activity_start_time__year=self.year, activity_start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, activities)}\n'
        return cal
