import scipy
import scipy.io
import glob
import os
import numpy as np
from scipy.io import loadmat
import cv2


ground_truths=[]
dir=os.chdir(r"C:/Users/Fatima R/Desktop/CVHW3/BSR_bsds500/BSR_bsds500/BSR/BSDS500/data/groundTruth/test")
for file in glob.glob("*.mat"):
    ground_truths.append(file)
images=[]
os.chdir(r"C:/Users/Fatima R/Desktop/CVHW3/BSR_bsds500/BSR_bsds500/BSR/BSDS500/data/images/test")
for file in glob.glob("*.jpg"):
    images.append(cv2.imread(file))
os.chdir(r"C:/Users/Fatima R/Desktop/CVHW3/BSR_bsds500/BSR_bsds500/BSR/BSDS500/data/groundTruth/test")
trues=0
falses=0
totalAvg=0
for i in range (200):


    image=images[i]
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurredImg = cv2.GaussianBlur(grayImg, (3, 3), 1)
    Canny = cv2.Canny(blurredImg, 50,200)



    temp=loadmat(ground_truths[i])
    new_list = []
    for j in range(len(temp["groundTruth"][0])):
        new_list.append(np.array(temp["groundTruth"][0][j][0][0][1]))
    size1=len(new_list[0])
    size2=len(new_list[0][0])
    emptyImg=np.zeros((size1,size2))
       
    for j in range(len(new_list)):
        emptyImg+=new_list[j]
    emptyImg=emptyImg*256//len(new_list)
    
    fileName=ground_truths[i].split("/")[-1]
    save_path = 'C:/Users/Fatima R/Desktop/CVHW3/output/'+fileName[:-4]+".png"
    cv2.imwrite(save_path,emptyImg)
    averages=[]
    for i in range(size1):
        for j in range(size2):
            if emptyImg[i][j]==Canny[i][j]:
                trues+=1
            else:
                falses+=1
    avg= trues/(trues+falses)
    averages.append(avg)
for i in range(len(averages)): 
     totalAvg+= averages[i]
     avg=totalAvg/200
print(avg)
    
# I got average precision as 0.004237387549303437