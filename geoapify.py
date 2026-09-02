import requests
import os
from dotenv import load_dotenv
load_dotenv()

from categories import Categorie, Rayon, TAGS_GEOAPIFY
from gelocalistaion import calculer_distance

GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

def rechercher_lieux_geoapify(latitude: float, longitude: float, categorie: Categorie, rayon: Rayon) -> list:
    categorie_geoapify = TAGS_GEOAPIFY[categorie]

    params = {
        "categories": categorie_geoapify,
        "filter": f"circle:{longitude},{latitude},{rayon.value}",
        "limit": 50,
        "apiKey": GEOAPIFY_API_KEY
    }

    try:
        reponse = requests.get("https://api.geoapify.com/v2/places", params=params, timeout=25)
        print(f"STATUS: {reponse.status_code}")
        print(f"REPONSE: {reponse.text[:300]}")
    except Exception as e:
        print(f"ERREUR RESEAU: {e}")
        raise Exception("Erreur lors de la requête Geoapify")

    if reponse.status_code != 200:
        raise Exception(f"Erreur Geoapify : {reponse.status_code}")

    resultats = reponse.json()["features"]

    lieux = []
    for element in resultats:
        proprietes = element.get("properties", {})
        nom = proprietes.get("name", "Nom inconnu")
        lon_lieu = proprietes.get("lon")
        lat_lieu = proprietes.get("lat")

        if lat_lieu is None or lon_lieu is None:
            continue

        distance = calculer_distance(latitude, longitude, lat_lieu, lon_lieu)
        lieux.append({
            "nom": nom,
            "latitude": lat_lieu,
            "longitude": lon_lieu,
            "distance_km": round(distance, 2)
        })

    return sorted(lieux, key=lambda lieu: lieu["distance_km"])