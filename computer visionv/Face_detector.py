import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


my_webcam = cv2.VideoCapture(0)

key = cv2.waitKey(1)

while True:
    ret, frame = my_webcam.read()

    #converting the webcam to grey scale
    grey_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # parsing the greyscale video into the the haarcascade
    face_detect = trained_face_data.detectMultiScale(grey_video)

    #print(face_detect)
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+w), (randrange(200),randrange(256),10), 3)

    #display webcam
    cv2.imshow('face_detection', frame)
    cv2.waitKey(1)


    # using a key to quit
    if cv2.waitKey(1) == ord('q'):
        break

my_webcam.release()
cv2.destroyAllWindows()



"""""

# using an image
#img = cv2.imread('Four_faces.jpeg')

#usng a webecame to capture video

#converting the image to grey scale
grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#parsing the greyscale image into the the haarcascade
face_detect = trained_face_data.detectMultiScale(grey_image)

#print(face_detect)
for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x+w, y+w), (randrange(200),randrange(256),10), 3)

#display image
cv2.imshow('face_detection', img)
cv2.waitKey()


print('code completed')
"""