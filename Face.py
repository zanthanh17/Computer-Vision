import cv2
import time

def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindow()

def detect(img):
    face_cascade = cv2.CascadeClassifier('D:\computer vision\data\haarcascade_frontalface_alt.xml')

    #chuyen sang anh xam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #nhan dien
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize=(30,30))
    
    #ve hop chua khuon mat
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0),2)
        
    return img

camera = cv2.VideoCapture(0)
#tao cua so hien thi
cv2.namedWindow('video player', cv2.WINDOW_NORMAL)

intervel = 200
cnt = 0

#ghi text tren hinh anh
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255,255,255)
font_scale = 1
font_thicknes = 2

#hien thi tung khung anh
while(1):
    #thoi gian truoc khi doc
    start_time = time.time()
    #doc 1 frame
    ret, frame = camera.read()
    if not ret:
        break
    
    cnt = cnt + 1
    #luu anh xuong
    if(cnt % intervel == 0):
        cv2.imwrite(f'./hinhanh/image_{cnt}.jpg', frame)
        
    end_time = time.time()
    #tinh fps
    fps = 1/(end_time - start_time)
    
    dis = detect(frame)
    
    # ghi so luong fps
    cv2.putText(frame, f'FPS: {fps:.2f}',(10,30), font,font_scale,font_color,font_thicknes)
    
    cv2.imshow('video player', frame)
    
    if(cv2.waitKey(10) == ord('q')):
        break
#huy bo player
camera.release()
cv2.destroyAllWindows()