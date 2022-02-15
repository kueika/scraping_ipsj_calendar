#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
from sql import OriginalSQLLite3

# sqlite
# database element
# date , name, submission_deadline, participation_deadline, place, update_time(取得時刻)
DB = OriginalSQLLite3(dbname="./DB/SQL.db")
DB.executeSQL(
    'CREATE TABLE IF NOT EXISTS ipsj(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, name TEXT, submission_deadline TEXT ,participation_deadline TEXT, place TEXT, update_time REAL)'
)

d_today = time.time()
url = "https://www.ipsj.or.jp/cgi-bin/ipsj_calendar.cgi"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", chrome_options=options)
driver.get(url)

html = driver.page_source.encode('utf-8')
driver.close()
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all("table")[5]
aa = table.find("tbody").find_all("tr")
data = [i.find_all("td") for i in aa]
arraydata = [[i[0].text, i[1].text, i[2].text, i[3].text, i[4].text]
             for i in data if i != []]
da = []
# date , name, submission_deadline, participation_deadline, place, update_time(取得時刻)
for i in arraydata:
    if i[2] != "" and i[3] != "":
        temp = {
            "date": i[0],
            "name": i[1],
            "submission_deadline": i[2],
            "participation_deadline": i[3],
            "place": i[4],
            "update_time": d_today
        }
        DB.executeSQL(
            'INSERT INTO ipsj(date,name,submission_deadline,participation_deadline,place,update_time) values("{0}","{1}","{2}","{3}","{4}","{5}")'.format(
                temp["date"], temp["name"], temp["submission_deadline"], temp["participation_deadline"], temp["place"], temp["update_time"]
            ))

# if __name__ == "__main__":
#     main()
