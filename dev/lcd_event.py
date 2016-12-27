#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ABANDONNE

tout a ete concentre dans calendrier.py, le seul truc a lancer tous les jours a minuit et au bout
'''



'''
le principe est :
* se lancer à 0h00 tous les jours
* s'il y a cours : récupérer l'horaire du train et lancer le scheduler
* sinon passer et quitter (cron fera le lendemain)
* scheduler : attend jusque x min avant le train et affiche msg sur lcd
* lance le second scheduler etc.
* eteint l'ecran dans le dernier scheduler
'''

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
'''
# mode print only

# l'evenement qui sera execute a l'heure dite
def event_response(type_event):
    if type_event == 0:
        print("event 0 ",time.time())
    elif type_event == 1:
        print("event 1 ",time.time())
    elif type_event == 2:
        print("event 2 ",time.time())


# l'attente et la reponse (il sleep() entre les deux)
# si le time est dans le passé il s'exécute immediatement
def waittilltime(str,type_event):
    print("on attend a partir de : ",time.time())
    lancement = conversion_horaire(str)
    s.enterabs(lancement, 1, event_response, [type_event])
    s.run()
    print(time.time())
    print("fini")
'''
# les affichages sur l'ecran
def lcd_event(train,type_event):
    import lcd_display
    if type_event == 0:
        print("event 0 : "+time.ctime())
        lcd_display.affichage("train " + train + "\nokay", (0.0,1.0,0.0))
        print("train " + train + "\nokay")
    elif type_event == 1:
        print("event 1 : "+time.ctime())
        lcd_display.affichage("train " + train + "\ndouche !", (0.0,0.0,1.0))
        print("train " + train + "\ndouche !")
    elif type_event == 2:
        print("event 2 : "+time.ctime())
        lcd_display.affichage("train " + train + "\npartir !", (1.0,0.0,0.0))
        print("train " + train + "\npartir !")
        time.sleep(3)
        lcd_display.clear_screen()

# l'attente et la reponse (il sleep() entre les deux)
# si le time est dans le passé il s'exécute immediatement
def wait_and_lcd(str,train,type_event):
    print("on attend a partir de : " + time.ctime())
    lancement = conversion_horaire(str)
    s.enterabs(lancement, 1, lcd_event, [train,type_event])
    s.run()
    # print(time.time())
    # print("fin de l'attente")



if __name__ == '__main__':
    # ici on a récupéré une date au format '20161226T13381800'
    # horaires = ["20161226T23420000","20161226T23430000","20161226T23440000"]
    # waittilltime(horaires[0],0)
    # waittilltime(horaires[1],1)
    # waittilltime(horaires[2],2)
    horaires = ["20161227T00170000","20161227T00180000","20161227T00190000"]
    train = "7:20"
    wait_and_lcd(horaires[0],train,0)
    wait_and_lcd(horaires[1],train,1)
    wait_and_lcd(horaires[2],train,2)
