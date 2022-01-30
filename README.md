# Airignis

Hello World! First things first. Don't be confused by the name of this package. It comes from the pronunciation of the 
German word Ereignis meaning Event. The aim of this package is to provide a C# familiar way of handling events which I 
find quite comfortable. Additionally, it provides a so-called Auto Event class which allows to schedule the execution of
periodic tasks on different time bases (year, month, weak, day, hour, minute, second) with a high degree of practicability
and intuitiveness.

## Installation
```bash
$ pip3 install airignis
```

## How to use this package?
### Create an Event and add subscriber's callbacks

```python
from airignis import Event

def foo(data):
    print(f"doing something with the data: {data}")

# creating an Event object
my_event = Event()

# adding the foo() function as subscriber callback     
my_event += foo
```
After importing the Event class an object can be created. Following, one or multiple callback functions can be added with
the += operator.

### Invoke the Event and pass arguments to the callback 
```python
my_event.invoke(data)
```
The type and number of arguments of the subscriber callbacks must match with the data template accepted by the Event.

### Remove a subscriber's callback
```python
# removing the foo() function from the list of subscriber callbacks
my_event -= foo 
```

## Schedule an AutoEvent and set the function to be executed at each due time

This example shows a minimalistic usage of the AutoEvent class. Please refer to the package documentation for a 
detailed showcase of the functionalities.

```python
from airignis import AutoEvent, duetime
from datetime import datetime, timedelta


def say_hello(name: str):
    print(f"Hello {name}")


rate = 2
rate_unit = 'second'
exec_time = 20

# Specify the target due time
test_due_time = duetime(rate=rate, rate_unit=rate_unit)

# Defining the stop date time of the auto event. Should stop after 20 seconds
stop_datetime = datetime.now(test_due_time.timezone) + timedelta(seconds=exec_time)
auto_event = AutoEvent(say_hello, test_due_time, stop_datetime, 'world')

#  starting the auto event handler
auto_event.start()

#  Interrupting the auto event handler
auto_event.stop()
```

## Developing Airignis
To install airignis, along with the tools you need to develop and run tests, run the following in your virtualenv:
```bash
$ pip3 install -e .[dev]
``` 

## License

&copy; 2021 Subvael

This repository is licensed under the MIT license
See LICENSE for details


