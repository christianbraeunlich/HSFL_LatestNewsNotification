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
            for news in response.css(".Card--orange.Media"):
                title = news.css("span::text").extract_first() 
                date = news.css("span.Card-meta span::text").extract_first()
                preview = news.css("a.Card-link::text").extract_first()
                image = response.css("div.Card--orange.Media img::attr(src)").extract_first()
                imageURL = response.urljoin(image)
                item['title'] = title
                item['date'] = date
                item['preview'] = preview
                item['image'] = imageURL
                timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                db.cursor.execute('INSERT or IGNORE INTO latestNews(title, date, preview, image, timestamp) VALUES(?, ?, ?, ?, ?)', (item['title'], item['date'], item['preview'][8:], item['image'], timestamp,) )
                newsID = db.query('SELECT id FROM latestNews WHERE title LIKE ?', ([item['title']] ))
                save_path = 'images/'
                newsID = str(newsID.pop())[1:-2]
                completeName = os.path.join(save_path, "news_" + newsID + ".jpg")  
                urllib.request.urlretrieve(imageURL, completeName)

        next_page_url = response.css("li.page__item > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

### Save new Grades into Database-Table
class HSFL_LatestGradesNotification(CrawlSpider):
    name = 'hsfl_latestgradesnotify'
    allowed_domains = ['hs-flensburg.de']
    start_urls = ['https://hs-flensburg.de/hochschule/pruefungsmanagement/notenaushaenge']

    def parse(self, response):
        href = response.xpath('/html/body/div/div/main/div[4]/div/div/div/ul/li/a/@href').extract()
        study_courses = response.xpath('/html/body/div/div/main/div[4]/div/div/div/ul/li/a/text()').extract()
        links = [[href[i], study_courses[i]] for i in range(len(study_courses))]
        print('######')
        print('######')
        print('######')
        print(":::::LINKS:::::")
        print(links)
        for i in range(len(links)):
            base_url = 'https://hs-flensburg.de/hochschule/pruefungsmanagement/notenaushaenge'
            item = HSFL_LNN_Item()
            item['study_course'] = links[i][1]
            study_course_id = links[i][0].rsplit('/', 1)
            item['study_course_id'] = study_course_id[1]

            print("# Study_Course   : " + item['study_course'])
            print("# Study_Course_Id: " + item['study_course_id']) 
            final_url = urljoin(base_url, links[i][0])
            print("# Final URL: " + final_url)
            print()
            request = scrapy.Request(final_url, callback=self.parse_exam_data, dont_filter=True)
            request.meta['item'] = item
            yield request
        
    def parse_exam_data(self, response):
        item = response.meta['item']
        print(":::::parse_exam_data:::::")
        for row in response.xpath('/html/body/div/div/main/div[4]/article/div/div[2]/ul'):
            with SQLiteConnection('hsfl_lnn.db') as db:
                for grade in response.css("li"):
                    if grade.css('a[href$=".pdf"]::attr(href)').extract_first() != None:
                        item['course'] = grade.css('a[href$=".pdf"]::attr(href)').extract_first()
                        print('# EXAM_PDF: ' + item['course'])
                        print()
                        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                        db.cursor.execute('INSERT or IGNORE INTO latestGrades(courseid, course, study_course, study_course_id, file, timestamp) VALUES(?, ?, ?, ?, ?, ?)', (item['course'][58:64], item['course'][65:-4], item['study_course'], item['study_course_id'], item['course'][:8] + urllib.parse.quote(item['course'][8:]), timestamp,) )
            yield item