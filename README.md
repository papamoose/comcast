Comcast
-------
Originally written by Eric Swanson and modified to work as a python class.
It returns a hash with all data Comcast is willing to divulge.

The example script shows you how to might deal with this information
to check your quota.


Comcast has recently implemented a data cap in my area. I wanted to track their
view of my usage so I could compare it with my vnstat logs. This Python script
(`comcast.py`) will dump a JSON blob with usage information. The included bash
script (`comcast.sh`) uses that data to write to a local statsd/graphite
installation.

The only requirement for the Python script is the requests library.

Usage
-----
```bash
COMCAST_USERNAME=bob COMCAST_PASSWORD=hope python3 example.py
```
