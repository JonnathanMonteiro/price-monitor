import json, schedule, time
from scraper import get_price
from notifier import send_alert
from config import CHECK_INTERVAL_MINUTES
 
def check_prices():
    print('Verificando preços...')
    with open('products.json') as f:
        products = json.load(f)
    for product in products:
        price = get_price(product['url'])
        if price is None:
            print(f'Não foi possível obter o preço de {product["name"]}')
            continue
        print(f'{product["name"]}: R$ {price:.2f}')
        if price <= product['target_price']:
            send_alert(product['name'], price, product['target_price'], product['url'])
 
if __name__ == '__main__':
    check_prices()   # Roda imediatamente ao iniciar
    schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(check_prices)
    while True:
        schedule.run_pending()
        time.sleep(60)
