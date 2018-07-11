import cv2 as cv
import time
from skimage.measure import compare_ssim as ssim
import numpy as np

path= "/home/ffe/Desktop/Video_Classifier/video/"

video = cv.VideoCapture(path + '0016.avi')
startTime = int(round(time.time()))

suc, img = video.read()
count = 0
count2 = 1
while suc:
    suc, img = video.read()
    if count%10 == 0:
        img_g = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_r = cv.resize(img_g, (100,100))
        cv.imwrite(path + "tmp/img%05d.jpg" % count2, img_r)
        count2 += 1
    count += 1
    
def compare(imgX, imgY):
    r = ssim(imgX, imgY)
    return r

ratio=[]

for x in range(1,count2-1):
    im = path + "tmp/img" +format(x, ">05d") + ".jpg"
    im2= path + "tmp/img"+format(x+1, ">05d")+ ".jpg"
    #print(im)
    img1 = cv.imread(im, 0)
    #print('### shape : {}'.format(img1.shape))
    img2 = cv.imread(im2, 0)
    #print('### shape : {}'.format(img2.shape))
    print(im +" --- "+ im2)
    tmp = compare(img1, img2)
    ratio.append(tmp)

rt = np.average(ratio)
print(rt)
      
endTime = int(round(time.time()))

print ("Time: ", (endTime-startTime))

print(count2)
if (rt > 0.8):
    print("Security cam")
else:
    print("Normal cam")