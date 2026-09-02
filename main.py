from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import shemas
from overpass import rechercher_lieux_overpass
import requests
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/recherche-lieux")
@limiter.limit("10/minute")
def rechercher_lieux(request:Request,demande: shemas.RechercheLieu):
    try:
        resultats = rechercher_lieux_overpass(
            demande.latitude,
            demande.longitude,
            demande.categorie,
            demande.rayon
        )
    except Exception:
        raise HTTPException(status_code=503, detail="Service de recherche indisponible, réessayez plus tard")

    return {
        "nombre_resultats": len(resultats),
        "lieux": resultats
    }
    
@app.get("/test-reseau")
def test_reseau():
    resultats = {}
    
    sites_a_tester = {
        "github": "https://api.github.com",
        "google": "https://www.google.com",
        "overpass": "https://overpass-api.de/api/interpreter"
    }
    
    for nom, url in sites_a_tester.items():
        try:
            reponse = requests.get(url, timeout=10)
            resultats[nom] = f"OK - status {reponse.status_code}"
        except Exception as e:
            resultats[nom] = f"ECHEC - {str(e)}"
    
    return resultats    