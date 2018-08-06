# -*- coding: utf-8 -*-
__author__ = "Mr.Joker"
# @Time     : 2018.1.25 12:25
# @File     : proxymiddlewares.py
# @Software : PyCharm   

import random, base64


class ProxyMiddleware(object):
    proxyList = [ \
        '218.20.218.79:8118', '42.231.165.132:8118', '120.15.159.105:9000',
        '222.64.36.145:9999', '61.50.244.179:808', '223.241.117.107:8010',
        '121.199.42.198:3129', '49.89.87.13:47528', '183.30.197.214:9797'
    ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr