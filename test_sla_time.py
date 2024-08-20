from sla_calculator import SLA_Calculator
import pendulum

sla_calc = SLA_Calculator(
    country_name="US",
    province="MO",
    state="MO",
    timezone="America/Chicago",
    open_hour=9,
    close_hour=17,
)


def test_sla_before_business_hours():
    # 1 AM start time on a business day
    start_time = pendulum.datetime(2022, 1, 3, 1, 0, 0, tz="America/Chicago")
    sla_time = sla_calc.calculate(start_time, minutes=60)
    # should be 10 AM the same day - 9am + 1 hour
    assert sla_time.isoformat() == "2022-01-03T10:00:00-06:00"


def test_sla_on_weekend():
    # 1 PM start time on a Saturday
    start_time = pendulum.datetime(2022, 1, 1, 13, 0, 0, tz="America/Chicago")
    sla_time = sla_calc.calculate(start_time, minutes=60)
    # should be 10 AM the following Monday - 9am + 1 hour
    assert sla_time.isoformat() == "2022-01-03T10:00:00-06:00"


def test_sla_on_holiday():
    # 1 PM start time on a holiday
    start_time = pendulum.datetime(2024, 1, 1, 13, 0, 0, tz="America/Chicago")
    sla_time = sla_calc.calculate(start_time, minutes=60)
    # should be 10 AM the following business day - 9am + 1 hour
    assert sla_time.isoformat() == "2024-01-02T10:00:00-06:00"


def test_not_enough_time_left():
    # 4 PM start time with 1 hour left in the day
    start_time = pendulum.datetime(2022, 1, 3, 16, 0, 0, tz="America/Chicago")
    sla_time = sla_calc.calculate(start_time, minutes=120)
    # should be 9 AM the following day - 9am + 1 hour
    assert sla_time.isoformat() == "2022-01-04T10:00:00-06:00"
