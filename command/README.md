# Command Pattern

Inspired by <https://www.youtube.com/watch?v=9qA5kw8dcSU>

We're going to build Iot controllers for Philips Hue Lights and Danfoss Thermostats.
The Hue and Heater code is in seperate packages to indicate they are are library from vendor.

In the `iot.py` we'll build Commands and Invokers following the Command Pattern.
