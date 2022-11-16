#Import necessary libraries
from tkinter import *
from random import randint

root = Tk()
width_x=1024
width_y=768 
root.geometry(str(width_x)+"x"+str(width_y))
root.configure(bg='white')
root.title("OBO")


#Define coordinates 
coor_b1 = width_y*9/20
coor_b2 = width_y*15/20

#CANVAS, before text
#Define interface margins
canvas = Canvas(root)
canvas.create_line(0,width_y/5,width_x,width_y/5)
canvas.create_line(0,width_y*3/10,width_x,width_y*3/10)
canvas.create_line(0,width_y*3/5,width_x,width_y*3/5,fill="gray")
canvas.create_line(0,width_y*9/10,width_x,width_y*9/10)

#Define wagon boxes
canvas.create_rectangle(width_x/2-100, coor_b1-100, width_x/2, coor_b1+50, outline="blue", fill="#fb0") ##Bus1
canvas.create_rectangle(width_x/2-100, coor_b2-100, width_x/2, coor_b2+50, outline="blue", fill="#fb0") ##Bus2


canvas.pack(fill=BOTH, expand=1)

#Text, after canvas
arret=Label(root, text="NOM D'ÂRRET", fg='blue', font=("Helvetica", 16))
arret.place(x=width_x/2, y= width_y/20, anchor="center")  

bus_nom=Label(root, text="NOM DU SERVICE", fg='black', font=("Helvetica", 16))
bus_nom.place(x=width_x/2, y= width_y/6, anchor="center")

orient_d=Label(root, text="Derriere", fg='gray', font=("Helvetica", 16))
orient_d.place(x=width_x/6, y= width_y*37/40, anchor="center")

orient_a=Label(root, text="Avant", fg='gray', font=("Helvetica", 16))
orient_a.place(x=width_x*5/6, y= width_y*37/40, anchor="center")

#Chiffre de pourcentage d'encombrement
bus1=Label(root, fg='gray', font=("Helvetica", 16))
bus1.place(x=width_x/2, y= coor_b1+80, anchor="center")

bus2=Label(root, fg='gray', font=("Helvetica", 16))
bus2.place(x=width_x/2, y= coor_b2+80, anchor="center")

#Update data fonction
def update():
   bus1['text'] = str(randint(0,100)) + " %"
   bus2['text'] = str(randint(0,100)) + " %"
   root.after(1000, update) # run itself again after 1000 ms

update()

root.mainloop()
