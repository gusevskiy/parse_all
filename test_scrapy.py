import scrapy


class all_parse(scrapy.Spider):
    
    name = "site"
    start_urls = ["жкхтеткино.рф"]
    
    def parse(self, response):
        for a in response.xpath('//a'):
            yield { 'a_link': a.xpath('.//a/@href').get()}