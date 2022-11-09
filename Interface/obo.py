from tkinter import *

width_x=1024
width_y=768
tk = Tk(); tk.geometry(str(width_x)+"x"+str(width_y)); tk.title('OBO')
tk.configure(bg='white')

lbl=Label(tk, text="NOM D'ÂRRET", fg='blue', font=("Helvetica", 16))
lbl.place(x=width_x/2, y= width_y/10, anchor="center")

lbl=Label(tk, text="NOM DU SERVICE", fg='black', font=("Helvetica", 16))
lbl.place(x=width_x/2, y= width_y/6, anchor="center")

lbl=Label(tk, text="% encombrement", fg='gray', font=("Helvetica", 16))
lbl.place(x=width_x/2, y= width_y/2, anchor="center")

lbl=Label(tk, text="Derriere - avant", fg='gray', font=("Helvetica", 16))
lbl.place(x=width_x/2, y= width_y*5/6, anchor="center")

tk.mainloop()
