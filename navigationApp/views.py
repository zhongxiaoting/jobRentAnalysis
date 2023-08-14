from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from haversine import haversine, Unit
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from recommendApp.models import Job
from recommendApp.models import Renting


# 计算出一个岗位中所有同区房子的距离排序
@api_view(['GET'])
def job_house_list(request, id):
    distance_r = []
    data = {}
    distance_l = {}
    job_obj = Job.objects.filter(id=id).values()
    # print(job_obj)
    company_name = job_obj[0]['company_name']
    job_area = job_obj[0]['job_area'][-3:]
    job_lng = float(job_obj[0]['lng'])
    job_lat = float(job_obj[0]['lat'])
    point1 = (job_lat, job_lng)
    houses = Renting.objects.filter(area=job_area, lat__isnull=False).values()
    houses_num = len(houses)
    for i in range(houses_num):
        house = houses[i]
        house_lng = float(house['lng'])
        house_lat = float(house['lat'])
        point2 = (house_lat, house_lng)
        distance = haversine(point1, point2, unit=Unit.KILOMETERS)
        distance_r.append(distance)
        distance_l[distance] = house
    dis_sort = sorted(distance_l.items(), key=lambda x: x[0], reverse=False)

    # 分页
    page_number = request.GET.get('page')
    paginator = Paginator(dis_sort, 5)
    page = paginator.get_page(page_number)

    data['has_previous'] = page.has_previous()
    data['has_next'] = page.has_next()
    data['previous_page_number'] = page.previous_page_number() if page.has_previous() else None
    data['next_page_number'] = page.next_page_number() if page.has_next() else None
    data['number'] = page.number
    data['num_pages'] = page.paginator.num_pages
    data['object_list'] = page
    response_data = data
    return Response(response_data)


# 地图导航，起点：房子，终点：岗位
def get_path():
    pass



