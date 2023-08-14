# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobrentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobQianCheng(scrapy.Item):
    # define the fields for your item here like
    company_name = scrapy.Field()  # 公司名
    job_name = scrapy.Field()  # 岗位
    job_area = scrapy.Field()  # 地点
    provide_salary = scrapy.Field()  # 薪资
    work_year = scrapy.Field()  # 经验
    degree = scrapy.Field()  # 学历
    job_tags = scrapy.Field()  # 福利
    industry_type = scrapy.Field()  # 公司行业
    issue_date = scrapy.Field()   # 岗位发布时间


class Lianjia(scrapy.Item):
    house = scrapy.Field()       # 小区名称/地点  格局，如：1室1厅 坐向，如：西
    area = scrapy.Field()
    addr = scrapy.Field()        # 房子所在地点
    area_d_p = scrapy.Field()    # 大小坐向格局
    price = scrapy.Field()       # 租金

    

    
