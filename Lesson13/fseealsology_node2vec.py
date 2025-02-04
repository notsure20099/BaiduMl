# 使用Node2Vec对space_data进行压缩
import networkx as nx
import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from sklearn.decomposition import PCA
from node2vec import Node2Vec
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 数据加载，构造图
data=pd.read_csv('seealsology-data.tsv', sep='\t')
G = nx.from_pandas_edgelist(data, "source", "target", edge_attr=True, create_using=nx.Graph())
print(type(G))
#G = nx.read_gml('football.gml', relabel=True)
print(len(G))

# 初始化Node2Vec模型
#model = DeepWalk(G, walk_length=10, num_walks=5, workers=1)
model = Node2Vec(G, walk_length = 10, num_walks = 5, p = 0.25, q = 4, workers = 1)
# 模型训练
result = model.fit(window=4, iter=20)
# 得到节点的embedding
print(result.wv.most_similar('critical illness insurance'))
embeddings = result.wv
print(embeddings)

# 在二维空间中绘制所选节点的向量
def plot_nodes(word_list):
    # 每个节点的embedding为100维
    X = []
    for item in word_list:
        X.append(embeddings[item])
    #print(X.shape)
    # 将100维向量减少到2维
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    #print(result)
    # 绘制节点向量
    plt.figure(figsize=(12,9))
    # 创建一个散点图的投影
    plt.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(list(word_list)):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.show()

plot_nodes(result.wv.vocab)
