import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)
response.raise_for_status()

# === START ===

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

for quote in soup.select("div.quote"):
    text = quote.select_one("span.text").get_text(strip=True)
    author = quote.select_one("small.author").get_text(strip=True)

    tags = [
        tag.get_text(strip=True)
        for tag in quote.select("a.tag")
    ]

    quotes_data.append({
        "citat": text,
        "autor": author,
        "taguri": tags
    })

df = pd.DataFrame(quotes_data)

print(df.head(10))

# === END ===
