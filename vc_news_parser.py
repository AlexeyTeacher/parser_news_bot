import requests
from bs4 import BeautifulSoup

URL = 'https://vc.ru/new/all/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='feed__item l-island-round')
    news = []
    for item in items:
        if item.find('div', class_='content-title content-title--short l-island-a') is not None:
            news.append(
                {
                    'title': item.find('div', class_='content-title content-title--short l-island-a').get_text().strip(),
                    'text': item.p,
                    'link_news': item.find('a', class_='content-link').get('href').strip()
                }
            )
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        return f'Error {html.status_code}'



