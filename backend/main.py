from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from solar import fetch_solar_data, estimate_output
from geocode import get_coordinates

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/estimate")
def estimate(address: str):
    lat, lon = get_coordinates(address)
    irradiance_data = fetch_solar_data(lat, lon)
    total_output = estimate_output(irradiance_data)
    return {
        "address": address,
        "latitude": lat,
        "longitude": lon,
        "total_kwh": total_output,
        "avg_irradiance": sum(irradiance_data.values()) / len(irradiance_data)
    }