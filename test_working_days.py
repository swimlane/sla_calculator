import pendulum
from sla_calculator import SLA_Calculator

holiday_date = pendulum.datetime(2022, 1, 3, tz="America/Chicago")
weekend_start_time = pendulum.datetime(2022, 1, 1, 9, 0, 0, tz="America/Chicago")
working_start_time = pendulum.datetime(2022, 1, 4, 9, 0, 0, tz="America/Chicago")
sla_calc = SLA_Calculator(holidays=[holiday_date.date()], timezone="America/Chicago")


def test_is_working_day():
    start_time = working_start_time
    assert sla_calc._is_working_day(start_time) is True
    assert sla_calc._is_weekend(start_time) is False
    assert sla_calc._is_holiday(start_time) is False


def test_is_weekend():
    start_time = weekend_start_time
    assert sla_calc._is_working_day(start_time) is False
    assert sla_calc._is_weekend(start_time) is True
    assert sla_calc._is_holiday(start_time) is False


def test_is_holiday():
    start_time = holiday_date
    sla_calc.holidays = [start_time.date()]
    assert sla_calc._is_working_day(start_time) is False
    assert sla_calc._is_holiday(start_time) is True
    assert sla_calc._is_weekend(start_time) is False


def test_check_working_days():
    start_time = holiday_date
    start_time = sla_calc.check_working_days(start_time)
    assert sla_calc._is_working_day(start_time) is True
    assert sla_calc._is_weekend(start_time) is False
    assert sla_calc._is_holiday(start_time) is False
    # go past two weekend days and the holiday on the 3rd
    assert start_time == pendulum.datetime(
        2022, 1, 4, 9, 0, 0, tz=pendulum.local_timezone()
    )
