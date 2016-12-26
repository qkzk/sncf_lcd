#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import sched

# on défini un programmateur temporel (?) = scheduler
s = sched.scheduler(time.time, time.sleep)

# on converti l'horaire au bon format
# "20161226T19290000"
# vers
# 1482776940.014
def conversion_horaire(str):
    str_tuple = (int(str[0:4]),int(str[4:6]),int(str[6:8]),int(str[9:11]),int(str[11:13]), int(str[13:15]))
    # print(str_tuple)
    str_datetime = datetime.datetime(*str_tuple)
    # print(str_datetime)
    str_mktime = time.mktime(str_datetime.timetuple())
    # print(str_mktime)
    return str_mktime

# l'evenement qui sera execute a l'heure dite
def event_response():
    print("et c'est parti ! ",time.time())

# l'attente et la reponse (il sleep() entre les deux)
# si le time est dans le passé il s'exécute immediatement
def waittilltime(str):
    print("on attend a partir de : ",time.time())
    lancement = conversion_horaire(str)
    s.enterabs(lancement, 1, event_response, ())
    s.run()
    print(time.time())
    print("fini")


if __name__ == '__main__':
    # ici on a récupéré une date au format '20161226T13381800'
    horaire = "20161226T19340000"
    waittilltime(horaire)
