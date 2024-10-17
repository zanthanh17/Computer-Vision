import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np

my_path = 'D:/computer vision/hinhanh/1.jpg'

#doc anh
img = Image.open(my_path)


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

# points = plt.ginput(5)
# print(points)

# for point in points:
#     x,y = point
#     plt.plot(x,y,'r*')

# plt.show()

#ham can bang do sang cua hinh anh
def histogram_equalization(img, nbr_bins=256):
    # dam bao hinh anh dau vao la anh xam
    if img.mode != 'L':
        img = img.convert('L')
        
    # chuyen hinh anh thanh mang Numpy
    img_arr = np.array(img)
    
    # tinh toan histogram cua anh
    histogram, bins = np.histogram(img_arr, bins=nbr_bins, range=(0, 256), density = True)
    
    # tinh toan ham phan phoi tich luy (CDF)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]
    
    # lay gia tri moi cho tuong pixel duaj tren CDF
    img_equalized = np.interp(img_arr, bins[:-1], cdf)
    
    equalized_img = Image.fromarray(img_equalized.astype('uint8'))
    
    return equalized_img
    
# HAM TAO ANH BANG CACH TRUNG BINH CAC ANH
def avr_img(img_list):
    total_arr = np.array(Image.open(img_list[0]), 'f')
    cnt = 1
    
    for img_path in img_list[1:]:
        try:
            img_arr = np.array(Image.open(img_path), 'f')
            total_arr += img_arr
            cnt = cnt + 1
        except:
            print('Skip ', img_path)
    avr_arr = total_arr / cnt
    avr_img = Image.fromarray(avr_arr.astype('uint8'))
    
    return avr_img

    
    



