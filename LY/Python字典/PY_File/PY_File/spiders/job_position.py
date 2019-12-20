# -*- coding: utf-8 -*-
import scrapy
from PY_File.items import PyFileItem

class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/data/caibao']
    def parse(self, response):
        for job_prirnary in response.xpath ('//div[@class="fn_rp_list"]/table[@class="fn_cm_table"]/tr'):
            item = PyFileItem()
            item['Nuber']=job_prirnary.xpath('./td[1]/text()').re(r'(\d+)')
            item['fodecode'] = job_prirnary.xpath('./td[2]/a/text()').extract()
            item['Name'] = job_prirnary.xpath('./td[3]/a/text()').extract()
            item['Type'] = job_prirnary.xpath('./td[4]/text()').extract()
            t='20-30'
            s=job_prirnary.xpath('./td[5]/text()').re(r'(\d+)')
            item['ReportDate'] =s
            item['Abstract'] = job_prirnary.xpath('./td[6]/text()').extract()
            item['DeclarationDate'] = job_prirnary.xpath('./td[7]/text()').re(r'^\d{4}-\d{1,2}-\d{1,2}')
            yield item

        new_links = response.xpath('//a[contains(text(), "下一页")]/@href').extract()

        if new_links and len(new_links) > 0:
            new_link = new_links[0]
            yield scrapy.Request("http://quotes.money.163.com" + new_link, callback=self.parse)