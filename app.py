import requests
from bs4 import BeautifulSoup


link = 'https://www.olx.kz/elektronika/igry-i-igrovye-pristavki/pristavki/karaganda/'

response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')

main_div = soup.find('div',class_='css-j0t2x2')
paragraphs = main_div.find_all('p')


       



with open('text.txt', 'w', encoding='utf-8') as file:
    for p in paragraphs:
        file.write(f'{p.text}\n')
