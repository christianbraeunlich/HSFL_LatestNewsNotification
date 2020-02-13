#!usr/bin/env python3

import time, datetime
import urllib.request
import os.path
import sqlite3
import sys
import array
import os
import glob
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from HSFL_LNN.items import HSFL_LNN_Item
from HSFL_LNN.SQLiteConnection import SQLiteConnection
from scrapy import Spider, Request
from urllib.parse import urljoin

#''''' News Spider '''''#
class HSFL_LatestNewsNotification(CrawlSpider):
    name = "hsfl_latestnewsnotify"
    allowed_domains = ["hs-flensburg.de"]
    start_urls = [
        'https://hs-flensburg.de/hochschule/aktuelles/'
    ]

    def parse(self, response):
        item = HSFL_LNN_Item() 
        with SQLiteConnection('hsfl_lnn.db') as db:
            for news in response.css("div.Card"):
                title = news.css("span::text").extract_first() 
                date = news.css("span.Card-meta span::text").extract_first()
                preview = news.css("a.Card-link::text").extract_first()
                image = news.css("img::attr(src)").extract_first()
                imageURL = response.urljoin(image)
                item['title'] = title
                item['date'] = date
                item['preview'] = preview
                item['image'] = imageURL
                timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                db.cursor.execute('INSERT or IGNORE INTO latestNews(title, date, preview, image, timestamp) VALUES(?, ?, ?, ?, ?)', (item['title'], item['date'], item['preview'][8:], item['image'], timestamp) )
                newsID = db.query('SELECT id FROM latestNews WHERE title LIKE ?', ([item['title']] ))
