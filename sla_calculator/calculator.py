import pendulum
import holidays as pyholidays


class SLA_Calculator(object):
    def __init__(self):
        pass

    def check_working_days(self, start_time, country_holidays, open_hour):
        while start_time in country_holidays:
            start_time = start_time.add(days=1)
            start_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, open_hour, 0, 0,
                                           tzinfo=pendulum.local_timezone())
        while start_time.is_weekend():
            start_time = start_time.add(days=1)
            start_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, open_hour, 0, 0,
                                           tzinfo=pendulum.local_timezone())
        return start_time

    def calculate(self, start_time, open_hour, close_hour, country_name='US', sla_in_hours=4, province=None,
                  state=None):
        sla_time = None
        sla_in_minutes = sla_in_hours * 60
        start_time = start_time if isinstance(start_time, pendulum.Pendulum) else pendulum.parse(start_time)

        country_holidays = pyholidays.CountryHoliday(country_name, prov=province, state=state)
        start_time = self.check_working_days(start_time, country_holidays, open_hour)

        open_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, open_hour,
                                      0, 0, tzinfo=pendulum.local_timezone())
        close_time = pendulum.datetime(start_time.year, start_time.month, start_time.day,
                                       close_hour, 0, 0, tzinfo=pendulum.local_timezone())
        if start_time < open_time:
            start_time = open_time
        elif start_time > close_time:
            start_time = open_time.add(days=1)
            open_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, open_hour, 0, 0,
                                          tzinfo=pendulum.local_timezone())
            close_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, close_hour, 0, 0,
                                           tzinfo=pendulum.local_timezone())

        time_left_today = start_time.diff(close_time).in_minutes()
        if time_left_today >= sla_in_minutes:
            sla_time = start_time.add(minutes=sla_in_minutes)
        else:
            tomorrow_minutes = sla_in_minutes - time_left_today
            start_time = open_time.add(days=1)
            while tomorrow_minutes > time_left_today:
                start_time = self.check_working_days(start_time, country_holidays, open_hour)
                open_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, open_hour, 0, 0,
                                              tzinfo=pendulum.local_timezone())
                close_time = pendulum.datetime(start_time.year, start_time.month, start_time.day, close_hour, 0, 0,
                                               tzinfo=pendulum.local_timezone())
                time_left_today = start_time.diff(close_time).in_minutes()
                if time_left_today >= sla_in_minutes:
                    sla_time = start_time.add(minutes=tomorrow_minutes)
                    break
                else:
                    tomorrow_minutes = tomorrow_minutes - time_left_today
                    start_time = open_time.add(days=1)
            if not sla_time:
                sla_time = start_time.add(minutes=tomorrow_minutes)

        return sla_time
