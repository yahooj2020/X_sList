#! -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import wget
import os
import urllib.request
import subprocess



def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def mkdir(path):
    # 引入模块
    import os

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

        return False

def parse_html(html):
    lpath = os.getcwd()
    selector = etree.HTML(html)
    patt = re.compile('<h1><span itemprop="name">(.*?)</span>(.*?)</h1>',re.S)
    infos = re.findall(patt,html)
    # 目录剔除空格 linux下的目录不一样
    f_path = lpath +"/"+ "".join(infos[0]).replace('(','').replace(')','').replace('/','')
    fpic_path = "".join(f_path.split())

    mkdir(fpic_path)
    links = selector.xpath('//*[@id="gallery"]/a/img/@src')
    print(infos)
    print(fpic_path)
    print(links)
    for one_url in links:

        cmd = 'wget -P {0} {1}'.format(fpic_path,one_url)
        subprocess.call(cmd, shell=True)

        print(cmd)






if __name__ == "__main__":
    for num in range(1,10000):

        url = 'https://xslist.org/zh/model/{0}.html'.format(num)
        print(url)
        try:

            html = get_one_page(url)
            parse_html(html)
            time.sleep(2)
        except:
            pass
