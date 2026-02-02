import requests
import os

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def google_search(query):
    url = "https://google.serper.dev/search"

    payload = {
        "q": query,
        "num": 5
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    results = []
    for item in data.get("organic", []):
        results.append({
            "title": item.get("title"),
            "snippet": item.get("snippet"),
            "link": item.get("link")
        })

    return results