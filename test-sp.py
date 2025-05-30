import requests

BASE_URL = "http://172.18.0.2:1234"  # Change if your Signpost runs elsewhere

def test_signpost(resource, resource_id, template):
    url = f"{BASE_URL}/{resource}/{resource_id}/{template}"
    print(f"Testing: {url}")
    response = requests.get(url, allow_redirects=False)
    print("Status code:", response.status_code)
    if response.is_redirect:
        print("Redirect location:", response.headers.get("Location"))
    else:
        print("Response body:", response.text)
    print("-" * 40)

if __name__ == "__main__":
    # Replace these IDs and templates with values that exist in your Golbat DB and config.toml
    test_signpost("pokemon", "1234567890123456", "google")
    test_signpost("pokestop", "1234567890123456", "google")