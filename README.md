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
```python
from sla_calculator import SLA_Calculator

sla_calc = SLA_Calculator()

sla_time = sla_calc.calculate(start_time="2019-12-10T01:02:03Z",
                              open_hour=9,
                              close_hour=17,
                              country_name="US",
                              sla_in_hours=4)
print(sla_time.to_iso8601_string())
```

## Locale Specification
You can also specify the province or state that you are in to get a more
specific set of holidays:
```python
sla_time = sla_calc.calculate(start_time="2019-12-10T01:02:03Z",
                              open_hour=9,
                              close_hour=17,
                              country_name="US",
                              sla_in_hours=4,
                              state="CO")
```
Or:
```python
sla_time = sla_calc.calculate(start_time="2019-12-10T01:02:03Z",
                              open_hour=9,
                              close_hour=17,
                              country_name="Switzerland",
                              sla_in_hours=4,
                              province="Zurich")
```

## Run tests
Test are written for the pytest framework. Install it with:

    $ poetry install pytest
    
Run the tests with:

    $ poetry run pytest
