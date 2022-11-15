from tkinter import *
from random import randint

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        width_x=1024
        width_y=768 
        self.master.geometry(str(width_x)+"x"+str(width_y))
        self.master.configure(bg='white')
        self.master.title("OBO")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80,
            outline="#fb0", fill="#fb0")
        canvas.pack(fill=BOTH, expand=1)
        
        lbl=Label(self, text="NOM D'ÂRRET", fg='blue', font=("Helvetica", 16))
        lbl.place(x=width_x/2, y= width_y/10, anchor="center")  

        lbl=Label(self, text=str(randint(0,1000)), fg='gray', font=("Helvetica", 16))
        lbl.place(x=width_x/2, y= width_y/2, anchor="center")

        lbl=Label(self, text="NOM DU SERVICE", fg='black', font=("Helvetica", 16))
        lbl.place(x=width_x/2, y= width_y/6, anchor="center")

        lbl=Label(self, text="Derriere - avant", fg='gray', font=("Helvetica", 16))
        lbl.place(x=width_x/2, y= width_y*5/6, anchor="center")


def update(root):
    root.after(1000, update) # run itself again after 1000 ms

def main():

    root = Tk()
    ex = Example()
    update(root)
    root.mainloop()


if __name__ == '__main__':
    main()