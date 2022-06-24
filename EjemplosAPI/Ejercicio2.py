
##Durangozki 
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from pytz import timezone
import uvicorn
import requests

app = FastAPI() ##instancia 

db = []

class City(BaseModel): ##corrobora el tipo de dato 
    name: str
    timezone: str


@app.get('/cities') ##añade la ruta 
def get_cities():
    results = []
    for city in db: #para cada ciudad en la lista db 
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}') ##extrae el datatime actual 
        current_time = r.json()['datetime'] #se almacena en json en forma de texto plano 
        results.append({'name' : city['name'], 'timezone': city['timezone'], 'current_time': current_time}) #añadae diccionario 
    return results

@app.get('/cities/{city_id}') ###ruta 
def get_city(city_id: int): ###consigue la ciudad de acuerdo al id que se le ingresa
    city = db[city_id-1] ##ubica la posicion 
    r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}') #hace request a la url 
    current_time = r.json()['datetime']
    return {'name' : city['name'], 'timezone': city['timezone'], 'current_time': current_time} #retorna diccinario 

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1] #almacena todas las ciudades y en el get se procesa 

@app.delete('/cities/{city_id}') #elimina la cidad de aceurdo al id que se le asigna 
def delete_city(city_id: int): 
    db.pop(city_id-1) #elimina posicion de la lista (diccionario)
    return {}

if __name__ == "__main__":
    uvicorn.run("Ejercicio2:app")



