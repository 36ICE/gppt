import requests
from bs4 import BeautifulSoup

# # 要爬取的页面 URL
# url = "http://guba.eastmoney.com/list,BK1046.html"
#
# # 定义请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
# }
#
# # 发送 GET 请求并获取响应内容
# response = requests.get(url, headers=headers)
#
# # 解析 HTML 页面
# soup = BeautifulSoup(response.text, "html.parser")
#
# # 找到评论区域（class="articleh"）
# comments = soup.find_all(class_="articleh")
#
# # 遍历评论区域，提取评论内容和发表时间
# for comment in comments:
#     content = comment.find(class_="l3 a3").text.strip()  # 评论内容
#     time = comment.find(class_="l5 a5").text.strip()    # 发表时间
#     print(content, time)


import requests
from bs4 import BeautifulSoup
import time

# 设置请求间隔时间
interval = 5

# 创建session对象
session = requests.Session()

# 发送第一页请求并获取响应
url = "http://guba.eastmoney.com/list,BK1046.html"
response = session.get(url)

# 解析HTML文档
soup = BeautifulSoup(response.text, "html.parser")

# 获取当前页面的评论数据
comments = soup.find_all("div", class_="articleh")
for comment in comments:
    content = comment.find(class_="l3 a3").text.strip()  # 评论内容
    date = comment.find(class_="l5 a5").text.strip()  # 发表时间
    print(content, date)

# 等待一段时间后再发送下一页请求
time.sleep(interval)

# 获取下一页URL并发送请求
next_page_link = soup.find("a", text="下一页")
while next_page_link:
    next_page_url = "http://guba.eastmoney.com" + next_page_link["href"]
    response = session.get(next_page_url)

    # 解析HTML文档
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取下一页的评论数据
    comments = soup.find_all("div", class_="articleh")
    for comment in comments:
        content = comment.find(class_="l3 a3").text.strip()  # 评论内容
        time = comment.find(class_="l5 a5").text.strip()  # 发表时间
        print(content, time)

        # 等待一段时间后再发送下一页请求
        time.sleep(interval)
    next_page_link = soup.find("a", text="下一页")
