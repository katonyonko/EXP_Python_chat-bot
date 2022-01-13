import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

 # 1. Get a html.
with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
titles = soup.select(".entrylist-contents-title a")
titles =[[t["title"], t["href"]] for t in titles]
shuffle(titles)
print(titles[0][0],titles[0][1])