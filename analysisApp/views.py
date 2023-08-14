from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.decorators import api_view
from recommendApp.models import Job
from recommendApp.models import Renting

# Create your views here.

'''工作与房源的分析页面'''


# 每一个区房子的占比率
@api_view(['GET'])
def job_analysis(request):
    """
    每一个区的岗位占总深圳岗位的比率
    :param request:
    :return:
    """
    job = Job.objects.all()
    job_sum = len(job)

    # 岗位在南山区的数量占比
    job_nanshan = Job.objects.filter(job_area="深圳·南山区")
    nanshan_num = len(job_nanshan)
    ratio_nanshan = nanshan_num / job_sum
    nanshan_per = round(ratio_nanshan, 4) * 100

    # 岗位在福田区的数量占比
    job_futian = Job.objects.filter(job_area="深圳·福田区")
    futian_num = len(job_futian)
    ratio_futian = futian_num / job_sum
    futian_per = round(ratio_futian, 4) * 100

    # 岗位在罗湖区的数量占比
    job_luohu = Job.objects.filter(job_area="深圳·罗湖区")
    luohu_num = len(job_luohu)
    ratio_luohu = luohu_num / job_sum
    luohu_per = round(ratio_luohu, 4) * 100

    # 岗位在龙岗区的数量占比
    job_longgang = Job.objects.filter(job_area="深圳·龙岗区")
    longgang_num = len(job_longgang)
    ratio_longgang = longgang_num / job_sum
    longgang_per = round(ratio_longgang, 4) * 100

    # 岗位在龙华区的数量占比
    job_longhua = Job.objects.filter(job_area="深圳·龙华区")
    longhua_num = len(job_longhua)
    ratio_longhua = longhua_num / job_sum
    longhua_per = round(ratio_longhua, 4) * 100

    # 岗位在宝安区的数量占比
    job_baoan = Job.objects.filter(job_area="深圳·宝安区")
    baoan_num = len(job_baoan)
    ratio_baoan = baoan_num / job_sum
    baoan_per = round(ratio_baoan, 4) * 100

    # 岗位在光明区的数量占比
    job_guangming = Job.objects.filter(job_area="深圳·光明区")
    guangming_num = len(job_guangming)
    ratio_guangming = guangming_num / job_sum
    guangming_per = round(ratio_guangming, 4) * 100

    # 岗位在坪山区的数量占比
    job_pingshan = Job.objects.filter(job_area="深圳·坪山区")
    pingshan_num = len(job_pingshan)
    ratio_pingshan = pingshan_num / job_sum
    pingshan_per = round(ratio_pingshan, 4) * 100

    # 岗位在盐田区的数量占比
    job_yantian = Job.objects.filter(job_area="深圳·盐田区")
    yantian_num = len(job_yantian)
    ratio_yantian = yantian_num / job_sum
    yantian_per = round(ratio_yantian, 4) * 100

    # 岗位在深圳其他地区的数量占比
    others = 100 - nanshan_per - futian_per - luohu_per - longgang_per - longhua_per - baoan_per - guangming_per - pingshan_per - yantian_per

    response_data = {"nanshan_per": nanshan_per, "futian_per": futian_per, "luohu_per": luohu_per, "longgang_per": longgang_per, "longhua_per": longhua_per,
                     "baoan_per": baoan_per, "guangming_per": guangming_per, "pingshan_per": pingshan_per, "yantian_per": yantian_per, "others": others}
    return Response(response_data)


# 每一个区房子的占比率
@api_view(['GET'])
def house_analysis(request):
    house = Renting.objects.all()
    house_sum = len(house)

    # 房子在南山区的数量占比
    house_nanshan = Renting.objects.filter(area="南山区")
    nanshan_num = len(house_nanshan)
    ratio_nanshan = nanshan_num / house_sum
    h_nanshan_per = round(ratio_nanshan, 4) * 100

    # 房子在福田区的数量占比
    house_futian = Renting.objects.filter(area="福田区")
    futian_num = len(house_futian)
    ratio_futian = futian_num / house_sum
    h_futian_per = round(ratio_futian, 4) * 100

    # 房子在罗湖区的数量占比
    house_luohu = Renting.objects.filter(area="罗湖区")
    luohu_num = len(house_luohu)
    ratio_luohu = luohu_num / house_sum
    h_luohu_per = round(ratio_luohu, 4) * 100

    # 房子在龙岗区的数量占比
    house_longgang = Renting.objects.filter(area="龙岗区")
    longgang_num = len(house_longgang)
    ratio_longgang = longgang_num / house_sum
    h_longgang_per = round(ratio_longgang, 4) * 100

    # 房子在龙华区的数量占比
    house_longhua = Renting.objects.filter(area="龙华区")
    longhua_num = len(house_longhua)
    ratio_longhua = longhua_num / house_sum
    h_longhua_per = round(ratio_longhua, 4) * 100

    # 房子在宝安区的数量
    house_baoan = Renting.objects.filter(area="宝安区")
    baoan_num = len(house_baoan)
    ratio_baoan = baoan_num / house_sum
    h_baoan_per = round(ratio_baoan, 4) * 100

    # 房子在光明区的数量占比
    house_guangming = Renting.objects.filter(area="光明区")
    guangming_num = len(house_guangming)
    ratio_guangming = guangming_num / house_sum
    h_guangming_per = round(ratio_guangming, 4) * 100

    # 房子在坪山区的数量占比
    house_pingshan = Renting.objects.filter(area="坪山区")
    pingshan_num = len(house_pingshan)
    ratio_pingshan = pingshan_num / house_sum
    h_pingshan_per = round(ratio_pingshan, 4) * 100

    # 房子在盐田区的数量占比
    house_yantian = Renting.objects.filter(area="盐田区")
    yantian_num = len(house_yantian)
    ratio_yantian = yantian_num / house_sum
    h_yantian_per = round(ratio_yantian, 4) * 100

    #房子在深圳其他地区的数量占比
    dapeng_num = house_sum - nanshan_num - futian_num - luohu_num - longgang_num - longhua_num - baoan_num - guangming_num - pingshan_num -yantian_num
    others = 100 - h_nanshan_per - h_futian_per - h_luohu_per - h_longgang_per - h_longhua_per - h_baoan_per - h_guangming_per - h_pingshan_per - h_yantian_per

    response_data = {"h_nanshan_per": h_nanshan_per, "h_futian_per": h_futian_per, "h_luohu_per": h_luohu_per,
                     "h_longgang_per": h_longgang_per, "h_longhua_per": h_longhua_per,
                     "h_baoan_per": h_baoan_per, "h_guangming_per": h_guangming_per, "h_pingshan_per": h_pingshan_per,
                     "h_yantian_per": h_yantian_per, "others": others,
                     "nanshan_num": nanshan_num, "futian_num": futian_num, "luohu_num": luohu_num, "longgang_num": longgang_num,
                     "longhua_num": longhua_num, "baoan_num": baoan_num, "guangming_num": guangming_num, "pingshan_num": pingshan_num,
                     "yantian_num": yantian_num, "dapeng_num": dapeng_num}
    return Response(response_data)


# 多少公里内岗位数
@api_view(['GET'])
def job_distance(request):
    """
    最近距离和第二近距离在几公里内的岗位数有多少
    :param request:
    :return:
    """
    # 最小距离与第二小距离在1公里内的岗位数
    min_one_value = Job.objects.filter(min_distance__lte=1).values()
    min_one_dis_num = len(min_one_value)
    sec_one_value = Job.objects.filter(sec_distance__lte=1).values()
    sec_one_dis_num = len(sec_one_value)


    # 最小距离与第二小距离在1到2公里内的岗位数
    min_sec_value = Job.objects.filter(min_distance__gt=1, min_distance__lte=2).values()
    min_sec_dis_num = len(min_sec_value)
    sec_sec_value = Job.objects.filter(sec_distance__gt=1, sec_distance__lte=2).values()
    sec_sec_dis_num = len(sec_sec_value)

    # 最小距离与第二小距离在2到3公里内的岗位数
    min_third_value = Job.objects.filter(min_distance__gt=2, min_distance__lte=3).values()
    min_third_dis_num = len(min_third_value)
    sec_third_value = Job.objects.filter(sec_distance__gt=2, sec_distance__lte=3).values()
    sec_third_dis_num = len(sec_third_value)

    # 最小距离与第二小距离在3到4公里内的岗位数
    min_four_value = Job.objects.filter(min_distance__gt=3, min_distance__lte=4).values()
    min_four_dis_num = len(min_four_value)
    sec_four_value = Job.objects.filter(sec_distance__gt=3, sec_distance__lte=4).values()
    sec_four_dis_num = len(sec_four_value)

    # 最小距离与第二小距离在4到8公里内的岗位数
    min_five_value = Job.objects.filter(min_distance__gt=4, min_distance__lte=8).values()
    min_five_dis_num = len(min_five_value)
    sec_five_value = Job.objects.filter(sec_distance__gt=4, sec_distance__lte=8).values()
    sec_five_dis_num = len(sec_five_value)

    # 最小距离与第二小距离在8到12公里内的岗位数
    min_six_value = Job.objects.filter(min_distance__gt=8, min_distance__lte=12).values()
    min_six_dis_num = len(min_six_value)
    sec_six_value = Job.objects.filter(sec_distance__gt=8, sec_distance__lte=12).values()
    sec_six_dis_num = len(sec_six_value)

    # 最小距离与第二小距离在12到25公里内的岗位数
    min_sev_value = Job.objects.filter(min_distance__gt=12, min_distance__lte=25).values()
    min_sev_dis_num = len(min_sev_value)
    sec_sev_value = Job.objects.filter(sec_distance__gt=12, sec_distance__lte=25).values()
    sec_sev_dis_num = len(sec_sev_value)

    # 25公里以上
    min_last_value = Job.objects.filter(min_distance__gt=25).values()
    min_last_dis_num = len(min_last_value)
    sec_last_value = Job.objects.filter(sec_distance__gt=25).values()
    sec_last_dis_num = len(sec_last_value)

    response_data = {"min_one_dis_num": min_one_dis_num, "min_sec_dis_num": min_sec_dis_num, "min_third_dis_num": min_third_dis_num, "min_four_dis_num": min_four_dis_num,
                     "min_five_dis_num": min_five_dis_num, "min_six_dis_num": min_six_dis_num, "min_sev_dis_num": min_sev_dis_num, "min_last_dis_num": min_last_dis_num,
                     "sec_one_dis_num": sec_one_dis_num, "sec_sec_dis_num": sec_sec_dis_num,
                     "sec_third_dis_num": sec_third_dis_num, "sec_four_dis_num": sec_four_dis_num,
                     "sec_five_dis_num": sec_five_dis_num, "sec_six_dis_num": sec_six_dis_num,
                     "sec_sev_dis_num": sec_sev_dis_num, "sec_last_dis_num": sec_last_dis_num
                     }

    return Response(response_data)

