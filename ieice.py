#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import sqlite3

from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.ieice.org/event/allevents.php"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", chrome_options=options)

# ページにアクセス

driver.get(url)

# 検索ボックスを見つけてキーワードを検索
text = "a\u3000 b\t\nc\r\n"
table = str.maketrans({
    '\u3000': '',
    ' ': '',
    '\t': ''
})

# search = driver.find_element_by_class_name("st-Header_searchInput")

# 検索先のページのHTMLを取得

html = driver.page_source.encode('utf-8')
driver.close()
soup = BeautifulSoup(html, 'lxml')

li = soup.find("ol")

li_a = li.find_all("li")
# text = text.translate(table)
data = [i.text.split("\n") for i in li_a]
print([i[0].split(",")+(i[1].split("テーマ：")) for i in data])
# for i in li_a:
#     print("----")
#     # print(i.text)
#     aaa = i.text.split("\n")
#     print(aaa)
# print(li_a)
