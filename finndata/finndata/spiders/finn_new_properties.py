# -*- coding: utf-8 -*-
import scrapy
import subprocess
from ..items import NewFinnItems

class NewBoligSpider(scrapy.Spider):
    #custom_settings = {'ITEM_PIPELINES': {'finndata.pipelines.NewFinndataPipeline': 200}}
    name = 'finn'
    allowed_domains = ['finn.no']
    start_urls = [
        'https://www.finn.no/realestate/newbuildings/search.html?filters=&location=0.20061']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        urls = response.css('a.ads__unit__link::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_alpha_page)

        # follow
        next_page_url = response.css('a.button--icon-right::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_alpha_page(self, response):
        alpha_url = response.css('th.u-text-left > a::attr(href)').extract()
        for link in alpha_url:
            link = response.urljoin(link)
            yield scrapy.Request(url=link, callback=self.parse_ads_details)

    def parse_ads_details(self, response):
        newFinnItems = NewFinnItems()
        try:
            newFinnItems['finn-code']= response.css('span.u-select-all::text').extract_first(),
            # 'headline': response.css('h1.u-t2::text').extract_first().replace(",", " "),
            newFinnItems['address']= response.css('p.u-caption::text').extract_first(default=",").replace(",", "[;]"),
            newFinnItems['total_price'] = response.xpath("//dt[contains(., 'Totalpris')]/following-sibling::dd/text()").extract_first(
                default=0).replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            newFinnItems['common_costs'] = response.xpath("//dt[contains(., 'Felleskost/mnd')]/following-sibling::dd/text()").extract_first(
                default='null').replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            newFinnItems['for_sale_price'] = response.css('div.panel > span.u-t3::text').extract_first(default=0).replace(
                "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", "").replace(">", ""),
            # 'ownership_form': response.xpath(
            #    "//dt[contains(., 'Eieform')]/following-sibling::dd/text()").extract_first(default='N/A').replace(
            #    "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            # 'building_type': response.xpath(
            #    "//dt[contains(., 'Boligtype')]/following-sibling::dd/text()").extract_first(default='N/A'),
            newFinnItems['bedrooms'] = response.xpath("//dt[contains(., 'Soverom')]/following-sibling::dd/text()").extract_first(default=0),
            newFinnItems['pra'] = response.xpath("//dt[contains(., 'Primærrom')]/following-sibling::dd/text()").extract_first(default=0).replace(
                "m²", ""),
            # 'year_built': response.xpath(
            #    "//dt[contains(., 'Byggeår')]/following-sibling::dd/text()").extract_first(default='null').replace(
            #    "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            newFinnItems['last_changed'] = response.xpath("//th[contains(., 'Sist endret')]/following-sibling::td/text()").extract_first(default='null'),
            newFinnItems['rooms'] = response.xpath("//dt[contains(., 'Rom')]/following-sibling::dd/text()").extract_first(
                default=0).replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", "")
        except Exception as e:
            print(e)


        yield newFinnItems

    def closed(self, reason):
        filename = "/newboligdata_out.csv"
        subprocess.call(['open', filename])