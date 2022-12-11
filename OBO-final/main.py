from tkinter import *
from random import randint
from time import sleep
import peopleCounter

window = Tk()
window.geometry('905x640')
window.title('OBO - Interface')
window['bg'] = '#b3ccc6' ##B8C6C2
window.resizable(height=False, width=False)

"""
CREATION OF THE FOUR FRAMES
"""
#Creation of the Head_Frame
headFrame = Frame(window, bg="red", width="902", height="30")

herderLabel = Label(headFrame, text="LIBERTE PLACE", fg="black", bg="#b3ccc6", font=("Verdana", 20, "bold"))
herderLabel.pack()
headFrame.pack()

#Creation of the Top_Left_Frame
topLeftFrame = Frame(window, bg='#CCDDD9', width="300", height="300")
topLeftFrame.place(x="0", y="35")

#Creation of the Top_Right_Frame
topRightFrame = Frame(window, bg='#CCDDD9', width="600", height="300")
topRightFrame.place(x="303", y="35")

#Creation of the Bottom_Left_Frame
bottomLeftFrame = Frame(window, bg='#CCDDD9', width="300", height="300")
bottomLeftFrame.place(x="0", y="340")

#Creation of the Bottom_Right_Frame
bottomRightFrame = Frame(window, bg='#CCDDD9', width="600", height="300")
bottomRightFrame.place(x="303", y="340")


WIDTH = 280
HEIGHT = 40
STOPS_02 = ["PORTE DE PLOUZANE", "RECOUVRANCE", "KENNEDY GARE", "LIBERTE PLACE"]
STOPS_08 = ["PORTZIC", "PRAT LEDAN", "RAMPES", "KENNEDY GARE"]
MIN_02 = ["05", "03", "01", "00"]
MIN_08 = ["09", "07", "05", "04"]
CUR_STOP_INDEX = 0
CUR_MIN_INDEX = 0
CURRENT_STOP = "RECOUVRANCE"
W_RECOMMENDED = "W2"
BUS_SHAPE_W = 580
BUS_SHAPE_H = 200
WAGON_W = 125
WAGON_H = 190

SATURATION_RED = "#D2837E"
SATURATION_GREEN = "#76D4B8"
SATURATION_ORANGE = "#F3A761"

#W1_COLOR = SATURATION_GREEN
#W2_COLOR = SATURATION_GREEN
#W3_COLOR = SATURATION_RED
#W4_COLOR = SATURATION_RED

MAX = -13
MIN = -150
#W1_A_Y = MAX
#W2_A_Y = MAX
#W3_A_Y = MAX
#W4_A_Y = MAX


"""
TOP_LEFT_FRAME COMPONENTS
"""
def setInformations():
    curMins = arrivalMinute()
    curStops = currentStop()

    busInfoCanvas = Canvas(topLeftFrame, width=WIDTH, height=HEIGHT, bg="#CCDDD9")

    diam = HEIGHT
    A = (a,b) = (0, 0)
    B = (diam+a, diam+b)
    busInfoCanvas.create_oval(A, B, fill="orange")

    busInfoCanvas.create_text(HEIGHT/2, HEIGHT/2, text="02", fill="white", font=("Times", 16, "bold"))
    busInfoCanvas.create_rectangle(HEIGHT, 0, WIDTH, HEIGHT, fill="#111C7E")
    busInfoCanvas.create_text(((WIDTH-HEIGHT)/2)+HEIGHT, HEIGHT/2, text="ARRIVEE : %s min" %curMins[0], fill="white", font=("Times", 14, "bold"))
    busInfoCanvas.place(x="10", y="10")


    busPositonCanvas = Canvas(topLeftFrame, width=WIDTH, height=HEIGHT, bg="#CCDDD9")
    busPositonCanvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#AAC5CB")
    busPositonCanvas.create_text(WIDTH/2, HEIGHT/2, text="BUS à : %s" %curStops[0], fill="white", font=("Times", 14, "bold"))
    busPositonCanvas.place(x="10", y="130")



    recommendationCanvas = Canvas(topLeftFrame, width=WIDTH, height=HEIGHT, bg="#CCDDD9")
    recommendationCanvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#AAC5CB")
    recommendationCanvas.create_text(WIDTH/2, HEIGHT/2, text="Recommandation : %s" %W_RECOMMENDED, fill="white", font=("Times", 14, "bold"))
    recommendationCanvas.place(x="10", y="250")


#-------------------------------------------------------------------------------------------------

"""
TOP_RIGHT_FRAME COMPONENTS
"""
def draw_bus(W1_A_Y, W2_A_Y, W3_A_Y, W4_A_Y, W1_COLOR, W2_COLOR, W3_COLOR, W4_COLOR):
    busShape = Canvas(topRightFrame, width=BUS_SHAPE_W, height=BUS_SHAPE_H, bg="#AAC5CB")
    busShape.place(x="10", y="10")

    # Bus bottom shape
    A1 = (10, 50)
    B1 = (10, 150)
    C1 = (60, 150)
    D1 = (60, 10)
    E1 = (30, 10)
    busShape.create_polygon(A1, B1, C1, D1, E1)

    # Bus middle shape
    A2 = (65, 10)
    B2 = (465, 150)
    busShape.create_rectangle(A2, B2)

    # WAGON 1
    A_w1_bg = (67, 13)
    B_w1_bg = (162, 148)
    busShape.create_rectangle(A_w1_bg, B_w1_bg, fill="#BFDFE7", outline="#BFDFE7")

    A_w1_fg = (67, W1_A_Y)
    B_w1_fg = (162, 148)
    busShape.create_rectangle(A_w1_fg, B_w1_fg, fill=W1_COLOR, outline=W1_COLOR)

    # WAGON 2
    A_w2_bg = (167, 13)
    B_w2_bg = (262, 148)
    busShape.create_rectangle(A_w2_bg, B_w2_bg, fill="#BFDFE7", outline="#BFDFE7")

    A_w2_fg = (167, W2_A_Y)
    B_w2_fg = (262, 148)
    busShape.create_rectangle(A_w2_fg, B_w2_fg, fill=W2_COLOR, outline=W2_COLOR)

    # WAGON 3
    A_w3_bg = (267, 13)
    B_w3_bg = (362, 148)
    busShape.create_rectangle(A_w3_bg, B_w3_bg, fill="#BFDFE7", outline="#BFDFE7")

    A_w3_fg = (267, W3_A_Y)
    B_w3_fg = (362, 148)
    busShape.create_rectangle(A_w3_fg, B_w3_fg, fill=W3_COLOR, outline=W3_COLOR)

    # WAGON 4
    A_w4_bg = (367, 13)
    B_w4_bg = (462, 148)
    busShape.create_rectangle(A_w4_bg, B_w4_bg, fill="#BFDFE7", outline="#BFDFE7")

    A_w4_fg = (367, W4_A_Y)
    B_w4_fg = (462, 148)
    busShape.create_rectangle(A_w4_fg, B_w4_fg, fill=W4_COLOR, outline=W4_COLOR)

    # Bus head shape
    A3 = (470, 10)
    B3 = (470, 150)
    C3 = (570, 150)
    D3 = (570, 85)
    E3 = (520, 10)
    busShape.create_polygon(A3, B3, C3, D3, E3)


"""
management of the arrival minute
"""
def arrivalMinute():
    global CUR_MIN_INDEX

    if CUR_MIN_INDEX >= 4:
        CUR_MIN_INDEX = 0
    
    CUR_MIN_INDEX += 1
    return [MIN_02[CUR_MIN_INDEX-1], MIN_08[CUR_MIN_INDEX-1]]


"""
management of the current stop
"""
def currentStop():
    global CUR_STOP_INDEX

    if CUR_STOP_INDEX >= 4:
        CUR_STOP_INDEX = 0
    
    CUR_STOP_INDEX += 1
    return [STOPS_02[CUR_STOP_INDEX-1], STOPS_08[CUR_STOP_INDEX-1]]


def update():
    args = peopleCounter.argsParser()
    num = 150 - 137 * peopleCounter.detectPeople(args) /30
    for i in range(4):
        if i == 0:
            #W1_A_Y = abs(peopleCounter.localDetect("people1.png"))
            #num = 150-137*peopleCounter.localDetect(imagePath)/30
            
            W1_A_Y = abs(num)
            #print(int(W1_A_Y))
        elif i == 1:
            W2_A_Y = abs(num)
        elif i == 2:
            W3_A_Y = abs(randint(MIN, MAX))
        else:
            W4_A_Y = abs(randint(MIN, MAX))
    deltaVal = MAX - MIN
    deltaPerCent = 100
    randPerCent1 = (W1_A_Y-13)*deltaPerCent / deltaVal #deltaVal*curPerCent = deltaPercent*curVal
    randPerCent1 = 100-randPerCent1                    #Inversion of the percentage
    randPerCent2 = (W2_A_Y-13)*deltaPerCent / deltaVal
    randPerCent2 = 100-randPerCent2
    randPerCent3 = (W3_A_Y-13)*deltaPerCent / deltaVal
    randPerCent3 = 100-randPerCent3
    randPerCent4 = (W4_A_Y-13)*deltaPerCent / deltaVal
    randPerCent4 = 100-randPerCent4
    #print(int(randPerCent1))

    if randPerCent1 <= 50:
        W1_COLOR = SATURATION_GREEN
    elif randPerCent1 > 50 and randPerCent1 <= 80:
        W1_COLOR = SATURATION_ORANGE
    else:
        W1_COLOR = SATURATION_RED


    if randPerCent2 <= 50:
        W2_COLOR = SATURATION_GREEN
    elif randPerCent2 > 50 and randPerCent2 <= 80:
        W2_COLOR = SATURATION_ORANGE
    else:
        W2_COLOR = SATURATION_RED


    if randPerCent3 <= 50:
        W3_COLOR = SATURATION_GREEN
    elif randPerCent3 > 50 and randPerCent3 <= 80:
        W3_COLOR = SATURATION_ORANGE
    else:
        W3_COLOR = SATURATION_RED

    if randPerCent4 <= 50:
        W4_COLOR = SATURATION_GREEN
    elif randPerCent4 > 50 and randPerCent4 <= 80:
        W4_COLOR = SATURATION_ORANGE
    else:
        W4_COLOR = SATURATION_RED


    # Recommendation management
    global W_RECOMMENDED

    if min(randPerCent1, randPerCent2, randPerCent3, randPerCent4) == randPerCent1:
        W_RECOMMENDED = "W1"
    elif min(randPerCent1, randPerCent2, randPerCent3, randPerCent4) == randPerCent2:
        W_RECOMMENDED = "W2"
    elif min(randPerCent1, randPerCent2, randPerCent3, randPerCent4) == randPerCent3:
        W_RECOMMENDED = "W3"
    else:
        W_RECOMMENDED = "W4"

    setInformations()
    draw_bus(W1_A_Y, W2_A_Y, W3_A_Y, W4_A_Y, W1_COLOR, W2_COLOR, W3_COLOR, W4_COLOR)

    window.after(5000, update)


update()

# boucle qui permet de lancer la fenêtre
window.mainloop()
