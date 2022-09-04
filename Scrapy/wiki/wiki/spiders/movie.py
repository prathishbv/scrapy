import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/']

    def parse(self, response):
        movie_details = response.xpath("//table[@class='infobox vevent']/tbody/tr") 
        for detail in movie_details:
            name = detail.xpath(".//th/text()")
            yield{'details':name}
