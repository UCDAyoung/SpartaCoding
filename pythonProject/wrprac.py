from wordcloud import WordCloud
from PIL import Image
import numpy as np


text =''
with open("kakaoTalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        text += line.replace(' ','-').replace(',','-').replace('박준영','').replace('대건ㅇ','').replace('시바','').replace('ㅋ','').replace('ㅅㅂ','')


mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/Library/Fonts/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")