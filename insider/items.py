# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InsiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Headline = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    Dates = scrapy.Field()
    Age = scrapy.Field()
    Mode = scrapy.Field()
    Language = scrapy.Field()
    Interesting_url = scrapy.Field()
    Not_Interesting_url = scrapy.Field()
    pass
