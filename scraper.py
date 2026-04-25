import requests
from bs4 import BeautifulSoup
 
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
 
def get_price(url: str) -> float | None:
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.select_one('.price, [data-price], .product-price')
        if price_tag:
            price_text = price_tag.get_text(strip=True)
            price_clean = price_text.replace('R$','').replace('.','').replace(',','.').strip()
            return float(price_clean)
    except Exception as e:
        print(f'Erro: {e}')
    return None
