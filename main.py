from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = 'https://www.indeed.com/jobs?q=software%20developer&l=Seattle,%20WA&advn=6613095622180756'

client = uReq(url)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"jobsearch-SerpJobCard unifiedRow row result"})

total = len(containers)
counter = 0;
for container in containers:
    try:
        company_container = container.findAll("span",{'class':'company'})
        company = company_container[0].a.text.strip()
        counter += 1
    except:
        print("")

    title = container.div.a["title"]

    summary_container = container.find("div",{'class':'summary'})
    summary = summary_container.text.strip()

    print("company: " + company)
    print("title: " + title)
    print("summary: " + summary + "\n")

print(str(counter) + "/" + str(total) + " results shown")
