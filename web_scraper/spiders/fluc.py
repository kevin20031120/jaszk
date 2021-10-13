import scrapy
from web_scraper.items import WebScraperItem


class FlucSpider(scrapy.Spider):
    name = 'fluc'
    start_urls = ["https://www.fluc.at/programm/2021_Flucwoche25.html"]


def parse(self, response):
    Item = WebScraperItem()
    Item['title'] = response.xpath('//text()').getall()

    yield Item
