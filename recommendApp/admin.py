from django.contrib import admin
from .models import Job, Renting
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_name', 'job_area', 'min_distance', 'sec_distance']


class RentingAdmin(admin.ModelAdmin):
    list_display = ['house', 'area', 'addr', 'area_d_p', 'price']


admin.site.register(Job, JobAdmin)

# 添加栏目
admin.site.register(Renting, RentingAdmin)


# 博客后台管理
admin.site.site_header = '工作租房联动系统后台管理'