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




def parse_html(html):
    lpath = os.getcwd()
    selector = etree.HTML(html)
    patt = re.compile('<h1><span itemprop="name">(.*?)</span>(.*?)</h1>',re.S)
    infos = re.findall(patt,html)
    # 目录剔除空格 linux下的目录不一样
    f_path = lpath +"/"+ "".join(infos[0]).replace('(','').replace(')','').replace('/','')
    ff_path = "".join(f_path.split())

    isExists = os.path.exists(ff_path)
        if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(isExists)

        print(isExists + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(isExists + ' 目录已存在')
    
    links = selector.xpath('//*[@id="gallery"]/a/img/@src')


    for one_url in links:

        cmd = 'wget -P {0} {1}'.format(f_path,one_url)
        subprocess.call(cmd, shell=True)

        print(cmd)


    #直接用subprocess即可，不用但粗创建txt
    # if os.path.exists(r"t1.txt") == True:
    #     os.remove(r"t1.txt")
    # else:
    #     pass
    #
    # # 保存成txt文档，然后想办法用python调用bash来处理
    # for single_pic in links:
    #     try:
    #
    #         with open('t1.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
    #             file_handle.write(single_pic)     # 写入
    #             file_handle.write('\n')                      # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
    #
    #
    #     except:
    #         pass
    #
    #




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


