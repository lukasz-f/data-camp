import scrapy


class QuotesSpider(scrapy.Spider):
    """Making requests for quotes in humor category"""

    name = "quotes"  # unique within project Spider'a name
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',  # URL hich the Spider will begin to crawl from
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
