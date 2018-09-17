# -*- coding: utf-8 -*-
import scrapy


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['http://habr.com/']

    def start_requests(self):
        urls = [
            'https://habr.com/all/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('article.post'):
            yield {
                'title': article.css('a.post__title_link::text').extract_first(),
                'author': article.css('span.user-info__nickname::text').extract_first(),
            }
