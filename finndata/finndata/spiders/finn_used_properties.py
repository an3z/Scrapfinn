# -*- coding: utf-8 -*-
import scrapy
import subprocess
from scrapy.loader import ItemLoader
from ..items import FinnItems




class BoligSpider(scrapy.Spider):
    #custom_settings = {'ITEM_PIPELINES': {'finndata.pipelines.FinndataPipeline': 100}}
    name = 'finn'
    allowed_domains = ['finn.no']
    start_urls = ['https://www.finn.no/realestate/homes/search.html?filters=&location=0.20061']


    def parse(self, response):
        self.log('I just visited: ' + response.url)
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
        finnItems = FinnItems()
        try:
            finnItems['finn_code'] = response.css('span.u-select-all::text').extract_first(),
                # 'headline': response.css('h1.u-t2::text').extract_first().replace(",", " "),
            finnItems['address']  = response.css(
                    'p.u-caption::text').extract_first().replace(",", ";").replace(" Oslo", "").replace("; ", ";"),
            finnItems['total_price']= response.xpath(
                    "//dt[contains(., 'Totalpris')]/following-sibling::dd/text()").extract_first(
                    default=0).replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            finnItems['common_costs'] = response.xpath(
                    "//dt[contains(., 'Felleskost/mnd')]/following-sibling::dd/text()").extract_first(
                    default=0).replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            finnItems['for_sale_price'] = response.css(
                    'div.panel > span.u-t3::text').extract_first(default=0).replace(
                    "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            finnItems['ownership_form'] = response.xpath(
                    "//dt[contains(., 'Eieform')]/following-sibling::dd/text()").extract_first(default='N/A').replace(
                    "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            finnItems['building_type']  = response.xpath(
                    "//dt[contains(., 'Boligtype')]/following-sibling::dd/text()").extract_first(default='N/A'),
            finnItems['bedrooms'] = response.xpath(
                    "//dt[contains(., 'Soverom')]/following-sibling::dd/text()").extract_first(default=0),
            finnItems['pra']  = response.xpath(
                    "//dt[contains(., 'Primærrom')]/following-sibling::dd/text()").extract_first(default=0).replace(
                    "m²", ""),
            finnItems['year_built'] = response.xpath(
                    "//dt[contains(., 'Byggeår')]/following-sibling::dd/text()").extract_first(default=0).replace(
                    "\xa0", "").replace("\n", "").replace("kr", "").replace(" ", ""),
            finnItems['last_changed'] = response.xpath(
                    "//th[contains(., 'Sist endret')]/following-sibling::td/text()").extract_first(default='NaN'),
            finnItems['rooms'] = response.xpath(
                    "//dt[contains(., 'Rom')]/following-sibling::dd/text()").extract_first(
                    default=0).replace("\xa0", "").replace("\n", "").replace("kr", "").replace(" ", "")
        except Exception as e:
            print(e)

        #try:
            # finnItems['finn_code'] = finn_code
            # finnItems['address'] = address
            # finnItems['total_price'] = total_price
            # finnItems['common_costs'] = common_costs
            # finnItems['for_sale_price'] = for_sale_price
            # finnItems['ownership_form'] = ownership_form
            # finnItems['building_type'] = building_type
            # finnItems['bedrooms'] = bedrooms
            # finnItems['pra'] = pra
            # finnItems['year_built'] = year_built
            # finnItems['last_changed'] = last_changed
            # finnItems['rooms'] = rooms


        # except Exception as e:
        #     print(e)

        yield finnItems

        # yield {
        #         'finn_code': finn_code,
        #         'address': address,
        #         'total_price': total_price,
        #         'common_costs': common_costs,
        #         'for_sale_price': for_sale_price,
        #         'ownership_form': ownership_form,
        #         'building_type': building_type,
        #         'bedrooms': bedrooms,
        #         'pra': pra,
        #         'year_built': year_built,
        #         'last_changed': last_changed,
        #         'rooms': rooms
        #     }








    def closed(self, reason):
        filename = "/finnbolig_out.csv"
        subprocess.call(['open', filename])


