from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = 'https://www.indeed.com/jobs?q=software%20developer&l=Seattle,%20WA&advn=6613095622180756'

client = uReq(url)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
results = page_soup.findAll("td", {"id":"resultsCol"})
containers = page_soup.findAll("div",{"class":"jobsearch-SerpJobCard unifiedRow row result"})