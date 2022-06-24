
"""
Código basado en repositorio de https://github.com/Kunal-Varma/
"""

from pydantic import BaseModel
# 2. Esta clase que describe las medidas de los billetes

class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float