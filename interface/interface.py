#Import necessary libraries
from tkinter import *
from random import randint

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
def update():
    bus_full1 = randint(0,100)
    for i in range(4):
        bus1_t[i]= str(bus_full1) + " %"
    #bus2['text'] = str(randint(0,100)) + " %"
    draw(bus_full1)
    root.after(1000, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()