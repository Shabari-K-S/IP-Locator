# 🌐 GeoInsight API 

**GeoInsight API** is a powerful IP geolocation and network intelligence service. Built using FastAPI and MaxMind's GeoLite2 database, it provides rich details about any public IPv4 or IPv6 address.

### ✨ Key Features:

* Get location data: **City, Region, Country, Continent**
* Network info: **ISP, ASN number**
* Precise geolocation: **Latitude, Longitude, Timezone**
* Smart detection: **VPN / Proxy / Hosting providers**
* Country Flag emoji 🇺🇸
* Graceful fallback when data is unavailable

---

## 🛣️ Endpoint: `/ip-info`

**Method:** `POST`
**Description:** Returns detailed geolocation and network information for a given IP address.

### 🔹 Request Body:

```json
{
  "ip": "8.8.8.8"
}
```

| Field | Type   | Required | Description          |
| ----- | ------ | -------- | -------------------- |
| ip    | string | ✅ Yes    | IPv4 or IPv6 address |

---

### 🔸 Response Fields:

* `continent`: Continent name
* `country`: Country name
* `country_iso_code`: ISO 3166-1 alpha-2 code
* `flag`: Country flag emoji
* `is_in_european_union`: Boolean flag
* `region`: State or province name
* `region_iso_code`: ISO code of the region
* `city`: City name
* `postal_code`: ZIP or postal code
* `latitude` / `longitude`: Coordinates
* `time_zone`: Local timezone
* `accuracy_radius_km`: Estimated accuracy radius
* `asn`: Autonomous System Number
* `isp`: ISP or Organization name
* `vpn`: Boolean flag for VPN/Proxy detection

If data is unavailable, `"Unknown"` or `0` is returned instead — making it easy to handle programmatically.

---

## 🧠 Use Cases:

* IP tracking and geolocation
* Fraud prevention and VPN detection
* Network analysis dashboards
* Location-based personalization
* Web analytics and user insights

---

## ⚡ Example:

**Input:**

```json
{ "ip": "8.8.8.8" }
```

**Output:**

```json
{
  "country": "United States",
  "region": "California",
  "city": "Mountain View",
  "isp": "Google LLC",
  "latitude": 37.386,
  "longitude": -122.0838,
  "vpn": false,
  ...
}
```

---

## 🚀 Start using GeoInsight API now – your intelligent IP toolkit awaits!
