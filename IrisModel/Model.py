# 1. Library imports
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
#from sklearn.ensemble.forest import RandomForestClassifier

from pydantic import BaseModel
import joblib


# 2. Class which describes a single flower measurements
##metodo de la clase Pydantic para validar los argumento de entrada la función 
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


# 3. Class for training the model and making predictions
class IrisModel:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = pd.read_csv('iris.csv') ##leemos csv 
        self.model_fname_ = 'iris_model.pkl' #path modelo 
        try:
            self.model = joblib.load(self.model_fname_) ##abre modelo 
        except Exception as _:
            self.model = self._train_model() ##llamar a método 
            joblib.dump(self.model, self.model_fname_) #si no existe path model, entrena modelo 
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self): #método de entrenamiento (se aplica cuando no se encontró path de modelo pkl previamente entrenado con los párametros necesarios)
        X = self.df.drop('species', axis=1) ##Tomo los valores de X, variables para realizar predicción 
        y = self.df['species'] #target con las clases de especies 
        rfc = RandomForestClassifier() #instancia modelo 
        model = rfc.fit(X, y) #entrena
        return model #retorna modelo 


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_length]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max() ##probabilidad maxima asociada a la clase que predice 
        return prediction[0], probability ##en lugar de array, retorna especie y la probabilidad de esa especie predicha 
