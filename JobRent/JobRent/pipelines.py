# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from cursor import cursor
import pymysql


class JobrentPipeline:
    def process_item(self, item, spider):
        db = pymysql.connect(host="localhost", user="root", password="zhongxiaoting", db="jobrent", charset="utf-8")
        cursor = db.cursor()
        company_name = item['company_name'][0]
        job_name = item['job_name'][0]
        job_area = item['job_area'][0]
        provide_salary = item['provide_salary'][0]
        work_year = item['work_year'][0]
        degree = item['degree'][0]
        job_tags = item['job_tags'][0]
        industry_type = item['industry_type'][0]
        cursor.execute('INSERT INTO nba(球员,球队,排名,场均得分,命中率,三分命中率,罚球命中率) VALUES (%s,%s,%s,%s,%s,%s,%s)',
            (球员, 球队, 排名, 场均得分, 命中率, 三分命中率, 罚球命中率))
        return item

 
class HptyPipeline:
    def process_item(self, item, spider):
        db = pymysql.connect(host="Localhost", user="root", passwd="root", db="sww", charset="utf8")
        cursor = db.cursor()
        球员 = item["球员"][0]
        球队 = item["球队"][0]
        排名 = item["排名"][0]
        场均得分 = item["场均得分"][0]
        命中率 = item["命中率"]
        三分命中率 = item["三分命中率"][0]
        罚球命中率 = item["罚球命中率"][0]
        # 三分命中率 = item["三分命中率"][0].strip('%')
        # 罚球命中率 = item["罚球命中率"][0].strip('%')
 
        cursor.execute(
            'INSERT INTO nba(球员,球队,排名,场均得分,命中率,三分命中率,罚球命中率) VALUES (%s,%s,%s,%s,%s,%s,%s)',
            (球员, 球队, 排名, 场均得分, 命中率, 三分命中率, 罚球命中率)
        )
        # 对事务操作进行提交
        db.commit()
        # 关闭游标
        cursor.close()
        db.close()
        return item