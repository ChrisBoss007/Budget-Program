#This function will open the second window after the introduction window.
def PageOpen():
    intro_slide.destroy()
    Window2 = tk.Tk()
    Window2.title("Budget")
    Window2.geometry("300x270")
    windowWidth = Window2.winfo_reqwidth()
    windowHeight = Window2.winfo_reqheight()
    positionRight = int(Window2.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(Window2.winfo_screenheight() / 2 - windowHeight / 2)
    Window2.geometry("+{}+{}".format(positionRight, positionDown))

    #If the user does have an account, this function will close the old window and open a login window once the user has clicked the login button.
    def login():
        Window2.withdraw()
        Window3 = tk.Tk()
        Window3.title("Sign Up")
        Window3.geometry("300x270")
        windowWidth = Window3.winfo_reqwidth()
        windowHeight = Window3.winfo_reqheight()
        positionRight = int(Window3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Window3.winfo_screenheight() / 2 - windowHeight / 2)
        Window3.geometry("+{}+{}".format(positionRight, positionDown))





        UserName = tk.Label(Window3, text="Username:", font=('times', 15))
        UserName.place(x=100, y=0)

        def openfile():
            username = UserEntry.get()
            file = open(username, "r")
            lineList = [line.rstrip('\n') for line in open(username)]
            print(lineList)
            password2 = lineList[1]
            print(password2)




        UserEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 13))
        UserEntry.insert(0, "Type your text here!")
        def some_callback(event):
            UserEntry.delete(0, "end")
            return None
        UserEntry.bind("<Button-1>", some_callback)
        UserEntry.place(x=62, y=30)

        UserPassword = tk.Label(Window3, text="Password:", font=('times', 15))
        UserPassword.place(x=105, y=110)

        PasswordEntryt = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 13), show="*")
        PasswordEntryt.insert(0, "")
        def some_callback(event):
            PasswordEntryt.delete(0, "end")
            return None
        PasswordEntryt.bind("<Button-1>", some_callback)
        PasswordEntryt.place(x=62, y=140)

        def Program():
            Window3.withdraw()
            Window4 = tk.Tk()
            Window4.title("Budget Program")
            Window4.geometry("300x270")
            windowWidth = Window4.winfo_reqwidth()
            windowHeight = Window4.winfo_reqheight()
            positionRight = int(Window4.winfo_screenwidth() / 2 - windowWidth / 2)
            positionDown = int(Window4.winfo_screenheight() / 2 - windowHeight / 2)
            Window4.geometry("+{}+{}".format(positionRight, positionDown))

        Startbtn = tk.Button(Window3, text="Log on", height=1, width=7, command=Program, font=("times", 15), cursor="top_left_arrow", fg="green")
        Startbtn.place(x=105, y=180)

        Nextbtn = tk.Button(Window3, text="Submit", height=1, width=7, command=lambda: openfile(), font=("times", 15), cursor="top_left_arrow", fg="green")
        Nextbtn.place(x=105, y=65)

        Recoverbtn = tk.Button(Window3, text="Forgot Password?", cursor="top_left_arrow", fg="blue")
        Recoverbtn.place(x=170, y=230)


    #If the user doesnt have an account they button register will open this window and will close the old window, and open the regiter window where they can register their account.
    def register():
        Window2.withdraw()
        Window3 = tk.Tk()
        Window3.title("Sign Up")
        Window3.geometry("450x320")
        windowWidth = Window3.winfo_reqwidth()
        windowHeight = Window3.winfo_reqheight()
        positionRight = int(Window3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Window3.winfo_screenheight() / 2 - windowHeight / 2)
        Window3.geometry("+{}+{}".format(positionRight, positionDown))

        name_var=tk.StringVar()
        passw_var=tk.StringVar()


        #This is where the value of the users unsername and password is saved.
        #A Label exsplaing what the user is supoes to do here.
        IntroLabel = tk.Message(Window3, text="Okay lets get you started, please fill in the following:", font=('times', 15), bg='white', relief="sunken", borderwidth=3, width=500).grid(columnspan=2)

        #Adding the labels that give information on what i want the user to type where.
        NameLabel = tk.Label(Window3, text="         First Name:", font=('times', 13)).grid(row=2, column=0, sticky="w")
        SurNameLabel = tk.Label(Window3, text="          Last Name:", font=('times', 13)).grid(row=3, column=0, sticky="w")
        EmailLabel = tk.Label(Window3, text="    Email Address:", font=('times', 13)).grid(row=4, column=0, sticky="w")
        PhoneLable = tk.Label(Window3, text="Contact Number:", font=('times', 13)).grid(row=5, column=0, sticky="w")
        UserNameLable = tk.Label(Window3, text="Username:", font=('times', 15)).grid(row=9, column=0)
        PasswordLable = tk.Label(Window3, text="Password:", font=('times', 15)).grid(row=12, column=0)

        #Entry functions to save users information/
        NameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        NameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            NameEntry.delete(0, "end")
            return None
        NameEntry.bind("<Button-1>", some_callback)
        NameEntry.grid(row=2, column=0, padx=95)
        #------------------------------------------------------------------------------
        SurNameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        SurNameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            SurNameEntry.delete(0, "end")
            return None
        SurNameEntry.bind("<Button-1>", some_callback)
        SurNameEntry.grid(row=3, column=0, padx=95)
        #----------------------------------------------------------------------------------
        EmailEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        EmailEntry.insert(0, "Type your text here!")
        def some_callback(event):
            EmailEntry.delete(0, "end")
            return None
        EmailEntry.bind("<Button-1>", some_callback)
        EmailEntry.grid(row=4, column=0, padx=95)
        #------------------------------------------------------------------------------------
        PhoneEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        PhoneEntry.insert(0, "Type your text here!")
        def some_callback(event):
            PhoneEntry.delete(0, "end")
            return None
        PhoneEntry.bind("<Button-1>", some_callback)
        PhoneEntry.grid(row=5, column=0, padx=95)
        #This is the username entry and will save a text file with the username as the name of the file.
        UserNameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10), textvariable = name_var)
        UserNameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            UserNameEntry.delete(0, "end")
            return None
        UserNameEntry.bind("<Button-1>", some_callback)
        UserNameEntry.grid(row=10, column=0, padx=95)
        #This function will make a new file and write all the nessacary inforamtion to make thier account.
        def write_File (text_File, passw_var):

            #This is where i get all the values of the entrys.
            name=UserNameEntry.get()
            password=PasswordEntry.get()
            email=EmailEntry.get()
            phonenumber=PhoneEntry.get()
            firstname=NameEntry.get()
            surname=SurNameEntry.get()
            #This checks that the password is being saved.
            print("The name is : " + name)
            print("The password is : " + password)

            name_var.set("")
            passw_var.set("")
            #This writes all the values into the file then closes it.
            file = open(name, "a")
            user_Input = text_File.get()
            file.write("Username: " + user_Input)
            file.write("\n")
            file.write("Password: " + password)
            file.write("\n")
            file.write("FistName: " + firstname)
            file.write("\n")
            file.write("SurName: " + surname)
            file.write("\n")
            file.write("Email: " + email)
            file.write("\n")
            file.write("Phone number: " + phonenumber)
            file.close()
            return name, password


        #This is the password entry.
        PasswordEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10), textvariable = passw_var, show="*")
        PasswordEntry.insert(0, "")
        def some_callback(event):
            PasswordEntry.delete(0, "end")
            return None
        PasswordEntry.bind("<Button-1>", some_callback)
        PasswordEntry.grid(row=13, column=0, padx=95)

        #Button will save their password and username.
        Submitbtn = tk.Button(Window3, text="Submit", height=1, width=7, font=("times", 15), cursor="top_left_arrow", fg="green", command=lambda: write_File(UserNameEntry, passw_var)) #THis was Password entry but i changed it to Username entry not sure what that does
        Submitbtn.grid(row=17, column=0)

        #Button will run the login function once clicked.
        Contuinebtn = tk.Button(Window3, text="Contuine", height=1, width=7, font=("times", 15), cursor="top_left_arrow", fg="blue", command=login)
        Contuinebtn.grid(row=19, column=0)


    #This is part of the pageopen function and will ask the user to register or login.
    #Button will run the register function once clicked.
    registerbtn = tk.Button(Window2, text="Register", height=1, width=7, command=register, font=("times", 15), cursor="top_left_arrow", fg="green")
    registerbtn.place(x=50, y=40)

    #Button will run the login function once clicked.
    loginbtn = tk.Button(Window2, text="Login", height=1, width=7, command=login, font=("times", 15), cursor="top_left_arrow", fg="blue")
    loginbtn.place(x=155, y=40)

    #A Label informing the user what each button does.
    Label1 = tk.Label(Window2, text="Do you have an account?", bg='white', relief="sunken", borderwidth = 3, font=('times', 13))
    Label1.place(x=60, y=0)
    #This function will run to pop up a mesage box if the user needs helps
    def onClick():
        tk.messagebox.showinfo("Help", "If you dont already have an account register to make one, if you do you can go ahead and login.")
    #This button runs the function to show a help message.
    Helpbutton = tk.Button(Window2, text="?", command=onClick, fg="red", cursor="question_arrow")
    Helpbutton.place(x=20, y=20)


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os as os
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

#This button is the exit button incase the user acsednetly opened the program, and will quit the program when clicked.
intro_button1 = tk.Button(frame,
                  text="NO",
                  fg="red",
                  command=quit)
intro_button1.pack(side=tk.RIGHT)

#This will run the function (page open) that will open the second window.
intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=PageOpen)

intro_button2.pack(side=tk.LEFT)

root.mainloop()
