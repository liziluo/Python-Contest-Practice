import jieba
import wordcloud
f = open("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
t = f.read()
f.close()
Is = jieba.lcut(t)
txt = "".join(Is)
w = wordcloud.WordCloud(  font_path = "msyh.ttc",\
    width = 1000,height = 700 ,background_color="white",\
    max_words = 15)
w.generate(txt)
w.to_file("grwordcloud2.png")
