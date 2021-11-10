# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    time = scrapy.Field()
    nation = scrapy.Field()
    scenario = scrapy.Field()

# class SunItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = scrapy.Field()
#     hello = scrapy.Field()
