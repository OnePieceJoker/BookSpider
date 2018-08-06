# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItemLoader(ItemLoader):
    # 自定义item loader
    default_output_processor = TakeFirst()


def get_id(value):
    match_re = re.match(".*/(.*).htm", value)
    if match_re:
        return int(match_re.group(1))


class BookItem(scrapy.Item):
    bookname = scrapy.Field()  # 章节名
    chapter_id = scrapy.Field(
        output_processor=MapCompose(get_id)
    )  # 作为主键，方便排序
    label = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()  # 书名
