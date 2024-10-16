from PIL import Image
from imgtool import *

dir = 'D:/computer vision/hinhanh/1.jpg'

img1 = imag_tool(dir)

print(img1.size)
# img1.show()

# #thay doi kich thuoc anh
# new_size = (100,100)
# #tao anh moi
# new_resize = img1.resize(new_size)
# #task: luu anh
# new_resize.show()

# img1.thumbnail(50,50)
# img1.show()

##sao chep va dan ca vung` anh
 #dinh vi khu vuc cat -> crop
# region = (100,100,250,250)
# cropped_img = img1.crop(region)
# display(cropped_img)
#  #dinh vi khu vuc dan anh -> paste
# img1.paste(cropped_img,250,250)
# display(img1)

##XOAY ANH 
# rotate_img = img1.rotate(90) #xoay nhung bi mat 1 phan anh
# rotate_img.show()
# transpose_img = img1.transpose(Image.Transpose.ROTATE_90) #transpose xoay nhung k bi mat anh
# transpose_img.show()
# transpose_img = transpose_img.transpose(Image.Transpose.ROTATE_90) #transpose xoay nhung k bi mat anh
# transpose_img.show()

##BIEN DOI MAU ANH
 #chuyen anh mau sang anh xam
grey_img = img1.convert("L")
grey_img.show()
 #tach thanh 3 day mau R,G,B
red,green,blu = img1.split()
red.show()
green.show()
blu.show()
 #tron 3 day mau do lai
merged_img = Image.merge("RGB", (red,green,blu))
merged_img.show()





    


