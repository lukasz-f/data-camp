import scrapy


class QuotesSpider(scrapy.Spider):
    """Making requests for highest grossing movies of each year"""

    name = "boxofficemojo"
    start_urls = [
        'http://www.boxofficemojo.com/yearly/chart/?yr=2017',
    ]

    def parse(self, response):
        yield {
            'title': response.css('table')[6].css('tr')[2].css('td')[1].css('a::text').extract_first(),
            'year': response.css('h1::text')[0].extract()[:4],
            'boxoffice': response.css('table')[6].css('tr')[2].css('td')[3].css('b::text').extract_first(),
        }
        next_page = 'http://www.boxofficemojo.com' + response.css("a:contains('Previous')::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
