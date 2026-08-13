from enum import Enum

class Categorie(str, Enum):
    PHARMACIE = "pharmacie"
    RESTAURANT = "restaurant"
    MAQUIS = "maquis"
    HOPITAL = "hopital"
    HOTEL = "hotel"
    STATION_SERVICE = "station_service"
    BANQUE = "banque"
    SUPERMARCHE = "supermarche"
    BOULANGERIE = "boulangerie"
    ECOLE = "ecole"

class Rayon(int, Enum):
    UN_KM = 1000
    DEUX_KM = 2000
    CINQ_KM = 5000
    DIX_KM = 10000
    VINGT_KM = 20000

TAGS_OSM = {
    Categorie.PHARMACIE: "amenity=pharmacy",
    Categorie.RESTAURANT: "amenity=restaurant",
    Categorie.MAQUIS: "amenity=bar",
    Categorie.HOPITAL: "amenity=hospital",
    Categorie.HOTEL: "tourism=hotel",
    Categorie.STATION_SERVICE: "amenity=fuel",
    Categorie.BANQUE: "amenity=bank",
    Categorie.SUPERMARCHE: "shop=supermarket",
    Categorie.BOULANGERIE: "shop=bakery",
    Categorie.ECOLE: "amenity=school"
}