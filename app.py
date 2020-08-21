from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import tensorflow as tf
import cv2
import time
classes=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

MODEL=tf.keras.models.load_model("Model.h5")
# print(MODEL.summary())
s=time.time()
def load_image(filename):
    img=cv2.imread(filename,0)
    img=cv2.bitwise_not(img)
    img=cv2.resize(img,(28,28))
    data = np.asarray(img)
    return data/255.0

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)


data = [load_image(filename)]
data=np.array(data)
data = np.array(data).reshape(-1,28,28,1)



j=MODEL.predict([data])
print(j)
i=np.argmax(j)

print('\n')
print(i)
print('class:{0}'.format(classes[i]))
l=time.time()
print(f'{1000/(l-s)}FPS')
while True:
    img=cv2.imread(filename,0)
    img=cv2.bitwise_not(img)
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


