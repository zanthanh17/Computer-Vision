import cv2
import time

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
    
    # ghi so luong fps
    cv2.putText(frame, f'FPS: {fps:.2f}',(10,30), font,font_scale,font_color,font_thicknes)
    
    cv2.imshow('video player', frame)
    
    if(cv2.waitKey(10) == ord('q')):
        break
#huy bo player
camera.release()
cv2.destroyAllWindows()