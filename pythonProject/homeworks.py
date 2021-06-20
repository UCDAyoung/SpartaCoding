import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from openpyxl import Workbook

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = "https://search.naver.com/search.naver?&where=news&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

cases = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul> li')

for case in cases:
    article = case.select_one('li > dl > dt > a').text
    link = case.select_one('li > dl > dt > a')['href']
    news = case.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
    thumbnail = case.select_one('div > a > img')['src']



    print(article, link , news, thumbnail)
    ws1.append([article, link , news, thumbnail])

wb.save(filename='articles.xlsx')
driver.quit()

# 보내는 사람 정보
me = "qkr93643857@gmail.com"
my_password = "qkrwnsdud134"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)
# 받는 사람 정보
emails = ['wnsdudcksgh@naver.com','gyeh159@naver.com']

for you in emails:

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[공유] 추석기사"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "추석 기사"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())
s.quit()