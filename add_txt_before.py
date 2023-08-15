import os,sys                       
def add_prefix_files(mark):             
    old_names = os.listdir( path )  #获得文件夹中的文件名，生成list
    for old_name in old_names:      
            if  old_name!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
               if old_name.endswith('.jpg'):   #找到以.jpg 为后缀的文件,可改
                    os.rename(os.path.join(path,old_name),os.path.join(path,mark+old_name))  #rename
                    print (old_name,"has been renamed successfully! New name is: ",mark+old_name)  #rename success
if __name__ == '__main__': 
        path = r'/home/mozhe/test/fire_hydrant/JPEGImages/'   #主文件夹路径
        add_prefix_files('2007_')
        
