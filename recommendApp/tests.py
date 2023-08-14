from django.test import TestCase

# Create your tests here.
from haversine import haversine, Unit

if __name__ == "__main__":
    # 两点的经纬度
    point1 = (22.49761218985935, 113.89136859534268)
    point2 = (22.78670922490068, 114.31228572157245)
    result1 = haversine(point1, point2, unit=Unit.KILOMETERS)  # km
    result2 = haversine(point1, point2, unit=Unit.METERS)  # m
    # 打印计算结果
    print("距离：{:.3f}km".format(result1))
    print("距离：{:.3f}m".format(result2))