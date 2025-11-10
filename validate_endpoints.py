import requests


staging_urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.linkedin.com"
]

for url in staging_urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url}: ✅ Working")
        else:
            print(f"{url}: ⚠️ Error {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url}: ❌ Not responding")

