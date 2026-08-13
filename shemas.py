from pydantic import BaseModel
from categories import Categorie, Rayon

class RechercheLieu(BaseModel):
    latitude: float
    longitude: float
    categorie: Categorie
    rayon: Rayon