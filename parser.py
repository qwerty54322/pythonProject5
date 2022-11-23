from bs4 import BeautifulSoup
import requests
import random

def get_random_news():
    url = f'https://www.stopgame.ru'
    page = requests.get(url + '/news')
    soup = BeautifulSoup(page.text, 'html.parser')
    all_news = soup.findAll('div', class_='item article-summary')
    ln = len(all_news)
    x = random.randint(0, ln - 1)
    news = all_news[x]
    name = news.find('img')['alt']
    img = news.find('img')['src']
    link = url + news.find('a')['href']
    date = news.find('span').get_text(strip=True)
    tags = news.find('div', class_='tags').text
    return [name, img, link, date, tags]
z = get_random_news()
print(z)