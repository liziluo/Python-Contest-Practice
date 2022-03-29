import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
Is = jieba.lcut(t)
txt = "".join(Is)
w = wordcloud.WordCloud(  font_path = "msyh.ttc",\
    width = 1000,height = 700 ,background_color="white")
w.generate(txt)
w.to_file("grwordcloud3.png")
