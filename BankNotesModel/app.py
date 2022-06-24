# -*- coding: utf-8 -*-
"""
Código basado en repositorio de https://github.com/Kunal-Varma/

"""

# 1. Importando librerias
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# 2. Creamos el app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# 3. Función para la predicción,
# Utiliza los datos del JSON para predecir y devuelva el billete predicho con la confianza

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction ="Billete falso"
    else:
        prediction= "Es un billete real del banco"
    return {
        'prediction': prediction
    }

# 5. Ejecute la API con uvicorn
# Se ejecutará en http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
