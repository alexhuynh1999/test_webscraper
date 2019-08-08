import requests
from bs4 import BeautifulSoup


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        f.read()


url = 'https://www.indeed.com/jobs?q=software%20developer&l=Seattle%2C%20WA&advn=6613095622180756'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select_one('.pageContent')
print(rows)