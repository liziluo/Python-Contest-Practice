import jieba
import wordcloud
from scipy.misc import imread
mask = imread("fivestart.png")
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
Is = jieba.lcut(t)
txt = "".join(Is)
w = wordcloud.WordCloud(  font_path = "msyh.ttc",\
    width = 1000,height = 700 ,background_color="white",\
    max_words = 15)
w.generate(txt)
w.to_file("grwordcloud.png")
