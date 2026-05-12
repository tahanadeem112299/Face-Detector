import cv2

model=cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
camera=cv2.VideoCapture(0)
while True:
    success, frame=camera.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=model.detectMultiScale(frame,1.1,10 )
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("face detection", frame)
    if cv2.waitKey(1)!=-1:
            break 
camera.release()
cv2.destroyAllWindows()