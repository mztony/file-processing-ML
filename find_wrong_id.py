import os

path = "/home/viewer/Downloads/model_zoo/all/txts/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
for file in files: #遍历文件夹
    position = path + file #构造绝对路径，"\\"，其中一个'\'为转义符
    #print (position)           
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        data = f.readlines()   #读取文件
        for line in data:
            if line[0] != '0':
                print(file)

