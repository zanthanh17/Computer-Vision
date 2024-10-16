import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np

my_path = 'D:/computer vision/hinhanh/1.jpg'

#doc anh
img = Image.open(my_path)
plt.imshow(img)

#ve do thi
# x = [100,100,400,400]
# y = [200,300,200,300]
# plt.imshow(img)
# plt.plot(x,y,'r*')
# plt.plot(x,y,'ks:')
# plt.show()

#ve bieu do cot Bar chart
# data = ['A','B','C','D']
# value = [15,20,40,80]
# plt.bar(data,value,color = 'g',alpha = 0.6)
# plt.show()

#ve bieu do tron Pie chart
# data = ['A','B','C','D']
# value = [15,20,40,80]
# color = ['red','blue','green','yellow']
# plt.pie(value,labels=data,colors=color,autopct= '%1.1f%%')
# plt.show()

#bieu do cloud tu van ban
# text = 'VO VAN THANH DEP TRAI QUA!!!!!!!!!!!!!!.'

# WordCloud = WordCloud(width= 800,height= 400).generate(text)

# plt.imshow(WordCloud,interpolation='bilinear')
# plt.axis('off')
# plt.show()

#bieu do histogram
# img_gray = img.convert('L')
# plt.imshow(img_gray,cmap='gray')

# img_arr = np.array(img_gray)
# print(img_arr)

# plt.figure()
# plt.hist(img_arr.flatten(),bins=128)
# plt.show()

# plt.figure()
# plt.gray()
# plt.contour(img_gray, origin = "image")
# plt.show()

points = plt.ginput(5)
print(points)

for point in points:
    x,y = point
    plt.plot(x,y,'r*')

plt.show()
    



