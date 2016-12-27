#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
renvoie l'heure de départ, d'arrivee et la duree
d'un train qui arrive part de Lille et arrive à Hazebrouck avant l'horaire indiquée
horaire = "20161229T080000"
'''
def sncf_train(horaire):
	# import time
	import urllib, json
	import token

	sandboxToken = token.sandboxToken # api key sncf
	froms = 'stop_area:OCE:SA:87286005' # lille
	to = 'stop_area:OCE:SA:87286302' 	# hazebrouck

	# url qui renvoie de l'api sncf qui renvoie un json
	url = "https://"+sandboxToken+"@api.sncf.com/v1/coverage/sncf/journeys?from="+froms+'&to='+to+'&datetime_represents=arrival&datetime='+horaire +'&'
	print('parsed url :')
	print(url)

	response = urllib.urlopen(url) # charge l'url
	data = json.loads(response.read()) # charge les données dans data

	# on cherche dans 'journeys' (= les voyages) si on a une section de type "public_transport"
	for voyage in data['journeys'][0]["sections"]:
		if voyage["type"]=="public_transport":
			# print(voyage) # debug : pour tout afficher
			start =voyage["departure_date_time"] # l'heure de départ 20161229T071500
			start = start[-6:-4] + ":" + start[-4:-2] # 07:15 - à améliorer

			stop =voyage["arrival_date_time"] # l'heure d'arrivee 20161229T074600
			stop = stop[-6:-4] + ":" + stop[-4:-2] # 07:46 - à améliorer

			duration = str(voyage["duration"] / 60)

			print("le train part a "+start)
			print("le train arrive a "+stop)
			print("le trajet dure "+duration+ " minutes") # la durée en minutes
	return([start,stop,duration])


# le train que je prends qd j'ai cours à 8h
def ajd_pour8h():
	from time import localtime, strftime
	print(" ")
	print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
	arrive=strftime("%Y%m%dT072500", localtime())
	print("horaire sncf : " +arrive)
	sncf_train(arrive)

# le train que je prends qd j'ai cours à 10h45
def ajd_pour12h45():
	from time import localtime, strftime
	print(" ")
	print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
	arrive=strftime("%Y%m%dT110000", localtime())
	print("horaire sncf : " +arrive)
	sncf_train(arrive)



if __name__ == '__main__':
	# le 29 decembre 2016 à 8h (arriver à Haz avant le...)
	# sncf_train('20161229T080000')
	ajd_pour12h45()
	ajd_pour8h()
