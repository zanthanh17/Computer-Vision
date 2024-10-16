import os
from PIL import Image

def imag_tool(image_path):

    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print('duong dan bi loi', image_path,' ', e)
        return None
    
def is_image_file(file_path):
    """
    return True Neu la file anh
           False Neu ko la file anh
    """

    extension = ('.jpg','.jpeg','.png','.gif')
    return file_path.lower().endswith(extension)

def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):  #kiem tra folder co ton tai hay khong
        filenames = os.listdir(folder_path)  #them ten file trong folder
        for filename in filenames:  #kiem tra tung ten file 
            file_path = os.path.join(folder_path,filename)   
            if os.path.isfile(file_path) and is_image_file(file_path): #kiem tra co phai la file khong
                img = imag_tool(file_path)
                image_list.append(img)   #them nhieu anh vao list
    return image_list
