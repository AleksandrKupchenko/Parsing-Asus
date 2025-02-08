import requests
from bs4 import BeautifulSoup


base_url = 'https://shop.kz/karaganda/offers/noutbuki/filter/fltr_brand-is-asus/apply/?PAGEN_1='


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

page = 1  
all_laptops = []  
previous_count = None  

while True:
    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    
    title_divs = soup.find_all('div', class_='bx_catalog_item_title')
    price_divs = soup.find_all('div', class_='bx_catalog_item_price')

   
    if not title_divs or (previous_count is not None and len(title_divs) < previous_count):
        print("Парсинг завершен. Больше страниц нет.")
        break  

    previous_count = len(title_divs)  

    for i in range(len(title_divs)):
        title = title_divs[i].find('a').text.strip()  
        price = price_divs[i].find('span', class_='current_price').text.strip()  
        all_laptops.append(f"{title}: {price}")

    print(f"Страница {page} обработана...")  
    page += 1  


with open('text.txt', 'w', encoding='utf-8') as file:
    for laptop in all_laptops:
        file.write(f'{laptop}\n')

print("Парсинг завершен. Данные сохранены в text.txt")