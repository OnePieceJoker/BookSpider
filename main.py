# -*- coding: utf-8 -*-
__author__ = "Mr.Joker"
# @Time     : 2018.1.25 8:57
# @File     : main.py
# @Software : PyCharm   

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "biquge"])