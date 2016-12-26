#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime as dt

d = dt.datetime.today() # 2016-12-26 13:38:18.464000
print(d)

j = dt.datetime.today().weekday() # le jour de la semaine à partir de lundi = 0
print(j)

n = time
nf = n.strftime("%Y%m%dT%H%M%S00") #20161226T13381800
print(nf)

depart_dans = dt.timedelta(hours=1)

import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.time()


def print_some_times():
    print time.time()
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    s.run()
    print time.time()

print_some_times()


#dt.timedelta.total_seconds()
