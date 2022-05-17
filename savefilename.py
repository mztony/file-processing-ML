import os
def dirList(pathlist):
    for i in range(0, len(pathlist)):
        paths = os.path.join(path, pathlist[i])
    if os.path.isdir(paths):
        saveList(os.listdir(paths))
def saveList(pathlist):
    for filename in pathlist:
        with open("filename.txt", "a") as f:
            f.write(filename.split(".")[0] + "\n")#删掉后缀
    print('Success!')

if __name__ == '__main__': 
        path = r'C:/Users/lenovo/Desktop/灭火器数据集/Annotations/'   #路径
        pathlist = os.listdir(path)  #所有文件名    
        dirList(pathlist)
        saveList(pathlist)