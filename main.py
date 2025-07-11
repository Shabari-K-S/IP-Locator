from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import geoip2.database

app = FastAPI()

# Load GeoIP databases
city_reader = geoip2.database.Reader("GeoLite2-City.mmdb")
country_reader = geoip2.database.Reader("GeoLite2-Country.mmdb")
asn_reader = geoip2.database.Reader("GeoLite2-ASN.mmdb")

class IPRequest(BaseModel):
    ip: str

def detect_vpn(org: str):
    if org and any(kw in org.lower() for kw in ["vpn", "proxy", "tor", "digitalocean", "ovh", "linode"]):
        return True
    return False

def get_flag(iso_code: str):
    if not iso_code or len(iso_code) != 2:
        return ""
    return ''.join(chr(0x1F1E6 + ord(c.upper()) - ord('A')) for c in iso_code)

def safe(value, default="Unknown"):
    return value if value is not None else default

@app.post("/ip-info")
def get_ip_info(data: IPRequest):
    try:
        city_resp = city_reader.city(data.ip)
        asn_resp = asn_reader.asn(data.ip)

        country_iso = safe(city_resp.country.iso_code, None)

        return {
            "ip": data.ip,
            "continent": safe(city_resp.continent.name),
            "country": safe(city_resp.country.name),
            "country_iso_code": country_iso if country_iso else "Unknown",
            "flag": get_flag(country_iso) if country_iso else "",
            "is_in_european_union": safe(city_resp.country.is_in_european_union, False),
            "region": safe(city_resp.subdivisions.most_specific.name),
            "region_iso_code": safe(city_resp.subdivisions.most_specific.iso_code),
            "city": safe(city_resp.city.name),
            "postal_code": safe(city_resp.postal.code),
            "latitude": safe(city_resp.location.latitude, 0.0),
            "longitude": safe(city_resp.location.longitude, 0.0),
            "time_zone": safe(city_resp.location.time_zone),
            "accuracy_radius_km": safe(city_resp.location.accuracy_radius, 0),
            "asn": safe(asn_resp.autonomous_system_number, 0),
            "isp": safe(asn_resp.autonomous_system_organization),
            "vpn": detect_vpn(asn_resp.autonomous_system_organization)
        }

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid IP or not found")

@app.get("/ping")
def ping():
    return {"message": "pong"}
