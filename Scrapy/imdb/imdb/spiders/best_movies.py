import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
        yield{
            'title' : response.xpath("//div[@class='sc-80d4314-1 fbQftq']/h1/text()").get(),
            'year' : response.xpath(" //span[@class='sc-8c396aa2-2 itZqyK']/text()").get(),
            # 'duration' : response.xpath("//div[@class='sc-80d4314-1 fbQftq']/h1/text()").get(),
            'genre' : response.xpath(" //a[@class='sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt']/span/text()").get(),
            'rating' : response.xpath("//span[@class='sc-7ab21ed2-1 jGRxWM']/text()").get(),
            'movie_url' : response.url,
            'user_agent': response.request.headers['User-Agent']
        }