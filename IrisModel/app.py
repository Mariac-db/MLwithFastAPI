# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Model import IrisModel, IrisSpecies #importar script model y usar clase IrisModel e IrisSpecies  


# 2. Create app and model objects
app = FastAPI() #api instance
model = IrisModel() #model instance, va a cargar las instancias del modelo 

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict') ##subruta
def predict_species(iris: IrisSpecies): #varaible que tendrá que tener estrutura de acuerdo a IrisSpecies (vadilación)
    data = iris.dict() #dicitionary data
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }


# 4. Run the API with uvicorn
#Ahora todo melo para hacer la predicción de nuestro modelo, when you like to use both lenguages, spanglish there we go

#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)