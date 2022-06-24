from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import uvicorn
import requests

##import requeriments
app=FastAPI() ##instancia
db=[] #lista que contiene nombre de ciudades

class City(BaseModel):#valida el tipo de formato y las variables de entrada de city 
    #clase de Pydanctic que ayuda a verificar el tipo de parámetros de la funcipon create_city
    name:str
    timezone:str

@app.get('/cities') ###devolver la base de datos 
def get_cities():
    return db

@app.post('/cities') ##devuelve con la url de city
def create_city(city:City): #tendra variables time and timezone
    db.append(city.dict())
    return db[-1]

if __name__ == "__main__":
    uvicorn.run("Ejercicio1:app")


