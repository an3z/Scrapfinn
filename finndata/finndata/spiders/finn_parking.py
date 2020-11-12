# -*- coding: utf-8 -*-
import scrapy
from ..items import  ParkingItems

class ParkingSpider(scrapy.Spider):
    #custom_settings = {'ITEM_PIPELINES': {'finndata.pipelines.parkingPipeline': 300}}
    name = 'finn_parking'
    allowed_domains = ['finn.no']
    start_urls = ['https://www.finn.no/realestate/homes/search.html?location=0.22030&location=0.20061&property_type=6']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        price_area = response.css('span.u-t3::text').extract()
        urls = response.css('a.ads__unit__link::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_ads_details)

        # follow
        next_page_url = response.css('a.button--icon-right::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_ads_details(self, response):
        try:
            parkingItems =ParkingItems()
            parkingItems['finn_code'] = response.css('span.u-select-all::text').extract_first(),
            parkingItems['title'] = response.css('span.u-t3::text')[0].extract(),
            parkingItems['headline']= response.css('h1.u-t2::text').extract_first(default="NaN"),
            parkingItems['address'] = response.css('p.u-caption::text').extract_first(default="NaN"),
            parkingItems['price']= response.css('div.panel > span.u-t3::text').extract_first(default="NaN"),
        except Exception as e:
            print(e)

        yield parkingItems

