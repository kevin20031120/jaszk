import scrapy
from scrapy.item import Item, Field



class WebScraperItem(Item):

        Class = Field()
        urlsonsite = Field()
        content = Field()
        patagraphs = Field()
        headers = Field()
        title = Field()
        link = Field()
        desc = Field()
        request = Field()
        price = Field()