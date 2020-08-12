#This function will open the second window after the intro window. it closes the old window and opens the new window where the user is asked to register or make a account.
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

    #If the user doesnt have an account they button register will open this window and will close the old window, and open the regiter window where they can register their account.
    def register():
        Slide2.destroy()
        Slide3 = tk.Tk()
        Slide3.title("Sign Up")
        Slide3.geometry("500x470")
        windowWidth = Slide3.winfo_reqwidth()
        windowHeight = Slide3.winfo_reqheight()
        positionRight = int(Slide3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Slide3.winfo_screenheight() / 2 - windowHeight / 2)
        Slide3.geometry("+{}+{}".format(positionRight, positionDown))

        #A Label exsplaing what the user is supoes to do here.
        IntroLabel = tk.Message(Slide3, text="Okay lets get you started, please fill in the following:", font=('times', 15), bg='white', relief="sunken", borderwidth=3, width=500).grid(columnspan=2)

        #Adding the labels that give information on what i want the user to type where.
        NameLabel = tk.Label(Slide3, text="         First Name:", font=('times', 13)).grid(row=2, column=0, sticky="w")
        SurNameLabel = tk.Label(Slide3, text="          Last Name:", font=('times', 13)).grid(row=3, column=0, sticky="w")
        EmailLabel = tk.Label(Slide3, text="    Email Address:", font=('times', 13)).grid(row=4, column=0, sticky="w")
        PhoneLable = tk.Label(Slide3, text="Contact Number:", font=('times', 13)).grid(row=5, column=0, sticky="w")


        UserNameLable = tk.Label(Slide3, text="Username:", font=('times', 15)).grid(row=3, column=1)


        NameEntry = tk.Entry(Slide3, bd=2, cursor="cross", font=("times", 10))
        NameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            NameEntry.delete(0, "end")
            return None
        NameEntry.bind("<Button-1>", some_callback)
        NameEntry.grid(row=2, column=0, padx=95)
        #------------------------------------------------------------------------------
        SurNameEntry = tk.Entry(Slide3, bd=2, cursor="cross", font=("times", 10))
        SurNameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            SurNameEntry.delete(0, "end")
            return None
        SurNameEntry.bind("<Button-1>", some_callback)
        SurNameEntry.grid(row=3, column=0, padx=95)
        #----------------------------------------------------------------------------------
        EmailEntry = tk.Entry(Slide3, bd=2, cursor="cross", font=("times", 10))
        EmailEntry.insert(0, "Type your text here!")
        def some_callback(event):
            EmailEntry.delete(0, "end")
            return None
        EmailEntry.bind("<Button-1>", some_callback)
        EmailEntry.grid(row=4, column=0, padx=95)

        PhoneEntry = tk.Entry(Slide3, bd=2, cursor="cross", font=("times", 10))
        PhoneEntry.insert(0, "Type your text here!")
        def some_callback(event):
            PhoneEntry.delete(0, "end")
            return None
        PhoneEntry.bind("<Button-1>", some_callback)
        PhoneEntry.grid(row=5, column=0, padx=95)







    #If the user does have an account, this function will close the old window and open a login window once the user has clicked the login button.
    def login():
        Slide2.destroy()
        Slide3 = tk.Tk()
        Slide3.title("Sign Up")
        Slide3.geometry("300x270")
        windowWidth = Slide3.winfo_reqwidth()
        windowHeight = Slide3.winfo_reqheight()
        positionRight = int(Slide3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Slide3.winfo_screenheight() / 2 - windowHeight / 2)
        Slide3.geometry("+{}+{}".format(positionRight, positionDown))

    #Button will run the register function once clicked.
    registerbtn = tk.Button(Slide2, text="Register", height=1, width=7, command=register, font=("times", 15), cursor="top_left_arrow", fg="green")
    registerbtn.place(x=50, y=40)

    #Button will run the login function once clicked.
    loginbtn = tk.Button(Slide2, text="Login", height=1, width=7, command=login, font=("times", 15), cursor="top_left_arrow", fg="blue")
    loginbtn.place(x=155, y=40)

    #A Label informing the user what each button does.
    Label1 = tk.Label(Slide2, text="Do you have an account?", bg='white', relief="sunken", borderwidth = 3, font=('times', 13))
    Label1.place(x=60, y=0)
    #This function will run to pop up a meesage box if the user needs helps
    def onClick():
        tk.messagebox.showinfo("Help", "If you dont already have an account register to make one, if you do you can go ahead and login.")

    Helpbutton = tk.Button(Slide2, text="?", command=onClick, fg="red", cursor="question_arrow")
    Helpbutton.place(x=20, y=20)


import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
#Making the introduction window.
root.title("Welcome to Budget calculator")
root.geometry("380x330")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

#Making the intro message that will introduce the user to the program.
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

#This button is the exit button incase the user acsednetly opened the program, and will exit when clicked.
intro_button1 = tk.Button(frame,
                  text="NO",
                  fg="red",
                  command=quit)
intro_button1.pack(side=tk.RIGHT)

#This will run the function (page open) that will start the program.
intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=PageOpen)

intro_button2.pack(side=tk.LEFT)

root.mainloop()
