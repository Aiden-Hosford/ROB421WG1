import cv2
import imutils
import math

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
  
cap = cv2.VideoCapture(10)
  
while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    if ret:
        image = imutils.resize(image, 
                               width=min(400, image.shape[1]))
  
        # Detecting all the regions 
        # in the Image that has a 
        # pedestrians inside it
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)





        # Drawing the regions in the 
        # Image
        midpoint = (0,0)
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h), 
                          (0, 0, 255), 2)
            midpoint = (math.floor(x + w/2), math.floor(y + h/2))

        # Showing the output Image
        cv2.imshow("Image", image)
        if len(regions) > 0:
            #stop robot
            print("person found, stopping")
            if midpoint[0] < 190:
                #turn left
                print("turn left")
            elif midpoint[0] > 210:
                #turn right
                print("turn right")
            else: 
                #shoot
                print("shooting")

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
 
cap.release()
cv2.destroyAllWindows()