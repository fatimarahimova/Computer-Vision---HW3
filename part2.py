import numpy as np
import os
import glob


ground_truth=[]
dir=os.chdir(r"C:/Users/Fatima R/Desktop/CVHW3/output")
for file in glob.glob("*.png"):
    ground_truth.append(file)
network_output=[]
os.chdir(r"C:/Users/Fatima R/Desktop/CVHW3/CATS-master/CATS-master/output/model_cpu/test/sing_scale_test")
for file in glob.glob("*.png"):
    network_output.append(file)
trues=0
falses=0
totalAvg=0
for i in range(200):
    size1=len(ground_truth[i][0])
    size2=len(network_output[i][0][0])
    averages=[]
    for i in range(size1):
        for j in range(size2):
            if ground_truth[i][j]==network_output[i][j]:
                trues+=1
            else:
                falses+=1
    avg= trues/(trues+falses)
    averages.append(avg)
for i in range(len(averages)): 
     totalAvg+= averages[i]
     avg=totalAvg/200
print(avg)

#I found average precision as 0.005