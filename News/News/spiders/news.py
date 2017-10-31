# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
from News.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tieba.baidu.com']
    url1 = 'https://tieba.baidu.com/f?kw=%E6%B0%94%E8%B1%A1&ie=utf-8&'
    pn=0
    start_urls = [url1 + str(pn)]


    def parse(self, response):
       #先抓取第一页
       base_url = 'https://tieba.baidu.com'
       node_list = response.xpath('//div[@class="threadlist_lz clearfix"]')

       print(node_list)


       # for node in node_list:
       #
       #     temp_link = base_url + node
       #
       #     res = requests.get(temp_link)
       #     soup = BeautifulSoup(res.text, 'html.parser')
       #     for con in soup.select('.d_post_content.j_d_post_content'):
       #         print(con.text.strip())
       #         item = NewsItem()
       #
       #         item['content']=con.text.strip()
       #         yield  item



       # soup = BeautifulSoup(response.text, 'html.parser')
       # base_url = 'https://tieba.baidu.com'

       # for link in soup.select('.threadlist_title.pull_left.j_th_tit a '):
       #     last = link['href']
       #     temp_link = base_url + last

           # res = requests.get(temp_link)
           # soup = BeautifulSoup(res.text, 'html.parser')
           # for con in soup.select('.d_post_content.j_d_post_content'):
           #     print(con.text.strip())
           #     item = NewsItem()
           #
           #     item['content']=con.text.strip()
           #     yield  item


       if self.pn<100:
           self.pn += 50

           yield scrapy.Request(self.url1 + str(self.pn), callback=self.parse)













