import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("RecVid.mkv",fourcc, 20.0, (640,480))  

while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('Frame',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()