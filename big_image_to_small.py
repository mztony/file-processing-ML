import cv2 as cv
import numpy as np
import os
def readimage(imgpath,imgsavepath):
    for image in os.listdir(imgpath):
        cutimage(image,10,imgsavepath,imgpath)

def cutimage(imagename,size,imgsavepath,imgpath):
    img = cv.imread(imgpath + imagename)
    for i in range(size):
            for j in range(size):
                newimg = img[int(144*i):int(720+(144*(i))),int(256*j):int(1280+(256*(j)))]
                #newimg = img[int(img.shape[0]*(i/size)):int(img.shape[0]*((i+1)/size)),int(img.shape[1]*(j/size)):int(img.shape[1]*((j+1)/size))]
        
            #newimg = newimg.resize(1280,720)
            print(i,j)
            print(newimg.shape)
            #newimg = cv.resize(newimg,(1280,720))
            cv.imwrite(imgsavepath + imagename.split('.')[0] + str(i) + str(j) + '.jpg',newimg)
            #newimg.save(imgsavepath + imagename.split['.'][0] + str(i) + str(j) + '.jpg')
            #newimg.imwrite(imgsavepath + imagename.split['.'][0] + str(i) + str(j) + '.jpg')

imgpath = '/home/viewer/Downloads/model_zoo/southxj_20230618/0028/'
imgsavepath = '/home/viewer/Downloads/model_zoo/southxj_20230618/002_split/'

if __name__ == '__main__':
    readimage(imgpath,imgsavepath)
    # cutimage('000000.jpg',3,imgsavepath,imgpath)