import cv2 as cv
import numpy as np

img = cv.imread('coc_image.png',cv.IMREAD_UNCHANGED)
img2 = cv.imread('coc_army.png',cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(img,img2,cv.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
print('match top left :%s'%str(max_loc))
print('confidence :%s'%str(max_val))
threshold = 0.8
img_w = img2.shape[1]
img_h = img2.shape[0]
top_left = max_loc
bottom_right = (top_left[0] + img_w,top_left[1] + img_h)
if max_val >= threshold:
    cv.rectangle(img,top_left,bottom_right,color=(2,255,10),thickness = 4,lineType = cv.LINE_4)
    cv.imshow('RESULT',img)
    cv.waitKey()
else:
    print('not found')


