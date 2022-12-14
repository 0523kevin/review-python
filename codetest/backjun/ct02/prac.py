# dict(k:v for k,v in sorted(x.items, key = lambda item:item[1]))


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = sin(x)
y2 = cos(x)

plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()


from matplotlib.image import imread

img = imread('len.png')
plt.imshow(img)
plt.show()
