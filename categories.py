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
    BUVETTE = "buvette"
    MARCHE = "marche"
    LIEU_DE_CULTE = "lieu_de_culte"

class Rayon(int, Enum):
    UN_KM = 1000
    DEUX_KM = 2000
    CINQ_KM = 5000
    DIX_KM = 10000
    VINGT_KM = 20000

TAGS_GEOAPIFY = {
    Categorie.PHARMACIE: "healthcare.pharmacy",
    Categorie.RESTAURANT: "catering.restaurant",
    Categorie.MAQUIS: "catering.bar",
    Categorie.HOPITAL: "healthcare.hospital",
    Categorie.HOTEL: "accommodation.hotel",
    Categorie.STATION_SERVICE: "service.vehicle.fuel",
    Categorie.BANQUE: "service.financial.bank",
    Categorie.SUPERMARCHE: "commercial.supermarket",
    Categorie.BOULANGERIE: "commercial.food_and_drink.bakery",
    Categorie.ECOLE: "education.school",
    Categorie.BUVETTE: "catering.pub",
    Categorie.MARCHE: "commercial.marketplace",
    Categorie.LIEU_DE_CULTE: "religion.place_of_worship",
}