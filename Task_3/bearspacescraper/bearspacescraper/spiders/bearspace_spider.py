import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, CrawlSpider, Rule


class Mixin:
    site = 'bearspace'
    allowed_domains = ['bearspace.co.uk']
    start_urls = ['https://www.bearspace.co.uk/purchase?page=10000']
    custom_settings = {'DOWNLOAD_DELAY': 2}


class BearSpaceParseSpider(Spider, Mixin):
    name = Mixin.site + '-parse'

    def parse(self, response, **kwargs):
        artwork = {}
        artwork['url'] = response.url
        artwork['title'] = response.css('h1[data-hook="product-title"] ::text').get()
        artwork['price'] = response.css('[data-hook="formatted-primary-price"] ::text').get()
        artwork['media'] = response.css('[data-hook="description"]').xpath('./p[1]//text()').get()
        artwork['height_cm'], artwork['width_cm'] = self.extract_dimensions(response)

        yield artwork

    def extract_dimensions(self, response):
        regex = r'(?i)(\d+(?:[,|.]\d+)?)\s*(?:cm)?\s*(?:\s*[x|by]\s*(?:width)?\s*(\d+(?:[,|.]\d+)?))?'
        dimensions_css = '[data-hook="description"] ::text'
        description = response.css(dimensions_css).getall()
        description = ' '.join([s for s in description if 'cm' in s.lower()]) or ' '.join(description)
        dimensions = re.findall(regex, description)
        return dimensions[0]


class BearSpaceCrawlSpider(CrawlSpider, Mixin):
    name = Mixin.site + '-crawl'
    parse_spider = BearSpaceParseSpider()
    artwork_css = ['[data-hook="product-item-root"]']

    def parse_item(self, response):
        return self.parse_spider.parse(response)

    rules = (
        Rule(LinkExtractor(restrict_css=artwork_css), callback='parse_item'),
    )
