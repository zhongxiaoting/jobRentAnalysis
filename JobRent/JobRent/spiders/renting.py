import scrapy
from scrapy import Request
from ..items import Lianjia
from recommendApp.models import Renting


class JobSpider(scrapy.Spider):
    name = "renting"
    allowed_domains = ["sz.lianjia.com"]

    # 定义入口URL
    start_urls = ['https://sz.lianjia.com/zufang/pg1']   

    def start_requests(self):
        for i in range(1, 2):
            url = "https://sz.lianjia.com/zufang/pg" + str(i)
            yield Request(url=url) #用来获取页码

    def parse(self, response):
        rent_items = Lianjia()

        house_lists = response.xpath('//*[@id="content"]/div[1]/div[1]/div')

        for house_list in house_lists:
            addr1 = house_list.xpath('./div/p[2]/a[1]/text()').extract_first()
            
            if addr1:
                rent_items['area'] = addr1
                rent_items['house'] = house_list.xpath('./div/p[1]/a/text()').extract_first().strip()
                addr2 = house_list.xpath('./div/p[2]/a[2]/text()').extract_first().strip()
                addr3 = house_list.xpath('./div/p[2]/a[3]/text()').extract_first().strip()
                rent_items['addr'] = addr1 + addr2 + addr3
                area = house_list.xpath('./div/p[2]/text()[5]').extract_first().strip()
                direction = house_list.xpath('./div/p[2]/text()[6]').extract_first().strip()
                pattern = house_list.xpath('./div/p[2]/text()[7]').extract_first().strip()
                rent_items['area_d_p'] = area + direction + pattern
                rent_items['price'] = house_list.xpath('./div/span/em/text()').extract_first().strip()

                Renting.objects.create(house=rent_items['house'], area=rent_items['area'], addr=rent_items['addr'],
                                   area_d_p=rent_items['area_d_p'], price=rent_items['price'])
                # yield job_items
                print(rent_items)


