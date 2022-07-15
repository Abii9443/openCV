import cv2
import numpy as np
apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
apple_orange=np.hstack((apple[:, :256],orange[:,256:]))
#generate gaussian pyramid for apple

gp_apple=apple.copy()
apple_list=[gp_apple]
for i in range(6):
    gp_apple=cv2.pyrDown(gp_apple)
    apple_list.append(gp_apple)
    # cv2.imshow(str(i),apple_list[i])

#generate gaussian pyramid for orange
gp_orange=orange.copy()
orange_list=[gp_orange]
for i in range(6):
    gp_orange=cv2.pyrDown(gp_orange)
    orange_list.append(gp_orange)
    # cv2.imshow(str(i),orange_list[i])

#laplacian pyramid for apple

apple_copy=apple_list[5]
apple_lp_list=[apple_copy]
for i in range(5,0,-1):
    apple_gaussian_extended=cv2.pyrUp(apple_list[i])
    laplacian_apple=cv2.subtract(apple_list[i-1],apple_gaussian_extended)
    apple_lp_list.append(laplacian_apple)


#laplacian pyramid for orange

orange_copy=orange_list[5]
orange_lp_list=[orange_copy]
for i in range(5,0,-1):
    orange_gaussian_extended=cv2.pyrUp(orange_list[i])
    laplacian_orange=cv2.subtract(orange_list[i-1],orange_gaussian_extended)
    orange_lp_list.append(laplacian_orange)

#now add left and right halves of images in each level

apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(apple_lp_list,orange_lp_list):
    n+=1
    cols,rows,ch=apple_lap.shape
    laplacian=np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#now reconstruct

apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)
cv2.imshow('reconstruct',apple_orange_reconstruct)
# cv2.imshow('both',apple_orange)
cv2.waitKey(0)
cv2.destroyAllWindows()