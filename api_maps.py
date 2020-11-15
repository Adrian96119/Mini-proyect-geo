import requests
import os
from dotenv import load_dotenv 

url = "https://maps.googleapis.com" #nuestra Api de google maps

#Oficina de Wetpoint Seatle
latitude = 47.603122
longitude = -122.333253

clave = os.getenv("clave_maps")
#unicamente utilice dentro de las apis de google maps la Api de busqueda por cercanía

#saco una escuela secundaria en un radio de 700 metros, saco su valoracion y la localizacion por coordenadas.
escuela_secundaria = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=700&type=secondary_school&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
data_secundario = requests.get(url+escuela_secundaria).json()
nombre_colegio_secundario = data_secundario["results"][0]["name"]
rating_secundario = data_secundario["results"][0]["rating"]
localizacion_secundario = data_secundario["results"][0]["geometry"]


#Aqui hice practicamente lo mismo solo que cambie el radio a 1500 porque no me encontraba una más cercana.
escuela_primaria = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=1500&type=primary_school&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
data_primario = requests.get(url+escuela_primaria).json()
nombre_colegio_primario = data_primario["results"][1]["name"]
rating_primaria = data_primario["results"][1]["rating"]
localizacion_primaria = data_primario["results"][1]["geometry"]


#aqui hemos sacado el starbucks más cercano a la oficina y su localizacion. Cabe destacar que se encuentra de la oficina a 100 metros! Esta pegada!!!
starbucks = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=100&keyword=starbucks&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"

starbucks = requests.get(url+starbucks).json()
localizacion_starbucks = starbucks["results"][0]["geometry"]


#aqui hemos sacado una lista de los clubs de fiesta mas cercanos en un radio de 300 metros, también hemos sacado sus localizaciones.
fiesta = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=300&type=night_club&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
data_fiesta = requests.get(url+fiesta).json()
disco = data_fiesta["results"]
listas_discos =[i["name"]for i in disco]
 #lista de discos en un radio de 300 metros.
localizaciones_discos = [d["geometry"]for d in disco]

#aqui busque las peluquerías mas cercanas en un radio de 100 metros, y sus localizaciones.

peluqueria = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=100&keyword=hairdressing&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
pelu = requests.get(url+peluqueria).json()
pelus = pelu["results"]
lista_peluquerias =[p["name"]for p in pelus]
 #peluquerias en un radio de 100 metros
localizaciones_pelus = [d["geometry"]for d in pelus]

#Aqui se intento buscar un estadio de baloncesto y niquiera el maximo permitido por el ejercico que era un radio de 10 km aparecía alguno.
estadio_baloncesto= "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=10000&keyword=basketballstadium&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
estadio = requests.get(url+estadio_baloncesto).json()
 #No pude encontrar ningun estadio de baloncesto

#Buscamos también agencias de viaje en un radio de 100 metros y nos aparecieron unas cuantas, de las cuales sacamos una lista de sus nombres y de sus coordenadas.
agenciaDeviajes = "/maps/api/place/nearbysearch/json?location=47.603122,-122.333253&radius=100&keyword=travelagency&key=AIzaSyDXnDhIgOa-C4ngxIZuV3Tw4nBaZBv3ZnU"
agencia = requests.get(url+agenciaDeviajes).json()
lista_agencias =[a["name"]for a in agencia["results"]]
localizaciones_agencias = [d["geometry"]for d in agencia["results"]]



