import cv2
import numpy as np

def verify_signature(path1, path2):
    img1 = cv2.imread(path1,0)
    img2 = cv2.imread(path2,0)

    img1 = cv2.resize(img1,(300,150))
    img2 = cv2.resize(img2,(300,150))

    diff = cv2.absdiff(img1,img2)
    score = np.sum(diff)/100000

    return float(score)