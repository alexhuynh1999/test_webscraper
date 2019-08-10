from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = 'https://www.indeed.com/jobs?q=software%20developer&l=Seattle,%20WA&advn=6613095622180756'

client = uReq(url)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"jobsearch-SerpJobCard unifiedRow row result"})

for container in containers:
    company = container.find("a",{'data-tn-element':"companyName"}).text.strip()
    title = container.div.a["title"]
    summary = container.find("div",{'class':'summary'}).text.strip()