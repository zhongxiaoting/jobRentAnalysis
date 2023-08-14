import json

from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recommendApp.models import Job
from recommendApp.models import Renting
from recommendApp.geocoding import get_coord
from recommendApp.common import houses_filter
from django.db.models import Q
from haversine import haversine, Unit
from django.core.paginator import Paginator
# Create your views here.

"""
    1. 调用百度地图API计算工作与租房的距离，并返回距离最小的两个值
    2. 根据岗位所在区检索出所在区的所有房子然后排序
"""


# 所有岗位信息
@api_view(['GET'])
def job_lists(request):
    data = {}
    job_list = Job.objects.all()
    # 10为每页多少数据
    paginator = Paginator(job_list, 5)
    # 获取 url 中的页码
    page_num = request.GET.get('page')
    # 将导航对象对应的页码内容返回给 page
    page = paginator.get_page(page_num)

    data['has_previous'] = page.has_previous()
    data['has_next'] = page.has_next()
    # 是否存在上一页
    if page.has_previous():
        data['previous_page_number'] = page.previous_page_number()
    else:
        None
    # 是否存在下一页
    if page.has_next():
        data['next_page_number'] = page.next_page_number()
    else:
        None
    data['page'] = page.number
    data['num_pages'] = page.paginator.num_pages
    data['object_list'] = page.object_list.values()
    response_data = data
    return Response(response_data, status=status.HTTP_200_OK)


# 所有租房信息
@api_view(['GET'])
def house_lists(request):
    data = {}
    house_list = Renting.objects.all()
    paginator = Paginator(house_list, 5)
    # 获取url中的页码
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    data['has_previous'] = page.has_previous()
    data['has_next'] = page.has_next()
    if page.has_previous():
        data['previous_page_number'] = page.previous_page_number()
    else:
        None
    if page.has_next():
        data['next_page_number'] = page.next_page_number()
    else:
        None
    data['page'] = page.number
    data['num_pages'] = page.paginator.num_pages
    data['object_list'] = page.object_list.values()
    response_data = data
    return Response(response_data, status=status.HTTP_200_OK)


# 岗位搜索功能
@api_view(['GET'])
def job_search(request):
    data = {}
    search = request.GET.get('search')

    job_list = Job.objects.filter(Q(job_area__icontains=search) | Q(company_name__icontains=search) | Q(job_name__icontains=search)
                                  | Q(work_year__icontains=search) | Q(degree__icontains=search) | Q(provide_salary__icontains=search)
                                  | Q(industry_type__icontains=search)).values()

    job_keyword = "关于 " + '"' + search + '"' + " 的搜索结果"

    # paginator = Paginator(job_list, 5)
    # # 获取url中的页码
    # page_num = request.GET.get('page')
    # page = paginator.get_page(page_num)
    # data['has_previous'] = page.has_previous()
    # data['has_next'] = page.has_next()
    # if page.has_previous():
    #     data['previous_page_number'] = page.previous_page_number()
    # else:
    #     None
    # if page.has_next():
    #     data['next_page_number'] = page.next_page_number()
    # else:
    #     None
    # data['page'] = page.number
    # data['num_pages'] = page.paginator.num_pages
    # data['object_list'] = page.object_list.values()

    if job_list:
        # response_data = {"job_keyword": job_keyword, "job_lists": data}
        response_data = {"job_keyword": job_keyword, "job_lists": job_list}
    else:
        job_list = "没有找到相关搜索"
        response_data = {"job_keyword": job_keyword, "job_lists": job_list}
    return Response(response_data, status=status.HTTP_200_OK)


# 房源搜索功能
@api_view(['GET'])
def house_search(request):
    search = request.GET.get('search')

    house_list = Renting.objects.filter(Q(area__icontains=search) | Q(house__icontains=search) | Q(area_d_p__icontains=search)
                                  | Q(price=search) | Q(addr__icontains=search)).values()

    house_keyword = "关于 " + '"' + search + '"' + " 的搜索结果"

    # paginator = Paginator(job_list, 5)
    # # 获取url中的页码
    # page_num = request.GET.get('page')
    # page = paginator.get_page(page_num)
    # data['has_previous'] = page.has_previous()
    # data['has_next'] = page.has_next()
    # if page.has_previous():
    #     data['previous_page_number'] = page.previous_page_number()
    # else:
    #     None
    # if page.has_next():
    #     data['next_page_number'] = page.next_page_number()
    # else:
    #     None
    # data['page'] = page.number
    # data['num_pages'] = page.paginator.num_pages
    # data['object_list'] = page.object_list.values()

    if house_list:
        response_data = {"house_keyword": house_keyword, "house_lists": house_list}
    else:
        house_list = "没有找到相关搜索"
        response_data = {"house_keyword": house_keyword, "house_list": house_list}
    return Response(response_data, status=status.HTTP_200_OK)


# 岗位推荐房源信息
@api_view(['GET'])
def house_recommand(request):
    house_result = []
    data = {}
    job_list = Job.objects.all()

    # 10为每页多少数据
    paginator = Paginator(job_list, 5)
    # 获取 url 中的页码
    page_num = request.GET.get('page')
    # 将导航对象对应的页码内容返回给 page
    page = paginator.get_page(page_num)

    data['has_previous'] = page.has_previous()
    data['has_next'] = page.has_next()
    if page.has_previous():
        data['previous_page_number'] = page.previous_page_number()
    else:
        None
    if page.has_next():
        data['next_page_number'] = page.next_page_number()
    else:
        None
    data['page'] = page.number
    data['num_pages'] = page.paginator.num_pages
    job_obj = page.object_list.values()
    data_num = len(job_obj)
    for i in range(data_num):
        job = job_obj[i]
        min_house_id = job['min_house_id']
        sec_house_id = job['sec_house_id']
        min_house = Renting.objects.filter(id=min_house_id).values()
        sec_house = Renting.objects.filter(id=sec_house_id).values()
        job['min_house'] = min_house
        job['sec_house'] = sec_house
        house_result.append(job)
    data['object_list'] = house_result
    response_data = data
    return Response(response_data, status=status.HTTP_200_OK)


# 更新所有岗位和房子的经纬度
@api_view(['GET'])
def update_job_house(request):
    not_shenzhen = Job.objects.exclude(job_area__icontains='深圳').delete()

    job_obj = Job.objects.filter(lng__isnull=True).values()
    job_num = len(job_obj)
    for i in range(job_num):
        id = job_obj[i]['id']
        job = Job.objects.filter(id=id)
        company_name = job_obj[i]['company_name']
        coord = get_coord(company_name)
        # print(id, company_name, coord)

        lng = coord['result']['location']['lng']
        lat = coord['result']['location']['lat']

        # 更新数据库中没有经纬度的数据
        print(company_name, lng, lat)
        job.update(lng=lng, lat=lat)

    print("岗位数据表的经纬度更新成功！")

    house_obj = Renting.objects.filter(lat__isnull=True).values()
    house_num = len(house_obj)
    for j in range(house_num):
        id = house_obj[j]['id']
        house = Renting.objects.filter(id=id)
        addr = house_obj[j]['addr']
        coord = get_coord(addr)
        lng = coord['result']['location']['lng']
        lat = coord['result']['location']['lat']

        house.update(lng=lng, lat=lat)
        print("租房数据表的经纬度更新成功！")
    response_data = {"house_list": "岗位数据表的经纬度更新成功！租房数据表的经纬度更新成功！"}
    return Response(response_data)


# 计算岗位的最小距离和第二距离
@api_view(['GET'])
def jisuan(request):
    # 根据新增岗位更新距离
    job_distance = "没有新加的岗位和房源！"

    job_dis = Job.objects.filter(min_distance__isnull=True, lat__isnull=False).values()
    job_num = len(job_dis)
    for i in range(job_num):

        distance_l = {}
        company_name = job_dis[i]['company_name']
        id = job_dis[i]['id']
        job_lat = float(job_dis[i]['lat'])
        job_lng = float(job_dis[i]['lng'])
        point1 = (job_lat, job_lng)

        job_area = job_dis[i]['job_area'][3:]
        if job_area:
            houses = Renting.objects.filter(area=job_area, lat__isnull=False).values()

        else:
            houses = Renting.objects.all().values()

        houses_num = len(houses)
        print(job_area)
        for j in range(houses_num):
            house = houses[j]
            house_lat = float(house['lat'])
            house_lng = float(house['lng'])
            point2 = (house_lat, house_lng)
            distance = haversine(point1, point2, unit=Unit.KILOMETERS)
            # distance_r.append(distance)
            distance_l[distance] = house
        dis_sort = sorted(distance_l.items(), key=lambda x: x[0], reverse=False)
        # print(dis_sort)

        min_dis = dis_sort[0][0]
        sec_dis = dis_sort[1][0]
        min_dis_id = dis_sort[0][1]['id']
        sec_dis_id = dis_sort[1][1]['id']
        job_obj = Job.objects.get(id=id)
        if job_obj:
            job_obj.min_distance = min_dis
            job_obj.sec_distance = sec_dis
            job_obj.min_house_id = min_dis_id
            job_obj.sec_house_id = sec_dis_id
            job_obj.save()
        job_distance = "根据新增岗位更新距离成功！"

    # 根据新增房源区域更新同区域所有岗位与房源的距离
    # 新增房源并且经纬度已经计算, 0代表新增加的房子
    is_created = Renting.objects.filter(created=0, lng__isnull=False).values()
    house_is_num = len(is_created)
    for j in range(house_is_num):

        created_houses = is_created[j]
        c_hous_id = created_houses['id']
        area = created_houses['area']
        h_created_lat = float(created_houses['lat'])
        h_created_lng = float(created_houses['lng'])
        # 找到新增的房子，将房子新加记录改为1，表示不是新加
        c_house = Renting.objects.filter(id=c_hous_id)
        c_house.update(created=1)
        created_point1 = (h_created_lat, h_created_lng)
        # 找出同区的岗位
        area = "深圳·" + area
        job_sec = Job.objects.filter(job_area=area).values()
        job_is_num = len(job_sec)
        for k in range(job_is_num):
            c_job = job_sec[k]
            c_id = c_job['id']
            c_min_dis = c_job['min_distance']
            c_sec_dis = c_job['sec_distance']
            j_created_lat = float(c_job['lat'])
            j_created_lng = float(c_job['lng'])
            created_point2 = (j_created_lat, j_created_lng)
            c_distance = haversine(created_point1, created_point2, unit=Unit.KILOMETERS)
            # 如果新增房子与岗位的距离比之前的最短距离小更新
            if c_distance < float(c_min_dis):
                c_job_obj = Job.objects.get(id=c_id)
                if c_job_obj:
                    c_job_obj.min_distance = c_distance
                    c_job_obj.min_house_id = c_hous_id
                    c_job_obj.save()
                job_distance = "根据新增房源更新距离成功！"
            # 如果新增房子与岗位的距离比之前的第二短距离小更新
            if float(c_min_dis) < c_distance < float(c_sec_dis):
                c_job_obj = Job.objects.get(id=c_id)
                if c_job_obj:
                    c_job_obj.sec_distance = c_distance
                    c_job_obj.sec_house_id = c_hous_id
                    c_job_obj.save()
                job_distance = "根据新增房源更新距离成功！"
    response_data = {"job_distance": job_distance}
    return Response(response_data)




