from django.db import models

# Create your models here.


# job工作表
class Job(models.Model):
    company_name = models.CharField(max_length=60, null=True, verbose_name="公司名称")
    job_name = models.CharField(max_length=50, null=True, verbose_name="岗位")
    job_area = models.CharField(max_length=30, null=True, verbose_name="工作地点")
    provide_salary = models.CharField(max_length=30, null=True, verbose_name="薪资")
    work_year = models.CharField(max_length=20, null=True, verbose_name="工作经验")
    degree = models.CharField(max_length=30, null=True, verbose_name="学历")
    job_tags = models.CharField(max_length=500, null=True, verbose_name="要求与福利")
    industry_type = models.CharField(max_length=50, null=True, verbose_name="公司行业")
    lng = models.DecimalField(max_digits=18, decimal_places=14, null=True, blank=True, verbose_name="经度值")
    lat = models.DecimalField(max_digits=18, decimal_places=14, null=True, blank=True, verbose_name="纬度值")
    min_distance = models.FloatField(null=True, blank=True, verbose_name="最小距离")
    sec_distance = models.FloatField(null=True, blank=True, verbose_name="第二距离")
    min_house_id = models.IntegerField(null=True, blank=True, verbose_name="最小距离房子的id")
    sec_house_id = models.IntegerField(null=True, blank=True, verbose_name="第二距离房子的id")
    issue_date = models.CharField(max_length=30, null=True, verbose_name="发布时间")

    class Meta:
        verbose_name = "工作岗位表"
        verbose_name_plural = verbose_name
        ordering = ['-issue_date']
        db_table = "job"

    def __str__(self):
        return self.company_name


# 租房表
class Renting(models.Model):
    house = models.CharField(max_length=100, null=True, verbose_name="小区名称")
    area = models.CharField(max_length=50, null=True, verbose_name="所在区")
    addr = models.CharField(max_length=80, null=True, verbose_name="地点")
    area_d_p = models.CharField(max_length=100, null=True, verbose_name="大小坐向格局")
    price = models.CharField(max_length=25, null=True, verbose_name="租金")
    created = models.IntegerField(default=0, verbose_name="是否新增")
    lng = models.DecimalField(max_digits=18, decimal_places=14, null=True, verbose_name="经度值")
    lat = models.DecimalField(max_digits=18, decimal_places=14, null=True, verbose_name="纬度值")

    class Meta:
        verbose_name = "租房表"
        verbose_name_plural = verbose_name
        db_table = "renting"

    def __str__(self):
        return self.addr


