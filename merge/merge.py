from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2
import requests
import time
import argparse
import time
import base64
from tkinter import *
from random import randint

#INTERFACE

#We want to open the intarface 
root = Tk()
width_x=1024
width_y=768 
root.geometry(str(width_x)+"x"+str(width_y))
root.configure(bg='white')
root.title("OBO")

#Dimension information boxes
marg = 24
w_box = 150
bus_x =[-(2*w_box+marg*3/2)+width_x/2,-(w_box+marg/2)+width_x/2,marg/2+width_x/2,marg*3/2+w_box+width_x/2]

#Define coordinates 
coor_b1 = width_y*9/20 + 70
coor_b2 = width_y*15/20 + 70

#CANVAS, before text
#Define interface margins
canvas = Canvas(root)
canvas.configure(bg='white')
canvas.create_line(0,width_y/5,width_x,width_y/5)
canvas.create_line(0,width_y*3/10,width_x,width_y*3/10)
canvas.create_line(0,width_y*3/5,width_x,width_y*3/5,fill="gray")
canvas.create_line(0,width_y*9/10,width_x,width_y*9/10)
canvas.pack(fill=BOTH, expand=1)


def draw(bus_full1):
    canvas.delete('all')
    #Define interface margins
    canvas.create_line(0,width_y/5,width_x,width_y/5)
    canvas.create_line(0,width_y*3/10,width_x,width_y*3/10)
    canvas.create_line(0,width_y*3/5,width_x,width_y*3/5,fill="gray")
    canvas.create_line(0,width_y*9/10,width_x,width_y*9/10)
    canvas.create_text(width_x/2,width_y/20, text="NOM D'ÂRRET", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(width_x/2,width_y/6, text="NOM DU SERVICE", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(width_x/6, width_y*37/40, text="Derriere", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(width_x*5/6, width_y*37/40, text="Avant", fill="black", font=('Helvetica 15 bold'))

    for i in range(4):
        canvas.create_text(bus_x[i]+w_box/2,coor_b1+20,text= bus1_t[i],fill='black',font=('Helvetica 15 bold'))

    #Define wagon boxes
    for dep in bus_x:
        canvas.create_rectangle(dep, coor_b1-bus_full1*1.4,dep+w_box, coor_b1, outline="blue", fill="#fb0") ##Bus1
    canvas.create_rectangle(width_x/2-w_box, coor_b2-100, width_x/2, coor_b2, outline="blue", fill="#fb0") ##Bus2
    canvas.pack(fill=BOTH, expand=1)

bus1_t=[None,None,None,None]
def update(bus_full1):
    #bus_full1 = randint(0,100)
    for i in range(4):
        bus1_t[i]= str(bus_full1) + " %"
    #bus2['text'] = str(randint(0,100)) + " %"
    draw(bus_full1)
    root.after(1000, update) # run itself again after 1000 ms

# run first time
update(bus_full1)

root.mainloop()














#CAMERA RECOGNITION
'''
Usage:

python peopleCounter.py -i PATH_TO_IMAGE  # Reads and detect people in a single local stored image
python peopleCounter.py -c  # Attempts to detect people using webcam

'''

# Opencv pre-trained SVM with HOG people features 
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detector(image):
    '''
    @image is a numpy array
    '''

    clone = image.copy()

    (rects, weights) = HOGCV.detectMultiScale(image, winStride=(4, 4),
                                              padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Applies non-max supression from imutils package to kick-off overlapped
    # boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    return result

# Defining the parameters that I will recieve from the command prompt
def argsParser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default=None,
                    help="path to image test file directory")
    ap.add_argument("-c", "--camera", default=False,
                    help="Set as true if you wish to use the camera")
    args = vars(ap.parse_args())

    return args


def localDetect(image_path):
    result = []
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    clone = image.copy()
    #iterator to count boxes
    i=0
    if len(image) <= 0:
        print("[ERROR] could not read your local image")
        return result
    print("[INFO] Detecting people")
    result = detector(image)

    # shows the result
    for (xA, yA, xB, yB) in result:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        i=i+1
        bus_full1=i
    print("[INFO] The search for people was successful. I was able to find", i , "people") 
    print("[INFO] Press Q to exit") 

    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #This will save the result in an image file that will have the before and after of the picture
    #cv2.imwrite("result.png", np.hstack((clone, image)))
    #return (result, image)


def cameraDetect():

    cap = cv2.VideoCapture(0)
    init = time.time()

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        result = detector(frame.copy())
        j=0
        # shows the result
        for (xA, yA, xB, yB) in result:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
            j=j+1
            bus_full1 = j
            #timer just in case we dont want the live data but rather a periodic check
            #time.sleep(1)
            print("[INFO] The search for people was successful. I was able to find", j , "people")
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def convert_to_base64(image):
    image = imutils.resize(image, width=400)
    img_str = cv2.imencode('.png', image)[1].tostring()
    b64 = base64.b64encode(img_str)

    return b64.decode('utf-8')


def detectPeople(args): 
    image_path = args["image"]
    camera = True if str(args["camera"]) == 'true' else False

    # Routine to read local image
    if image_path != None and not camera:
        print("[INFO] Image path provided, attempting to read image")
        (result, image) = localDetect(image_path)
        # Converts the image to base 64 and adds it to the context
        b64 = convert_to_base64(image)
        context = {"image": b64}

    # Routine to read images from webcam
    if camera:
        print("[INFO] reading camera images")
        cameraDetect()
        print("[INFO] Press Q to exit")


def main():
    args = argsParser()
    detectPeople(args)


if __name__ == '__main__':
    main()