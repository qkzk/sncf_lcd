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
			startf = start[-6:-4] + ":" + start[-4:-2] # 07:15 - à améliorer

			stop =voyage["arrival_date_time"] # l'heure d'arrivee 20161229T074600
			stopf = stop[-6:-4] + ":" + stop[-4:-2] # 07:46 - à améliorer

			duration = str(voyage["duration"] / 60)

			print("le train part a "+startf)
			print("le train arrive a "+stopf)
			print("le trajet dure "+duration+ " minutes") # la durée en minutes
	return([startf,stopf,duration,start])


# le train que je prends qd je dois arriver a...
def ajd_pour_x_heure(x):
	from time import localtime, strftime
	print("Nous sommes le : ")
	print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	arrive=strftime("%Y%m%dT", localtime())
	arrive = arrive + x + "00"
	# print("horaire sncf : " +arrive)
	horaire = sncf_train(arrive)
	return(horaire)





if __name__ == '__main__':
	#si je dois arriver a 7h25
	ajd_pour_x_heure("0725")
