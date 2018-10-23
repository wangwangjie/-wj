from skimage.measure import compare_ssim
#~ import skimage  as ssim
import argparse
import imutils
import cv2
from PIL import Image
import numpy as np
imageA = cv2.imread("C:/Users/Administrator/Documents/W/7-1.jpg")
imageB = cv2.imread("C:/Users/Administrator/Documents/W/7-2.jpg")


grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)

(score,diff) = compare_ssim(grayA,grayB,full = True)
diff = (diff *255).astype("uint8")
print("SSIM:{}".format(score))

thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

f=np.array([])
for c in cnts:                                                                                                                                                                                                                                        
    (x,y,w,h) = cv2.boundingRect(c)
    
    if(w*h>800):

        f=np.append(f,x)
        f=np.append(f,h)
        f=np.append(f,x)
        f=np.append(f,y)
        




u=len(f)
v=int(u/4)
h=f.reshape((v,4))

imageC=imageB.copy()


for m,n,p,q in h:    
    cv2.rectangle(imageA,(int(p),int(q)),(int(p+m),int(q+n)),(0,0,255),2)                                                                                                                                                                         
    cv2.rectangle(imageB,(int(p),int(q)),(int(p+m),int(q+n)),(0,0,255),2)
    imageB[int(q):int((q+n)),int(p):int((p+m))]=0
    
imageD=imageC-imageB


cv2.imshow("Modified",imageA)
cv2.imwrite("haha2.png",imageD)
cv2.waitKey(0)

