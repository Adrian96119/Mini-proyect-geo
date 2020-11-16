import requests
import os
from dotenv import load_dotenv 



#Vamos a hacer un filtro con las coordenadas de Seattle
"""
latitude = 47.60621
longitude = -122.33207
"""
load_dotenv()
clave = os.getenv("clave")
#Aqui unicamente utilice dentro de las apis de google maps la Api de busqueda por cercanía y la de busqueda por texto.

#saco una lista de escuelas dentro de la localización de Seattle, he visto que algunas de ellas tenian buena valoracion asique he elegido
#una de ellas y le he sacado las coordenadas.

url = "https://maps.googleapis.com" #nuestra Api de google maps

escuela_secundaria = f"/maps/api/place/textsearch/json?query=school&location=47.60621,-122.33207&type=secundary_school&key={clave}"
data_secundario = requests.get(url+escuela_secundaria).json()
es = data_secundario["results"]
lista_escuelas = [i["name"] for i in es]
nombre_se = lista_escuelas[16]
rating_secundarias = [i["rating"] for i in es]
rating_secundaria = rating_secundarias[16]
loc_se = [i["geometry"] for i in es]
localizacion_secundaria = loc_se[16]



#aqui cogeré las coordenadas del colegio secundario y vere y hay una escuela para chicos de primaria en un radio de 1500 metros.
escuela_primaria = f"/maps/api/place/nearbysearch/json?location=47.607718,-122.334751&radius=2000&type=primary_school&key={clave}"
data_primario = requests.get(url+escuela_primaria).json()
esp = data_primario["results"]
#saco la lista de colegios cercanos a la escuela secundaria y me aparecen 3, porque otro es en realidad un centro de salud.
lista_colegios = [i["name"]for i in esp]
#ratings = [i["rating"]for i in esp]

esp[0]["rating"]
esp[1]["rating"] #compruebo de esos tres cual tiene la valoracion mas alta y el elegido es el colegio de primaria Bailey Gatzert Elementary School.
esp[3]["rating"]

#asique le voy a sacar sus coordenadas

coordenadas_bailey = esp[3]["geometry"]

#47.6011701,-122.3155688




#vamos ahora a sacar un starbucks que este cerquita de la escuela de secundaria que era la que mas cerca estaba en general de las oficinas.
starbucks = f"/maps/api/place/nearbysearch/json?location=47.6033866,-122.3353421&radius=1&keyword=starbucks&key={clave}"

starbucks = requests.get(url+starbucks).json()
starbucks_elegido = starbucks["results"][0] #sacamos la primera que sera la más cercana y que además está abierta ya que no pone lo contrario, y cogemos sus coordenadas
print(starbucks_elegido) # elegimos el starbuck en funcion de la distancia de la discoteca.
#coordenadas starbucks = 47.60378799999999,-122.335678

#cogemos también la cercania del colegio secundario para sitios de fiesta
fiesta = f"/maps/api/place/nearbysearch/json?location=47.607718,-122.334751&radius=500&type=night_club&key={clave}"
data_fiesta = requests.get(url+fiesta).json()
disco = data_fiesta["results"]
lista_discos = [i["name"]for i in disco]
 #cogemos el club contour que ademas tiene una buena valoracion. sacamos su localizacion.
localizacion_disco = disco[0]["geometry"]

#47.6033866,-122.3353421

#ahora cogeremos la peluqueria más cercana al colegio de secundaria.

peluqueria = f"/maps/api/place/nearbysearch/json?location=47.607718,-122.334751&radius=50&keyword=hairdressing&key={clave}"
pelu = requests.get(url+peluqueria).json()
pelus = pelu["results"]
pelus_lista = [i["name"]for i in pelus]
 # tuvimos que prescindir de Sensa Salon porque estaba más lejos que la peluqueria de Aveda
#sacamos su localizacion como siempre.

#coordenadas de la peluqueria = 47.6050756,-122.3368054 

#Aqui se intento buscar un estadio de baloncesto y niquiera el maximo permitido por el ejercico que era un radio de 10 km aparecía alguno.
estadio_baloncesto= f"/maps/api/place/nearbysearch/json?location=47.607718,-122.334751&radius=10000&keyword=basketballstadium&key={clave}"
estadio = requests.get(url+estadio_baloncesto).json()

#No pude encontrar ningun estadio de baloncesto

#Buscamos también agencias de viaje en un radio de 100 metros y nos aparecieron unas cuantas, de las cuales sacamos una lista de sus nombres y de sus coordenadas.
agenciaDeviajes = f"/maps/api/place/nearbysearch/json?location=47.607718,-122.334751&radius=1&keyword=travelagency&key={clave}"
agencia = requests.get(url+agenciaDeviajes).json()
ag = agencia["results"]

lista_agencias=[i["name"] for i in ag] #Nos salen 4 pero nos quedamos con la primera llamada Meixi Travel Agency.

#le sacamos las coordenadas 47.6061317,-122.3338615