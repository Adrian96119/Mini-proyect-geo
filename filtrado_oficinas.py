import os
from dotenv import load_dotenv
import googlemaps
print(load_dotenv())
clave = os.getenv("clave")
# latitudes de colegio de secundaria = 47.607718,-122.334751

"""
coordenadas de oficinas

wetpaint = 47.603122,-122.333253
google = 47.649701,-122.350592
Jobster = 47.617682,-122.357242
ZenZui = 47.620716,-122.347533
Yapta = 47.599925, -122.334264
Farecast = 47.620982,-122.359397
TripHub = 47.614653,-122.338793
Newsvine = 47.618599, -122.358484
iLike = 47.615313,-122.323408
Redfin =  47.603122,-122.333253
"""
#lo que hago a continuacion es medir las distancias entre las coordenadas del colegio de secundaria, con las de las diez oficinas que tengo.

maps = googlemaps.Client(key=clave)

wetpaint = maps.distance_matrix('47.607718,-122.334751','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
google = maps.distance_matrix('47.607718,-122.334751','47.649701,-122.350592')["rows"][0]["elements"][0]["distance"]["text"]
Jobster = maps.distance_matrix('47.607718,-122.334751','47.617682,-122.357242')["rows"][0]["elements"][0]["distance"]["text"]
ZenZui = maps.distance_matrix('47.607718,-122.334751','47.620716,-122.347533')["rows"][0]["elements"][0]["distance"]["text"]
Yapta= maps.distance_matrix('47.607718,-122.334751','47.599925,-122.334264')["rows"][0]["elements"][0]["distance"]["text"]
Farecast= maps.distance_matrix('47.607718,-122.334751','47.620982,-122.359397')["rows"][0]["elements"][0]["distance"]["text"]
TripHub = maps.distance_matrix('47.607718,-122.334751','47.614653,-122.338793')["rows"][0]["elements"][0]["distance"]["text"]
Newsvine= maps.distance_matrix('47.607718,-122.334751','47.618599,-122.358484')["rows"][0]["elements"][0]["distance"]["text"]
iLike= maps.distance_matrix('47.607718,-122.334751','47.615313,-122.323408')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.607718,-122.334751','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
print(wetpaint,google,Jobster,ZenZui,Yapta,Farecast,TripHub,Newsvine,iLike,Redfin) #con esto veo las distancias de cada oficina con el colegio de secundaria.
#compruebo que la de google esta bastante lejos, a 6 km, asique la puedo ir descartando y quedarme con las otras que estan, la que más a 2.7 km.

#para el siguiente filtro, tomaré las coordenadas de el colegio de primaria y las compararé con las 9 oficinas que me quedan.

#latitudes del colegio de primaria = 47.6011701,-122.3155688

wetpaint = maps.distance_matrix('47.6011701,-122.3155688','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
Jobster = maps.distance_matrix('47.6011701,-122.3155688','47.617682,-122.357242')["rows"][0]["elements"][0]["distance"]["text"]
ZenZui = maps.distance_matrix('47.6011701,-122.3155688','47.620716,-122.347533')["rows"][0]["elements"][0]["distance"]["text"]
Yapta= maps.distance_matrix('47.6011701,-122.3155688','47.599925,-122.334264')["rows"][0]["elements"][0]["distance"]["text"]
Farecast= maps.distance_matrix('47.6011701,-122.3155688','47.620982,-122.359397')["rows"][0]["elements"][0]["distance"]["text"]
TripHub = maps.distance_matrix('47.6011701,-122.3155688','47.614653,-122.338793')["rows"][0]["elements"][0]["distance"]["text"]
Newsvine= maps.distance_matrix('47.6011701,-122.3155688','47.618599,-122.358484')["rows"][0]["elements"][0]["distance"]["text"]
iLike= maps.distance_matrix('47.6011701,-122.3155688','47.615313,-122.323408')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.6011701,-122.3155688','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]

print(wetpaint,Jobster,ZenZui,Yapta,Farecast,TripHub,Newsvine,iLike,Redfin)
#compruebo y descarto las oficinas de jobster,zenzui,farecast y newsvine que se encuentran alrededor de 4 km de distancia.


#Ahora hacemos lo mismo con el starbucks
#coordenadas de starbucks 47.60378799999999,-122.335678

wetpaint = maps.distance_matrix('47.60378799999999,-122.335678','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
Yapta= maps.distance_matrix('47.60378799999999,-122.335678','47.599925,-122.334264')["rows"][0]["elements"][0]["distance"]["text"]
TripHub = maps.distance_matrix('47.60378799999999,-122.335678','47.614653,-122.338793')["rows"][0]["elements"][0]["distance"]["text"]
iLike= maps.distance_matrix('47.60378799999999,-122.335678','47.615313,-122.323408')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.60378799999999,-122.335678','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]

print(wetpaint,Yapta,TripHub,iLike,Redfin) #descartamos Triphub y iLike que se encuentran a mas de un km...


#lo mismo con el club contour
#sus coordenadas 47.6033866,-122.3353421
wetpaint = maps.distance_matrix('47.6033866,-122.3353421','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
Yapta= maps.distance_matrix('47.6033866,-122.3353421','47.599925,-122.334264')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.6033866,-122.3353421','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]

print(wetpaint,Yapta,Redfin) #nos quedamos con la oficina de wetpaint y la de redfin, que son las más cercanas.

#coordenadas peluqueria  = 47.6050756,-122.3368054



wetpaint = maps.distance_matrix('47.6050756,-122.3368054','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.6050756,-122.3368054','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
print(wetpaint,Redfin) #De forma increible esta a la misma distancia de cada una

#por ultimo lo hacemos con la agencia 
#47.6061317,-122.3338615

wetpaint = maps.distance_matrix('47.6061317,-122.3338615','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
Redfin = maps.distance_matrix('47.6061317,-122.3338615','47.603122,-122.333253')["rows"][0]["elements"][0]["distance"]["text"]
print(wetpaint,Redfin) #me parecio demasiada casualidad que dieran otra vez la misma distancia, asique me di cuenta que tenían las mismas coordenadas. Es decir
#es la misma oficina, por tanto ya tenemos ganadora!!!!


