#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
recupere le jour, lance une recherche
"""
import datetime
import json_sncf

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


# on recupere le jour de la semaine (lundi = 0)
jour_de_la_semaine = datetime.datetime.today().weekday()
debut_cours = emploi_du_temps[jour_de_la_semaine]

# si un cours est prevu
if debut_cours:
    print("je dois arriver a {} heure".format(debut_cours))
    horaire = json_sncf.ajd_pour_x_heure(debut_cours)
    print(horaire)
    print(horaire[0]) # l'heure a laquelle je dois etre dans le train
    # calcul de l'horaire
    



if __name__ == '__main__':
    # print(emploi_du_temps[0])
    # print(emploi_du_temps[2])
    pass
