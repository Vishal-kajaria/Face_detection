import cv2

file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
capturing=cv2.VideoCapture(0)

while True:
    rec,image=capturing.read()
    color=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    scale=file.detectMultiScale(color,1.3,6)

    for (x1,y1,w1,h1) in scale:
        cv2.rectangle(image,(x1,y1), (x1+w1 , y1+h1) , (0,255,0) , 2)

    cv2.imshow('img',image)

    wait_key=cv2.waitKey(10) & 0xff

    if wait_key==10:
        break

capturing.release()
cv2.destroyAllWindows()
 