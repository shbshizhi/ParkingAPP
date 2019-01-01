import requests
import re
import random
from parking import DBoprate


parameter = {
        "newmap": "1",
        "reqflag": "pcmap",
        "biz": "1",
        "from": "webmap",
        "da_par": "direct",
        "pcevaname": "pc4.1",
        "qt": "con",
        "c": "315",            # 城市代码
        "wd": "南航将军路校区周边 停车场",       # 搜索关键词
        "wd2": "",
        "pn": "0",           # 页数
        "nn": "0",
        "db": "0",
        "sug": "0",
        "addr": "0",
        "da_src": "pcmappg.poi.page",
        "on_gel": "1",
        "src": "7",
        "gr": "3",
        "l": "12",
        "tn": "B_NORMAL_MAP",
        # "u_loc": "12621219.536556,2630747.285024",
        "ie": "utf-8",
        # "b": "(11845157.18,3047692.2;11922085.18,3073932.2)",  #这个应该是地理位置坐标，可以忽略
        "t": "1468896652886"
    }

TBName = "parking_info.plot_info"
url = 'http://map.baidu.com/'
DBoprate.DBTruncate(TBName)

for i in range(0,100):
    val_pn = i
    val_nn = i * 10
    parameter['pn'] = str(val_pn)
    parameter['nn'] = str(val_nn)

    htm = requests.get(url, params=parameter)
    htm = htm.text.encode('latin-1').decode('unicode_escape')  # 转码
    pattern = r'(?<=\baddress_norm":"\[).+?(?="ty":)'
    htm = re.findall(pattern, htm)  # 按段落匹配
    count = 1
    for r in htm:
        # pattern = r'(?<=\b"\},"name":").+?(?=")'
        # name = re.findall(pattern, r)
        # if not name:
        #     pattern = r'(?<=\b,"name":").+?(?=")'
        #     name = re.findall(pattern, r)
        #     print(name)  # 名称
        pattern = r'(?<="name":").+?(?=")'
        name = re.findall(pattern, r)
        str_name = name[0]
        # print(str_name)

        pattern = r'.+?(?=")'
        adr = re.findall(pattern, r)
        pattern = r'\(.+?\['
        address = re.sub(pattern, ' ', adr[0])
        pattern = r'\(.+?\]'
        address = re.sub(pattern, ' ', address)
        # print(address)  # 地址

        pattern = r'(?<="price":").+?(?=")'
        price = re.findall(pattern, r)
        if len(price) > 0:
            str_price = price[0]
        else:
            str_price = ""
        # print(str_price)

        pattern = r'(?<="poi_address":").+?(?=")'
        poi_address = re.findall(pattern, r)
        # print(poi_address[0])

        # pattern = r'(?<="phone":").+?(?=")'
        # phone = re.findall(pattern, r)
        # print(phone)

        if str_name == "停车场" or str_name == "地下车库" or str_name == "路侧停车位":
            str_name = poi_address[0] + "-" + str_name
        empty = str(random.randint(0, 30))
        val = "(" + "'" + str_name + "'" + "," + "'" + address + "'" + "," + "'" + str_price + "'" + "," + empty + ")"
        # print(val)
        DBoprate.DBInsert(TBName, val)
        if count == 10: break
        count = count + 1

