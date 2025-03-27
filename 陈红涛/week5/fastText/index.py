import fasttext #model 就是一个神经网络模型
import jieba

#提取以空格隔开的文本中的词 
# model = fasttext.train_unsupervised("XYJ1.txt",model='skipgram',dim=10,epoch=50,lr=0.1,wordNgrams=2)
# a = model.get_nearest_neighbors('弼马温',k=2)
# # b = model.get_analogies('弼马温','张无忌','张三丰')

# print(b)
# print(a)

#分类模型

model = fasttext.train_supervised("cooking.stackexchange.txt")
print(model.predict("Which baking dish is best to bake a banana bread ?"))
# model.save_model("model_cooking.bin") 保存模型
# model.load_model("model_cooking.bin") 加载模型


# print(model.words)
# print(model.labels)