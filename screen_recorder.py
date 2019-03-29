import numpy as np
import cv2
import pyscreenshot as pys
import sys
try:
	path = sys.argv[1]
except:
	path = '.'

test= np.array(pys.grab())
print(test.shape)
# print(type(test.shape))
VW = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path + '/recording.mp4', VW, 8, (test.shape[1],test.shape[0]),True)

while True:
    img= np.array(pys.grab())
    # img = cv2.resize(img,(800,600))
    cv2.imshow('Screen', img)
    # print(img.shape)
    out.write(img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

out.release()
cv2.destroyAllWindows()