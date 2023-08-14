from recommendApp.models import Job
from recommendApp.models import Renting
from recommendApp.geocoding import get_coord


# 返回经纬度
def houses_filter(houses, j):
    house_message = houses[j]
    house_area = house_message['addr']
    house_id = house_message['id']
    house = house_message['house']

    # 过滤掉已经有经纬度的值
    location_isnull = Renting.objects.filter(id=house_id, lat__isnull=True)

    if location_isnull:
        coord = get_coord(house_area)
        # print(coord)
        lng = coord['result']['location']['lng']
        lat = coord['result']['location']['lat']

        # 更新数据库中没有经纬度的数据
        location_isnull.update(lng=lng, lat=lat)
        print("房子数据表的经纬度更新成功！")

    house_lng = house_message['lng']
    house_lat = house_message['lat']
    return house, house_lng, house_lat
