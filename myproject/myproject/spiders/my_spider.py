import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def parse(self, response):
        self.log('Visited %s' % response.url)
