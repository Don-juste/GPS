import requests
import time
from categories import Categorie, Rayon, TAGS_OSM
from gelocalistaion import calculer_distance

URLS_OVERPASS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter"
]

def rechercher_lieux_overpass(latitude: float, longitude: float, categorie: Categorie, rayon: Rayon) -> list:
    tag = TAGS_OSM[categorie]
    cle, valeur = tag.split("=")

    requete_overpass = f"""
    [out:json];
    nwr[{cle}={valeur}](around:{rayon.value},{latitude},{longitude});
    out center;
    """

    headers = {
        "User-Agent": "ProxiApp/1.0 (contact@tonapp.com)"
    }

    reponse = None
    for url in URLS_OVERPASS:
        for tentative in range(2):
            try:
                reponse = requests.post(url, data={"data": requete_overpass}, headers=headers, timeout=25)
                print(f"URL: {url}, tentative {tentative+1}, STATUS: {reponse.status_code}")
                if reponse.status_code == 200:
                    break
            except requests.exceptions.RequestException as e:
                print(f"URL: {url}, tentative {tentative+1}, ERREUR RESEAU: {e}")
                reponse = None
            time.sleep(2)
        if reponse is not None and reponse.status_code == 200:
            break

    if reponse is None or reponse.status_code != 200:
        print("ECHEC FINAL : tous les serveurs ont échoué")
        raise Exception("Erreur lors de la requête Overpass, tous les serveurs ont échoué")

    resultats = reponse.json()["elements"]

    lieux = []
    for element in resultats:
        nom = element.get("tags", {}).get("name", "Nom inconnu")

        if "lat" in element and "lon" in element:
            lat_lieu = element["lat"]
            lon_lieu = element["lon"]
        elif "center" in element:
            lat_lieu = element["center"]["lat"]
            lon_lieu = element["center"]["lon"]
        else:
            continue

        distance = calculer_distance(latitude, longitude, lat_lieu, lon_lieu)
        lieux.append({
            "nom": nom,
            "latitude": lat_lieu,
            "longitude": lon_lieu,
            "distance_km": round(distance, 2)
        })

    return sorted(lieux, key=lambda lieu: lieu["distance_km"])