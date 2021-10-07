import scrapy

class FlucSpider(scrapy.Spider):
    name = "fluc"
    start_urls = [
        'https://www.fluc.at/programm/2021_Flucwoche25.html',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'fluc-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)