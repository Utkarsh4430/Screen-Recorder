import numpy as np
import cv2
import pyscreenshot as pys
import sys
filename = '/recording.mp4'
try:
	path = sys.argv[1]
except:
	path = '.'
if(path[-1]=='/'):
	filename = 'recording.mp4'
test= np.array(pys.grab())
print(test.shape)
# print(type(test.shape))
VW = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path + filename, VW, 4, (test.shape[1],test.shape[0]),True)
k=0
while True:
	img= np.array(pys.grab())
    # img = cv2.resize(img,(800,600))
	cv2.imshow('Screen', img)
	out.write(img)
	key = cv2.waitKey(1) & 0xFF #waitkey returns 32 bit integer when a key is struck and -1 otherwise
								#we need first 8 bits of the the output of waitkey so we take & with 0xFF (hexadecimal for 11111111)
	if key==ord(' '):
		break
	elif key==ord('p'):
		while True:
			key2 = cv2.waitKey(1) & 0xFF
			if key2==ord(' '):
				k=1
				break
			if key2==ord('p'):
				break
	if(k==1):
		break
out.release()
cv2.destroyAllWindows()