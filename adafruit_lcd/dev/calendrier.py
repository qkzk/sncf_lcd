#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
CALENDRIER

dependances :
    Adafruit_CharLCD
    json_sncf.py
    token.py
    lcd_display.py

principe :
    recupere chaque jour dans un calendrier l'heure a laquelle je dois arriver a haz
    affiche les infos dans la console (cour ?, date, horaire du train, horaires)
    affiche et colore l'ecran lcd en fct

"""


# imports
import time
import datetime
import sched
import json_sncf

# on défini un programmateur temporel (?) = scheduler
s = sched.scheduler(time.time, time.sleep)

# constantes

# [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]
emploi_du_temps = [
False,
"0725",
"0725",
"1100",
"0725",
False,
False
]

# le nb de seconde a maintenir l'ecran illumine
# display_time = 3 # 3 secondes pour debug
display_time = 10*60 # 10 minutes realiste


# fonctions

def affichage_matin():
    print("je dois arriver a {}:{} heure à Hazebrouck".format( *(debut_cours[0:2],debut_cours[2:4] )))
    horaire = json_sncf.ajd_pour_x_heure(debut_cours)
    # print(horaire)
    # print(horaire[0]) # l'heure a laquelle je dois etre dans le train
    # calcul de l'horaire
    # convertir une str en date (interpreté) et opérer dessus
    # horaire[3]=20161227T064500
    # datetime_train_depart = 2016-12-27 06:45:00
    datetime_train_depart = datetime.datetime.strptime(horaire[3], '%Y%m%dT%H%M%S')
    print("il faut se lever a :")
    datetime_lever = datetime_train_depart - datetime.timedelta(hours=1, minutes=15)
    print(datetime_lever)
    print("il faut se doucher a : ")
    datetime_douche = datetime_train_depart - datetime.timedelta(minutes=45)
    print(datetime_douche)
    print("il faut partir a :")
    datetime_quitter_appart = datetime_train_depart - datetime.timedelta(minutes=30)
    print(datetime_quitter_appart)
    print("le train part a :")
    print(datetime_train_depart)

    return [
    datetime_lever,
    datetime_douche,
    datetime_quitter_appart,
    datetime_train_depart,
    horaire[0]
    ]



'''
les evenements et l'affichage
'''



# l'attente et la reponse (il sleep() entre les deux)
# si le time est dans le passé il s'exécute immediatement
def wait_and_lcd(str,train,type_event):
    print("on attend a partir de : " + time.ctime())
    lancement = conversion_horaire(str)
    s.enterabs(lancement, 1, lcd_affichage, [train,type_event])
    s.run()
    # print("fin de l'attente")


# envoie les msg a afficher
def lcd_matin(listhoraires):
    print("Allumage LCD")
    for i in range(3):
        wait_and_lcd(listhoraires[i],listhoraires[4],i)


# on converti l'horaire au bon format :
# "2016-12-27 06:45:00"
# vers
# "1482776940.014"
def conversion_horaire(str):
    str_mktime = time.mktime(str.timetuple())
    # print(str_mktime)
    return str_mktime

# les affichages sur l'ecran lcd
def lcd_affichage(train,type_event):
    import lcd_display
    if type_event == 0:
        # print("event 0 : "+time.ctime())
        lcd_display.affichage("train " + train + "\n reveil...", (0.0,1.0,0.0))
        print("train " + train + "\nreveil")
    elif type_event == 1:
        # print("event 1 : "+time.ctime())
        lcd_display.affichage("train " + train + "\ndouche !", (0.0,1.0,1.0))
        print("train " + train + "\ndouche !")
    elif type_event == 2:
        # print("event 2 : "+time.ctime())
        lcd_display.affichage("train " + train + "\npartir !", (1.0,0.0,0.0))
        print("train " + train + "\npartir !")
        time.sleep(display_time)
        lcd_display.clear_screen()


if __name__ == '__main__':
    # on recupere le jour de la semaine (lundi = 0)
    jour_de_la_semaine = datetime.datetime.today().weekday()
    # on recupere le calendrier
    debut_cours = emploi_du_temps[jour_de_la_semaine]
    # si un cours est prevu
    if debut_cours:
        print("\nj'ai cours aujourd'hui")
        # on affiche les horaires dans la console
        leshoraires = affichage_matin()
        # on affiche les infos sur le lcd
        lcd_matin(leshoraires)
    else:
        from time import localtime, strftime
        print("\nNous sommes le : ")
    	print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
        print("je n'ai pas cours aujourd'hui")
    pass
