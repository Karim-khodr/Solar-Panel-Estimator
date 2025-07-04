import requests

def fetch_solar_data(lat, lon):
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=ALLSKY_SFC_SW_DWN&start=20240101&end=20241231"
        f"&latitude={lat}&longitude={lon}&format=JSON"
    )
    response = requests.get(url).json()
    return response['properties']['parameter']['ALLSKY_SFC_SW_DWN']

def estimate_output(irradiance_data, area=1.6, efficiency=0.18, loss=0.8):
    total_kwh = sum(val * area * efficiency * loss for val in irradiance_data.values())
    return round(total_kwh, 2)