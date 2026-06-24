from fastapi import APIRouter
import zoneinfo
from datetime import datetime

router = APIRouter()

@router.get("/", tags=["extras"])
async def root():
    return {"message": "Hola John"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "US": "America/New_York",
    "UK": "Europe/London",
    "DE": "Europe/Berlin",
    "FR": "Europe/Paris",
    "ES": "Europe/Madrid"
}

@router.get("/time/{iso_code}", tags=["extras"])
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone)
    return {"time": datetime.now(tz)}