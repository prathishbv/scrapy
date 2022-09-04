import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=phone&crid=WPUSID9U3ER4&sprefix=pho%2Caps%2C809&ref=nb_sb_noss_2']

    def parse(self, response):
        pass
