import scrapy
import requests
from lxml import html


class FlucSpider(scrapy.Spider):
        name = "fluc"
        start_urls = ["https://www.fluc.at/programm/2021_Flucwoche25.html"]

        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = f'fluc-{page}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

                def fluc_scraper(start_urls):
                    results = []
                    tree = html.fromstring(requests.get(start_urls).text)
                    for titles in tree.cssselect("a.issuesInYear"):
                        title = titles.cssselect("span")[0].text
                        title_link = titles.attrib['href']
                        results.append([title, title_link])
                    return results
                print(fluc_scraper(start_urls))