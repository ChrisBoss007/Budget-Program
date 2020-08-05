import tkinter as tk
root = tk.Tk()
root.title("Welcome to Budget calculator")
root.geometry("380x330")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

intro_slide = root
intro_message1 = "Welcome! \n To budget calculator"
intro_msg = tk.Message(root, text = intro_message1, justify="center")
intro_msg.config(fg="Yellow", bg="Black", font=('times', 20, 'italic'))
intro_msg.pack()

intro_message2 = "Here you can deposit or withdraw money and see your progress towards your goals, and insert your income and expenses and we will draw up a plan to solve your finance situation."
intro_msg2 = tk.Message(root, text = intro_message2)
intro_msg2.config(bg='white', relief="sunken", borderwidth = 3, font=('times', 17))
intro_msg2.pack()

intro_label = tk.Label(root, text="Are you ready to start?", font=("times", 15))
intro_label.pack()

frame = tk.Frame(root)
frame.pack()

intro_button1 = tk.Button(frame,
                  text="NO",
                  fg="red",
                  command=quit)
intro_button1.pack(side=tk.RIGHT)



def PageOpen():
    intro_slide.destroy()
    Slide2 = tk.Tk()
    Slide2.title("Budget")
    Slide2.geometry("300x270")
    windowWidth = Slide2.winfo_reqwidth()
    windowHeight = Slide2.winfo_reqheight()
    positionRight = int(Slide2.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(Slide2.winfo_screenheight() / 2 - windowHeight / 2)
    Slide2.geometry("+{}+{}".format(positionRight, positionDown))

    def register():
        Slide2.destroy()
        Slide3 = tk.Tk()
        Slide3.title("Budget")
        Slide3.geometry("300x270")
        windowWidth = Slide3.winfo_reqwidth()
        windowHeight = Slide3.winfo_reqheight()
        positionRight = int(Slide3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Slide3.winfo_screenheight() / 2 - windowHeight / 2)
        Slide3.geometry("+{}+{}".format(positionRight, positionDown))


    def login():
        print("Works")

    registerbtn = tk.Button(Slide2, text="Register", height = 10, width = 20, command=register)
    registerbtn.pack(fill=tk.Y, side=tk.LEFT, pady=30)

    loginbtn = tk.Button(Slide2, text="Login", height = 10, width = 20, command=login)
    loginbtn.pack(side=tk.RIGHT, fill=tk.Y, pady=30)

    Label1 = tk.Label(Slide2, text="Do you have an account?", bg='white', relief="sunken", borderwidth = 3, font=('times', 13))
    Label1.place(x=60, y=3)





intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=PageOpen)

intro_button2.pack(side=tk.LEFT)

root.mainloop()
