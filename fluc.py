import scrapy
from web_scraper.items import WebScraperItem


class FlucSpider(scrapy.Spider):
    name = 'fluc'

    x = "42"
    y = "43"
    start_urls = ["https://www.fluc.at/programm/2021_Flucwoche%s  %.html"]

def parse(self,response):
    Item = WebScraperItem()
    Item['title'] = response.xpath('//text()').getall()

    yield Item
