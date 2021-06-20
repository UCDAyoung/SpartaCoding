import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('/chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B5%9C%ED%9A%A8%EC%A0%95") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')


images=soup.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img')

i=1
for image in images:
    src = image['src']
    dload.save(src,f'imgs_homework/최효정{i}.jpg')
    i+=1

driver.quit() # 끝나면 닫아주기

#####################밑에는 연습######################3
