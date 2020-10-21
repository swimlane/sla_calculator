from sla_calculator import SLA_Calculator


def test_sla_time():
    sla_calc = SLA_Calculator()

    sla_time = sla_calc.calculate(start_time="2019-12-10T01:02:03Z",
                                  open_hour=9,
                                  close_hour=17,
                                  country_name="US",
                                  sla_in_hours=4)
    assert sla_time.to_iso8601_string() == '2019-12-10T13:00:00-08:00'
