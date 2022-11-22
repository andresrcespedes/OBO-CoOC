#Import necessary libraries
from tkinter import *
from random import randint

### Max number of passangers in a wagon
max = 45

#Start Tkinter
root = Tk()
width_x=1024
width_y=768
root.geometry(str(width_x)+"x"+str(width_y))
root.configure(bg='white')
root.title("OBO")
color_wag = '#350E54'
color_bg = '#D1D975'
color_arret = '#6C7314'
color_line = '#858A41'

#Dimension information boxes
marg = 24
w_box = 150
bus_x =[-(2*w_box+marg*3/2)+width_x/2,-(w_box+marg/2)+width_x/2,marg/2+width_x/2,marg*3/2+w_box+width_x/2]


#Buses information
bus1_t=[None,None,None,None]
coor_b1 = width_y*9/20 + 70
coor_b2 = width_y*15/20 + 70

#CANVAS, before labels
canvas = Canvas(root)
canvas.configure(bg=color_bg)
canvas.pack(fill=BOTH, expand=1)


def draw(bus_full1):
    canvas.delete('all')
    #Define interface margins
    canvas.create_rectangle(0,0,width_x,width_y/10,outline=color_line, fill=color_arret) #Arret
    canvas.create_rectangle(0,width_y/10,width_x,width_y*3/10,outline=color_line, fill=color_arret) #Bus Name
    canvas.create_line(0,width_y*3/5,width_x,width_y*3/5,fill=color_arret)
    canvas.create_line(0,width_y*9/10,width_x,width_y*9/10,fill=color_arret)
    canvas.create_text(width_x/2,width_y/20, text="NOM D'ÂRRET", fill="black", font=('Helvetica 28 bold'))
    canvas.create_text(width_x/2,width_y/5, text="NOM DU SERVICE", fill="black", font=('Helvetica 28 bold'))
    canvas.create_text(width_x/6, width_y*37/40, text="Derriere", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(width_x*5/6, width_y*37/40, text="Avant", fill="black", font=('Helvetica 15 bold'))

    #Wagon canva
    for i in range(4):
        canvas.create_text(bus_x[i]+w_box/2,coor_b1+20,text= bus1_t[i],fill='black',font=('Helvetica 15 bold'))
        canvas.create_rectangle(bus_x[i], coor_b1-bus_full1*140/max,bus_x[i]+w_box, coor_b1, outline=color_wag, fill=color_wag) ##Bus1
    #canvas.create_rectangle(width_x/2-w_box, coor_b2-100, width_x/2, coor_b2, outline=color_wag, fill=color_wag) ##Bus2
    canvas.pack(fill=BOTH, expand=1)

def update():
    bus_full1 = randint(0,max) #Signal input
    for i in range(4):
        bus1_t[i]= str(int(bus_full1*100/max)) + " %"
    #bus2['text'] = str(randint(0,100)) + " %"
    draw(bus_full1)
    root.after(1000, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()
