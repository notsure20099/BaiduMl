# -*- coding:utf-8 -*-
# 词云展示
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import jieba

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['可疑', '症状']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = jieba.cut(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		font_path="simhei.ttf",
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 数据加载
text = '今天，武汉市教育局发出《关于延迟2020年春季开学时间有关工作的通知》，延迟全市中小学、市属大中专院校2020年春季开学时间。具体开学时间将视武汉市新冠肺炎疫情发展和防控情况，请示上级同意后另行通知。2月10日前，各单位严格按照要求，做好假期各项工作。2月10日开始，各区教育局组织辖区中小学、中职学校，按照教学计划安排，开展在线课程教学（方案另发）。正式开学前，严禁市属各级各类学校组织各类线下课程教学、培训和集体活动。各区教育局要指导辖区中小学、幼儿园，合理制定学生学习计划和生活指南，指导学生安排好居家学习和生活；要关注学生心理健康，建立离校学生情况日报制度，定期向学生了解相关情况，通过电话、网络等各种方式做好学生的个性化辅导。'
## 生成词云
create_word_cloud(text)
