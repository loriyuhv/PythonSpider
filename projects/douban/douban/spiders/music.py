import scrapy


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    def parse(self, response):
        pass
