#Trialling the .grid() method
import tkinter
root=tkinter.Tk()
for r in range(3):
    for c in range(4):
        tkinter.Label(root, text='Row%s/Column%s'%(r,c), borderwidth=1).grid(row=r,column=c)
root.mainloop()
