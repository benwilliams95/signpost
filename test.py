import requests

GOLBAT_URL = "http://localhost:9001/api/gym/id/0015119b835a40c2972c91a4ffaabaa3.16"  # Change 12345 to your desired pokemon_id
API_PASSWORD = "SuperSecureGolbatApiSecret"  # From your config.toml

headers = {
    "Content-Type": "application/json",
    "X-Golbat-Secret": API_PASSWORD,
}

response = requests.get(GOLBAT_URL, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)