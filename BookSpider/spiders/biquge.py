# -*- coding: utf-8 -*-
import scrapy
from BookSpider.items import BookItem,BookItemLoader
from scrapy.http import Request
from urllib import parse


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.nbzww.org']
    start_urls = ['https://www.nbzww.org/xiaoshuo-34278/mulu.htm']

    def parse(self, response):
        '''
        去到目录页拿到所有章节的url并解析
        #list > dl:nth-child(1) > dt:nth-child(12)
        #list > dl:nth-child(1) > dt:nth-child(12)
        #list > dl:nth-child(1) > dd:nth-child(13) > a:nth-child(1)
        /html/body/div/div[6]/div/dl/dt[2]
        #list > dl > dd:nth-child(28)
        //*[@id="list"]/dl/dd[11]
        '''
        post_nodes = response.css("#chapters-list li a")
        # post_urls = post_urls[9:]  # 切片获取正文章节
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

    def parse_detail(self, response):
        book_item = BookItem()
        # bookname = response.css(".bookname h1::text").extract_first()
        # label = response.css(".con_top a::text").extract()[1]
        # content = response.css("#content::text").extract_first()
        item_loader = BookItemLoader(item=BookItem(), response=response)
        item_loader.add_css("bookname", "#h1 h1::text")
        item_loader.add_value("chapter_id", response.url)
        item_loader.add_css("label", ".breadcrumb li:nth-child(2) a::text")
        item_loader.add_css("content", "#txtContent")
        item_loader.add_value("author", "荣小荣")
        item_loader.add_css("title", "#h1 small a::text")

        book_item = item_loader.load_item()

        yield book_item
