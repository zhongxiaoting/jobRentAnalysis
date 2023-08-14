# encoding:utf-8
import requests


# 调用百度接口获取地点经纬度
def get_coord(area):
    # 接口地址
    url = "https://api.map.baidu.com/geocoding/v3"

    # 此处填写你在控制台-应用管理-创建应用后获取的AK
    ak = "uXGUGObSZRwHmZKHGMYy1AImnpiMAI6z"

    params = {
        "address":    area,
        "output":    "json",
        "ak":       ak,

    }

    response = requests.get(url=url, params=params)
    if response:
        return response.json()
    else:
        return