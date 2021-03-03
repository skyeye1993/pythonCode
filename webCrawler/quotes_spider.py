import scrapy

# 使用命令行   scrapy runspider quotes_spider.py
# 此代码在spider文档中可查

class QuotesSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # quotes = response.css('div.quote')
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'author': quote.xpath('./span/small/text()').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
            }

        # next_page = response.css('li.next a::attr("href")').get()
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)