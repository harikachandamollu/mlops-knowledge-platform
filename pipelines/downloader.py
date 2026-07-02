import requests

HEADERS = {
    "User-Agent": "Doc-Ingestion-Bot/1.0"
}

def download(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text