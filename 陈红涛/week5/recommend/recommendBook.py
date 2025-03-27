import csv
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_data(fileName):
    book_comments = {}
    with open(fileName,"r") as f:
        reader = csv.DictReader(f,delimiter='\t')

        for (index,item) in enumerate(reader):
            if index == 0: continue
            book = item["book"]
            comment = item["body"]
            conment_words = jieba.lcut(comment,cut_all=False)
            if book == "" : continue
            book_comments[book] = book_comments.get(book,[])
            book_comments[book].extend(conment_words)
    return book_comments

# a = load_data("./top250Book_comments.txt")

# print(a)

if __name__ == '__main__':

    stop_words = [line.strip() for line in open("./stopwords.txt", 'r', encoding='utf-8')]
    book_comments = load_data("./top250Book_comments.txt")
    # print(book_comments)
    print(len(book_comments))

    #提取书名和评论文本
    names = []
    comments = []
    for (name,comment) in book_comments.items():

        names.append(name)
        comments.append(" ".join(comment))
    #构建TF-IDF矩阵
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf = vectorizer.fit_transform(comments)
    
    #计算余弦相似度 把每一句评论 中的词 组成一个向量 然后 与 别的词进行对比
    similarity = cosine_similarity(tfidf) 
    #找到最相似的书
    book_list = names ;#  book_list1 = list(book_comments.keys())
    # print(book_list) 
    book_name = input("请输入书名：")
    book_index = book_list.index(book_name)
    # 排列出 加-号代表从高到低排列 imilarity[book_index] 这本书与其他所有书的相似度 然后取前9本
    sBook = np.argsort(-similarity[book_index])[1:10]

    for bookR in sBook:
        print(f"{book_list[bookR]} \t 相似度：{(similarity[book_index][bookR])*100:.4f}%" )
 