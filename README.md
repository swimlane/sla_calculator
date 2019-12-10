# SLA Calculator

## Installation
```
pip install sla-calculator
```
## Usage
To use this calculator, you must provide a starting time, the open time 
for business, the closing time for business, the country whose holidays
you observe, and the sla time in hours.  The function will then take
into account all holidays and weekends as none working hours, and return 
a pendulum object of the time the sla needs to be met by. The following
example will provide you with an SLA time 4 working hours from
12/10/2019 1:02:03 UTC
```
from sla_calculator import SLA_Calculator

sla_calc = SLA_Calculator()

sla_time = sla_calc.calculate(start_time="2019-12-10T01:02:03Z",
                              open_hour=9,
                              close_hour=17,
                              country_name="US",
                              sla_in_hours=4)
print(sla_time.to_iso8601_format())
```