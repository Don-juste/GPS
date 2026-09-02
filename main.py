from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import shemas
from geoapify import rechercher_lieux_geoapify
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
def rechercher_lieux(request: Request, demande: shemas.RechercheLieu):
    try:
        resultats = rechercher_lieux_geoapify(
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