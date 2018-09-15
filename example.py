#!/usr/bin/env python3
from json import dumps
from os import environ
from ComcastData.ComcastData import ComcastData

userdata = ComcastData(environ['COMCAST_USERNAME'], environ['COMCAST_PASSWORD'])

js = userdata.get()

used = js['usageMonths'][-1]['homeUsage']
total = js['usageMonths'][-1]['allowableUsage']
unit = js['usageMonths'][-1]['unitOfMeasure']

ret = {
  "used" : int(used),
  "total" : int(total),
  "unit" : unit
}

print(dumps(ret))
