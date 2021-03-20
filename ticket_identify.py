import os
import sys
import cv2

from pylab import *
from PIL import Image
from OCR import identify


"""
    获取名字
"""


def get_name(img):
    img_pname = img[208:239, 243:318]
    img_name = "pictures/name.png"
    cv2.imwrite(img_name, img_pname)
    name = identify(img_name)
    return name


"""
    获取始发站
"""


def get_start(img):
    img_start = img[45:78, 49:150]
    img_name = "pictures/start.png"
    cv2.imwrite(img_name, img_start)
    start = identify(img_name)
    return start


"""
    获取目的地
"""


def get_end(img):
    img_end = img[46:85, 320:430]
    img_name = "pictures/end.png"
    cv2.imwrite(img_name, img_end)
    end = identify(img_name)
    return end


"""
    获取车次
"""


def get_trainID(img):
    img_trainID = img[50:96, 204:300]
    img_name = "pictures/trainID.png"
    cv2.imwrite(img_name, img_trainID)
    trainID = identify(img_name)
    return trainID


"""
    获取发车时间
"""


def get_start_time(img):
    img_start_time = img[100:133, 26:256]
    img_name = "pictures/start_time.png"
    cv2.imwrite(img_name, img_start_time)
    start_time = identify(img_name)
    return start_time


"""
    获取座位号
"""


def get_locate(img):
    img_locate = img[102:132, 309:420]
    img_name = "pictures/locate.png"
    cv2.imwrite(img_name, img_locate)
    locate = identify(img_name)
    return locate


"""
    获取价格
"""


def get_price(img):
    img_price = img[128:156, 51:115]
    img_name = "pictures/price.png"
    cv2.imwrite(img_name, img_price)
    price = identify(img_name)
    return price


"""
    输出到info.txt中
"""


def to_txt(img):
    name = get_name(img)
    start = get_start(img)
    end = get_end(img)
    trainID = get_trainID(img)
    start_time = get_start_time(img)
    locate = get_locate(img)
    price = get_price(img)

    with open('info.txt', 'w') as file:
        file.write("姓名:"+name+'\n'+"始发站:"+start+'\n'+"终点站:"+end+'\n'+"车次:" +
                   trainID+'\n'+"出发时间:"+start_time+'\n'+"座位号:"+locate+'\n'+"价格:"+price)

"""
    main()
"""

# 读取原图片
img = cv2.imread("ticket.png", 0)

# 识别并输出
to_txt(img)
