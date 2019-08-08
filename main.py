import requests


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        f.read()

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

from bs4 import BeautifulSoup

r = requests.get(url)
print(r.content[:100])
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')
row = rows[0]
name = row.select_one('.source-title').text.strip()
print(name)

save_html(r.content, 'google_com')
