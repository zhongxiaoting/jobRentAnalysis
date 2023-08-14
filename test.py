import json

import requests

custom_settings = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "uid=wKhJC2RFO1xAAkxHFvHEAg==; guid=14704099285ec9a03c733226d26b4569; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2214704099285ec9a03c733226d26b4569%22%2C%22first_id%22%3A%22187aee9042576e-0c52e00b3cc0708-26031b51-1327104-187aee90426640%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3YWVlOTA0MjU3NmUtMGM1MmUwMGIzY2MwNzA4LTI2MDMxYjUxLTEzMjcxMDQtMTg3YWVlOTA0MjY2NDAiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxNDcwNDA5OTI4NWVjOWEwM2M3MzMyMjZkMjZiNDU2OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2214704099285ec9a03c733226d26b4569%22%7D%2C%22%24device_id%22%3A%22187aee9042576e-0c52e00b3cc0708-26031b51-1327104-187aee90426640%22%7D; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60040000%7C%21recentSearch0%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; slife=lastvisit%3D040000%26%7C%26; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DckwO92LYPBCUGwYB8ZL0QrH-nHVW1QkT2yCEVXdUmC7%26wd%3D%26eqid%3Da42b8920000075b00000000664623a2d%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1684159026; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1682254132,1682340098,1683127838,1684159025; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1684159025; acw_tc=ac11000116841590324176305e00ded31f750968e4d23c0983df5e39715f35; acw_sc__v2=64623cc7b08d4aae830e0f73490c83529cf8eb59; JSESSIONID=6D271FFD4F21ED6D6DE84A7E6C563258; ssxmod_itna=YqIx0DnDyDcD2DjrEDzhCnYDvdnB7DR2rdn3qGNi3DZDiqAPGhDC+4KruG807G2GKPADbYqq4iiEx44WznGbh5WKfRw4GLDmKDyYQG+K3D4+KGwD0eG+DD4DWDmWHDnxAQDjxGp9uXwV=Dm4GW8qGfDDoDYf6uDitD4qDBCOdDKqGg8q+z8T26CntdEwDP10h9D0tQxBdK7cG9mjcH=GNPdZnxrgQDzLHDtqNMSLddx0PBldXxg2ExiG+1K7QKWhDb4xxqb38i7iqrStwrW0Dqi+h00759xD3w8HD===; ssxmod_itna2=YqIx0DnDyDcD2DjrEDzhCnYDvdnB7DR2rdn4A6Ti5D/7IDFODhxzccKKh1AFxIiYPvDQIxFDFqG7KeD=",
    "Host": "cupidjob.51job.com",
    "Referer": "https://cupidjob.51job.com/open/noauth/search-pc?api_key=51job&timestamp=1684245923&keyword=&searchType=2&function=&industry=&jobArea=040000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
data = requests.get("https://cupidjob.51job.com", params=json.dumps(custom_settings))
print(data.text)


