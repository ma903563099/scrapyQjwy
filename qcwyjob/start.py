#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl qcwy_demo".split())

# import json
# text = """
# {"code":0,"success":true,"msg":"0","data":[{"ip":"182.246.158.165","port":42263,"expire_time":"2019-03-28 14:39:06"},{"ip":"182.246.158.165","port":4263,"expire_time":"2019-03-28 14:39:06"},{"ip":"182.246.158.165","port":41263,"expire_time":"2019-03-28 14:39:06"}]}
# """
#
# categories = {data.get('ip'):data.get('port') for data in json.loads(text).get('data')}
#
# print(list(categories.values()))
# datas = json.loads(text).get("data",[])
# print(datas)