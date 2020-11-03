# Please refer to line() where the program actually starts.
# Once the 'Yes' button has been clicked on the first window, it will run this function.
# This function will destroy the first window 'intro_slide' and open a new window 'Window2' and sets the dimensions and other details for this window which are written underneath:
def PageOpen():
    intro_slide.destroy()
    Window2 = tk.Tk()
    Window2.title("Account information")
    Window2.geometry("300x100")
    windowWidth = Window2.winfo_reqwidth()
    windowHeight = Window2.winfo_reqheight()
    positionRight = int(Window2.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(Window2.winfo_screenheight() / 2 - windowHeight / 2)
    Window2.geometry("+{}+{}".format(positionRight, positionDown))
#--------------------------------------------------------------------------------------------------------------------------------------------------

    # If the user has a existing account they can login in by pressing the 'login' button -[line 388] on the previous window 'window2', witch will run this function.
    def login():
        # This is where i close the previous window 'Window2', and i open a new window 'Window3', and below is where i set the dimension for the new window:
        Window2.withdraw()
        Window4 = tk.Tk()
        Window4.title("Sign In")
        Window4.geometry("300x270")
        windowWidth = Window4.winfo_reqwidth()
        windowHeight = Window4.winfo_reqheight()
        positionRight = int(Window4.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Window4.winfo_screenheight() / 2 - windowHeight / 2)
        Window4.geometry("+{}+{}".format(positionRight, positionDown))
        #--------------------------------------------------------------------------------------------------------------------------------------------------

        # This label informs the user what they should type in the corresponding entry below. -[line 50]
        UserName = tk.Label(Window4, text="Username:", font=('times', 15))
        UserName.place(x=100, y=20)
        #--------------------------------------------------------------------------------------------------------------------------------------------------

        # This function will search for a text file with the same name as what ever the user typed in when making an account, it will then check if the password typed in is the same as the one that is on the text file,
        # if it is the same it will grant access and make the 'log on' button usable, if not it will print error, and the 'log on' button will remain disabled.
        def openfile():
            # This is where i 'get' the values of the entry where the user entered their information.
            username = UserEntry.get() # -[line 54].
            passwordt = PasswordEntryt.get() # -[line 65].
            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # This is where i open the file with the same name as whatever the users entered or set as their username.
            try:
                file = open(username, "r")
                
            except OSError:
                tk.messagebox.showinfo("Error", "Usersname invalid, account not found")
            lineList = [line.rstrip('\n') for line in open(username)]
            print(lineList)

            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # This is where it checks if the password that the user entered, matches the password set user the username that they have entered.
            password2 = lineList[1]
            print(password2)
            name = lineList[2]
            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # If the user has entered the correct password they can move on to the program by clicking the 'Submit' button -[line 236].
            # This code below will make the button that open the program avalibil to use, so they can only click the button (that takes them to the program) if their password is correct, if not this button will be unlclickeable.
            if passwordt == password2:
                tk.messagebox.showinfo("Acepted", "Password acepted welcome back " + name)
                if (Startbtn['state'] == tk.NORMAL):
                    Startbtn['state'] = tk.DISABLED
                else:
                    Startbtn['state'] = tk.NORMAL
            else:
                tk.messagebox.showinfo("Error", "Username or Password is incorect")
             #--------------------------------------------------------------------------------------------------------------------------------------------------


        # For this entry the user is asked to enter their 'username',
        # This entry saves the users input to 'UserEntry', it also display the sentence 'type your text here' and the function below -[line 69] will clear the entry once the user has clicked on it.
        UserEntry = tk.Entry(Window4, bd=2, cursor="cross", font=("times", 13))
        UserEntry.insert(0, "Type your text here!")
        def some_callback(event):
            UserEntry.delete(0, "end")
            return None
        UserEntry.bind("<Button-1>", some_callback)
        UserEntry.place(x=62, y=50)
        #--------------------------------------------------------------------------------------------------------------------------------------------------

        # This label informs the user what they should type in in the corresponding entry below. -[line 79]
        UserPassword = tk.Label(Window4, text="Password:", font=('times', 15))
        UserPassword.place(x=105, y=90)
        #--------------------------------------------------------------------------------------------------------------------------------------------------

        # For this entry the user is asked to enter their 'password',
        # This entry saves the users input to 'PasswordEntry', it also display the sentence 'type your text here' and the function below -[line 85] will clear the entry once the user has clicked on it.
        PasswordEntryt = tk.Entry(Window4, bd=2, cursor="cross", font=("times", 13), show="*")
        PasswordEntryt.insert(0, "")
        def some_callback(event):
            PasswordEntryt.delete(0, "end")
            return None
        PasswordEntryt.bind("<Button-1>", some_callback)
        PasswordEntryt.place(x=62, y=120)
        #--------------------------------------------------------------------------------------------------------------------------------------------------





        #This function is where the main calculator is found, here it will ask the users for its financial information and respond by giving them there total amount of money they make.
        def Program():
            #This is where it closes the previous window (Window3), and opens a new window (Window4) and below that i simply set the dimensions for this new window.
            Window4.withdraw()
            Window5 = tk.Tk()
            Window5.title("Budget Program")
            Window5.geometry("800x400")
            windowWidth = Window5.winfo_reqwidth()
            windowHeight = Window5.winfo_reqheight()
            positionRight = int(Window5.winfo_screenwidth() / 2 - windowWidth / 2)
            positionDown = int(Window5.winfo_screenheight() / 2 - windowHeight / 2)
            Window5.geometry("+{}+{}".format(positionRight, positionDown))
            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # This is a class that makes a row consting of 3 entrys, each time the users clicks the 'add income' button
            class App(object):
                def new_row(self):

                    Unique_Val = 0
                    Unique_Val_A = 0

                    v = tk.StringVar()
                    entry_Box = "new_entry{}".format(Unique_Val)
                    entry_Box = tk.Entry(Window5, width=15, textvariable=v)
                    name = entry_Box.insert(0, "Name of income")
                    Unique_Val += 1

                    entry_Box2 = "new_entry2{}".format(Unique_Val_A)
                    entry_Box2 = tk.Entry(Window5, width=8)
                    amount = entry_Box2.insert(0, "Amount")
                    Unique_Val_A += 1

                    rate = OptionList = [
                    "Hourly",
                    "Daily",
                    "Weekly",
                    "Monthly"
                    ]
                    variable = tk.StringVar(Window5)
                    variable.set(OptionList[0])

                    opt = tk.OptionMenu(Window5, variable, *OptionList)
                    opt.config(width=5, font=('Helvetica', 6))

                    blank = tk.Label(Window5, text="  ")

                    # Put widgets in grid
                    self.num_rows += 1
                    self.num_rows2 += 1
                    self.num_rows3 += 1
                    self.num_rows4 += 1

                    opt.grid(column=3, row=self.num_rows3)
                    opt.bind("<Button-1>")

                    entry_Box.grid(column=0, row=self.num_rows)
                    def some_callback(event):
                        entry_Box.delete(0, "end")
                        return None
                    entry_Box.bind("<Button-1>", some_callback)

                    entry_Box2.grid(column=1, row=self.num_rows2)
                    def some_callback(event):
                        entry_Box2.delete(0, "end")
                        return None
                    entry_Box2.bind("<Button-1>", some_callback)

                    blank.grid(column=6, row=self.num_rows4, padx=180)

                    self.lst1.append(entry_Box)
                    self.lst2.append(entry_Box2)

                    return entry_Box, entry_Box2, rate

                def save(self, lst1, lst2):
                    open('income.txt', 'w').close()
                    print("List length ", len(lst1))
                    for i in range (len(lst1)):
                        print(lst1[i].get())

                    print("List length ", len(lst2))
                    for x in range (len(lst2)):
                        print(lst2[x].get())
                        file = open('income.txt', 'a')
                        file.write(self.lst2[x].get())
                        file.write('\n')
                        file.close()

                def __init__(self):
                    self.num_rows = 1
                    self.num_rows2 = 1
                    self.num_rows3 = 1
                    self.num_rows4 = 1
                    self.lst1 = []
                    self.lst2 = []
                    createRow_button = tk.Button(
                            Window5, text='Add income row', command=self.new_row)
                    createRow_button.place(x=240, y=0)
                    savebtn = tk.Button(Window5, text="save income", command=lambda: self.save(self.lst1, self.lst2))
                    savebtn.place(x=245, y=70)



            class App2(object):
                def new_row2(self):
                    Unique_Val2 = 0
                    Unique_Val_2A = 0

                    v = tk.StringVar()
                    entry_Box3 = "new_entry3{}".format(Unique_Val2)
                    entry_Box3 = tk.Entry(Window5, width=15, textvariable=v)
                    name2 = entry_Box3.insert(0, "Name of income")
                    Unique_Val2 += 1

                    entry_Box4 = "new_entry4{}".format(Unique_Val_2A)
                    entry_Box4 = tk.Entry(Window5, width=8)
                    amount2 = entry_Box4.insert(0, "Amount")
                    Unique_Val_2A += 1

                    rate2 = OptionList2 = [
                    "Hourly",
                    "Daily",
                    "Weekly",
                    "Monthly"
                    ]
                    variable2 = tk.StringVar(Window5)
                    variable2.set(OptionList2[0])

                    opt2 = tk.OptionMenu(Window5, variable2, *OptionList2)
                    opt2.config(width=5, font=('Helvetica', 6))

                    # Put widgets in grid
                    self.num_rows += 1
                    self.num_rows2 += 1
                    self.num_rows3 += 1

                    opt2.grid(column=9, row=self.num_rows3)
                    opt2.bind("<Button-1>")

                    entry_Box3.grid(column=7, row=self.num_rows)
                    def some_callback(event):
                        entry_Box3.delete(0, "end")
                        return None
                    entry_Box3.bind("<Button-1>", some_callback)

                    entry_Box4.grid(column=8, row=self.num_rows2)
                    def some_callback(event):
                        entry_Box4.delete(0, "end")
                        return None
                    entry_Box4.bind("<Button-1>", some_callback)

                    self.lst3.append(entry_Box3)
                    self.lst4.append(entry_Box4)

                    return entry_Box3, entry_Box4, rate2

                def save2(self, lst3, lst4):
                    open('outcome.txt', 'w').close()
                    print("List length ", len(lst3))
                    for j in range (len(lst3)):
                        print(lst3[j].get())

                    print("List length ", len(lst4))
                    for y in range (len(lst4)):
                        print(lst4[y].get())
                        file = open('outcome.txt', 'a')
                        file.write(self.lst4[y].get())
                        file.write('\n')
                        file.close()
 
                def __init__(self):
                    self.num_rows = 1
                    self.num_rows2 = 1
                    self.num_rows3 = 1
                    self.lst3 = []
                    self.lst4 = []
                    createRow_button2 = tk.Button(
                            Window5, text='Add outcome row', command=self.new_row2)
                    createRow_button2.place(x=440, y=0)
                    savebtn2 = tk.Button(Window5, text="save outcome", command=lambda: self.save2(self.lst3, self.lst4))
                    savebtn2.place(x=440, y=70)
            app = App()
            app2 = App2()

            def Calculate():
                # Here the codesets the varible 'total' to 0 so that it will start from 0 and not give random answers.
                totali = 0
                totalo = 0

                file = open('income.txt', 'r')
                income = [line.rstrip('\n') for line in open('income.txt')]

                file = open('outcome.txt', 'r')
                outcome = [line.rstrip('\n') for line in open('outcome.txt')]

                for x in range(0, len(income)):
                    totali = totali + int(income[x])
                print('income: ', totali)

                for y in range(0, len(outcome)):
                    totalo = totalo + int(outcome[y])

                print("outcome :", totalo)


                budget = totali - totalo

                print("Main :", budget)

                # This Label presents the user with the end resluts based on the users input.
                Totallabel = tk.Label(Window5, text= "Total Income: " + str(totali) + ('\n') + "Total Outcome: " + str(totalo) + ('\n') + "Budget: " + str(budget))
                Totallabel.place(x=325, y=160)
                #--------------------------------------------------------------------------------------------------------------------------------------------------


            # This lable simply explains to the user what the button below it does.
            Submitlabel = tk.Label(Window5, text="When you are done click below to save your entred value, \n PLEASE make sure that you only numbers into  the entrys", )
            Submitlabel.place(x=240, y=30)
            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # This label simply explains to the user what the button below it does.
            Callabel = tk.Label(Window5, text="When you are done click below to work out your budget.", )
            Callabel.place(x=240, y=105)
            #--------------------------------------------------------------------------------------------------------------------------------------------------

            # This button will run the funcion 'Calculate'
            # Which will open the file containg all the financial informantion entered by the user, and will take those values and preform calculations with them and present the user with the reslusts.
            Calculatebtn = tk.Button(Window5, text="Calcuate", command=lambda: Calculate())
            Calculatebtn.place(x=350, y=130)
            #------------------------------------------------------------------------------------------------------------------------------------------------------






        # When this button is clicked checks username and password
        # it will run the function 'openfile()' -[line 30]: opens file, get username and find in the password file, compare with data in entryboxes.
        Nextbtn = tk.Button(Window4, text="Submit", height=1, width=7, command=lambda: openfile(), font=("times", 15), cursor="top_left_arrow", fg="green") # -[line 30].
        Nextbtn.place(x=60, y=180)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # Once the user has resentered the username and password that the chose when registering, then they can click this 'logon' button witch will take them straight to the program IF their password is correct.
        # Once this button is clicked it will run the function 'Program' -[line 70].
        Startbtn = tk.Button(Window4, text="Log on", height=1, width=7, command=Program, font=("times", 15), cursor="top_left_arrow", fg="green", state=tk.DISABLED) # -[line 70].
        Startbtn.place(x=160, y=180)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # This button will aid the users in recoverying thier username and password in case they have forgotten it.
        # As of now it doesnt work.
        Recoverbtn = tk.Button(Window4, text="Forgot Password?", cursor="top_left_arrow", fg="blue")
        Recoverbtn.place(x=170, y=230)
        #------------------------------------------------------------------------------------------------------------------------------------------------------


    # If the user doesnt have an account they can click 'register' on window 2 -[line 400], witch will run this function.
    # This function will destroy the last window and open a new window, 'window3'.
    def register():
        # This is were is set the dimensions for the 'register' slide.
        Window2.withdraw()
        Window3 = tk.Tk()
        Window3.title("Sign Up")
        Window3.geometry("442x320")
        windowWidth = Window3.winfo_reqwidth()
        windowHeight = Window3.winfo_reqheight()
        positionRight = int(Window3.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(Window3.winfo_screenheight() / 2 - windowHeight / 2)
        Window3.geometry("+{}+{}".format(positionRight, positionDown))
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        name_var = tk.StringVar()
        passw_var = tk.StringVar()
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # This is a message that explains what this slides perpouse is.
        IntroLabel = tk.Message(Window3, text="Okay lets get you started, please fill in the following:", font=('times', 15), bg='white', relief="sunken", borderwidth=3, width=500).grid(columnspan=2)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # Below are a list of labels that inform the user what they should type in in the box next to the corresponding label.
        NameLabel = tk.Label(Window3, text="         First Name:", font=('times', 13)).grid(row=2, column=0, sticky="w")
        SurNameLabel = tk.Label(Window3, text="          Last Name:", font=('times', 13)).grid(row=3, column=0, sticky="w")
        EmailLabel = tk.Label(Window3, text="    Email Address:", font=('times', 13)).grid(row=4, column=0, sticky="w")
        PhoneLable = tk.Label(Window3, text="Contact Number:", font=('times', 13)).grid(row=5, column=0, sticky="w")
        UserNameLable = tk.Label(Window3, text="Username:", font=('times', 15)).grid(row=9, column=0)
        PasswordLable = tk.Label(Window3, text="Password:", font=('times', 15)).grid(row=12, column=0)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # For this entry the user is asked to enter a 'name' of their choice into a entry, witch will later be saved.
        # This entry saves the users input to 'NameEntry', it also display the sentence 'type your text here' and the function below -[line 392] will clear the entry once the user has clicked on it.
        NameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        NameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            NameEntry.delete(0, "end")
            return None
        NameEntry.bind("<Button-1>", some_callback)
        NameEntry.grid(row=2, column=0, padx=95)
        #------------------------------------------------------------------------------

        # For this entry the user is asked to enter a 'surname' of their choice into a entry, witch will later be saved.
        # This entry saves the users input to 'SurNameEntry', it also display the sentence 'type your text here' and the function below -[line 392] will clear the entry once the user has clicked on it.
        SurNameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        SurNameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            SurNameEntry.delete(0, "end")
            return None
        SurNameEntry.bind("<Button-1>", some_callback)
        SurNameEntry.grid(row=3, column=0, padx=95)
        #----------------------------------------------------------------------------------

        # For this entry the user is asked to enter a 'email' of their choice into a entry, witch will later be saved.
        # This entry saves the users input to 'EmailEntry', it also display the sentence 'type your text here' and the function below -[line 303] will clear the entry once the user has clicked on it.
        EmailEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        EmailEntry.insert(0, "Type your text here!")
        def some_callback(event):
            EmailEntry.delete(0, "end")
            return None
        EmailEntry.bind("<Button-1>", some_callback)
        EmailEntry.grid(row=4, column=0, padx=95)
        #------------------------------------------------------------------------------------

        # For this entry the user is asked to enter a 'phone number' of their choice into a entry, witch will later be saved.
        # This entry saves the users input to 'PhoneEntry', it also display the sentence 'type your text here' and the function below -[line 311] will clear the entry once the user has clicked on it.
        PhoneEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10))
        PhoneEntry.insert(0, "Type your text here!")
        def some_callback(event):
            PhoneEntry.delete(0, "end")
            return None
        PhoneEntry.bind("<Button-1>", some_callback)
        PhoneEntry.grid(row=5, column=0, padx=95)
        #------------------------------------------------------------------------------------

        # For this entry the user is asked to enter a username of their choice into a entry, witch will later be saved.
        # This entry saves the users input to 'name_var', by setting the 'textvariable' to a unique variable, this entry also display the sentence 'type your text here' and the function below -[line 318] will clear the entry once the user has clicked on it.
        UserNameEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10), textvariable = name_var)
        UserNameEntry.insert(0, "Type your text here!")
        def some_callback(event):
            UserNameEntry.delete(0, "end")
            return None
        UserNameEntry.bind("<Button-1>", some_callback)
        UserNameEntry.grid(row=10, column=0, padx=95)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # Once the user is happy with their username and password, they can click submit witch will run this function, witch will save all their information on this PC.
        # This function 'gets ()' all the values from all the entry's, and then opens a new text file and writes all the information in that file, effectively saving all the users information when the 'Submit' -[line 367] button is clicked.
        def write_File (text_File, passw_var):
            # This is where it finds and gets all the values of the entry's, and saves them as a unique variable.
            name = UserNameEntry.get()
            password = PasswordEntry.get()
            email = EmailEntry.get()
            phonenumber = PhoneEntry.get()
            firstname = NameEntry.get()
            surname = SurNameEntry.get()
            #------------------------------------------------------------------------------------------------------------------------------------------------------

            name_var.set("")
            passw_var.set("")
            #------------------------------------------------------------------------------------------------------------------------------------------------------

            # This opens a new text file and writes all the information into it, using the unique variables made above. -[line 326-331]
            if len(password) < 8:
                print("Make sure your password is at lest 8 letters")
                tk.messagebox.showinfo("Error", "Make sure your password is at lest 8 letters")
            else:
                tk.messagebox.showinfo("Perfect", "Your password is strong")
                file = open(name, "a")
                user_Input = text_File.get()
                file.write("Username: " + user_Input)
                file.write("\n")
                file.write(password)
                file.write("\n")
                file.write(firstname)
                file.write("\n")
                file.write("SurName: " + surname)
                file.write("\n")
                file.write("Email: " + email)
                file.write("\n")
                file.write("Phone number: " + phonenumber)
                file.close()
                return name, password
            #------------------------------------------------------------------------------------------------------------------------------------------------------


        # This is an entry where the user is asked to enter a password of their choice.
        # The password will be saved as 'pass_var' by setting it 'textvarible' to a variable of my choice, this entry display the sentence 'type your text here' and the function below -[line 360] will clear the entry once the user has clicked on it.
        PasswordEntry = tk.Entry(Window3, bd=2, cursor="cross", font=("times", 10), textvariable = passw_var, show="*")
        PasswordEntry.insert(0, "")
        def some_callback(event):
            PasswordEntry.delete(0, "end")
            return None
        PasswordEntry.bind("<Button-1>", some_callback)
        PasswordEntry.grid(row=13, column=0, padx=95)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # Once the user is happy with their chosen password and username they can click this button witch will save their chosen password and username as a text file on this PC.
        # If this button is clicked it will run the function 'write_File' -[line 323].
        Submitbtn = tk.Button(Window3, text="Submit", height=1, width=7, font=("times", 15), cursor="top_left_arrow", fg="green", command=lambda: write_File(UserNameEntry, passw_var)) # -[line 323].
        Submitbtn.grid(row=17, column=0)
        #------------------------------------------------------------------------------------------------------------------------------------------------------

        # If the user is finished registering they can move on ti the login screen by clicking this button.
        # This button will run the function 'login' -[line 15].
        Contuinebtn = tk.Button(Window3, text="Contuine", height=1, width=7, font=("times", 15), cursor="top_left_arrow", fg="blue", command=login) # -[line 15].
        Contuinebtn.grid(row=19, column=0)
        #------------------------------------------------------------------------------------------------------------------------------------------------------


    # This code is part of the second window, witch will ask the user to log in (if they have a account) or register (if they are new and dont have an account), as well as a help button explaining what to do.
    # If the users doesnt have an account the will be asked to register, and when this button is clicked it will take them to the register slide.
    # For this button i set the 'command' to 'register' witch will run the (register) function. -[line 255]
    registerbtn = tk.Button(Window2, text="Register", height=1, width=7, command=register, font=("times", 15), cursor="top_left_arrow", fg="green") #-[line 255]
    registerbtn.place(x=50, y=40)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    # If the user has an account they can 'login', witch will take them stright to the login window where they will be asked to enter their username and password.
    # For this button is set the 'command'  to 'login', witch will run the function (login)-[line 15].
    loginbtn = tk.Button(Window2, text="Login", height=1, width=7, command=login, font=("times", 15), cursor="top_left_arrow", fg="blue") #-[line 15]
    loginbtn.place(x=155, y=40)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    # This label asks the user if they have a account, the user can select 'login' if they do and 'register' if they do not.
    Label1 = tk.Label(Window2, text="Do you have an account?", bg='white', relief="sunken", borderwidth = 3, font=('times', 13))
    Label1.place(x=60, y=0)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function will create a pop up a 'message box' using 'messagebox' from tkinter, in case the users doesnt understand what to do.
    def Help():
        tk.messagebox.showinfo("Help", "If you dont already have an account register to make one, if you do you can go ahead and login.")
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    # If the user is unsure what to do they ca click on this button witch will bring up a pop up message explaining what to do on this window.
    # For this button is set the 'command'  to 'Help', witch will run the function (Help)-[line 394].
    Helpbutton = tk.Button(Window2, text="?", command=Help, fg="red", cursor="question_arrow")
    Helpbutton.place(x=20, y=20)
    #------------------------------------------------------------------------------------------------------------------------------------------------------


# All the necessary imports needed for my program are written here:
import tkinter as tk
from tkinter import messagebox
import os
#--------------------------------------------------------------------------------------

# Below is were the first window is created that will great the user and briefly informs them of the purpose of this program.
# The first part is where the dimensions and other details about the window are set.
root = tk.Tk()
root.title("Welcome to Budget calculator")
root.geometry("380x330")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))
#-------------------------------------------------------------------------------------

# Making a introduction message that will introduce the user to the program.
intro_slide = root
intro_message1 = "Welcome! \n To budget calculator"
intro_msg = tk.Message(root, text=intro_message1, justify="center")
intro_msg.config(fg="Yellow", bg="Black", font=('times', 20, 'italic'))
intro_msg.pack()
#--------------------------------------------------------------------------------------

# This is the second label further explaining what the program does.
intro_message2 = "Here you can deposit or withdraw money and see your progress towards your goals, and insert your income and expenses and we will draw up a plan to solve your finance situation."
intro_msg2 = tk.Message(root, text=intro_message2)
intro_msg2.config(bg='white', relief="sunken", borderwidth=3, font=('times', 17))
intro_msg2.pack()
#--------------------------------------------------------------------------------------

# A label asking the user if they are done reading the introduction message and if they are ready to start.
intro_label = tk.Label(root, text="Are you ready to start?", font=("times", 15))
intro_label.pack()
#--------------------------------------------------------------------------------------

# Creating a frame for the first window.
frame = tk.Frame(root)
frame.pack()
#--------------------------------------------------------------------------------------

# This button is the exit button in case the user accidentally opened the program, once clicked the program will exit.
# This button sets the 'command' to 'quit' in order to quit once clicked.
intro_button1 = tk.Button(frame,
                  text="NO",
                  fg="red",
                  command=quit)
intro_button1.pack(side=tk.RIGHT)
#--------------------------------------------------------------------------------------

# Once the user has finished reading they can start the program by clicking on 'YES', this will run the (PageOpen) function - [line 3].
# This button sets the 'command' to 'PageOpen' witch means that when the user clicks on this button it will run the function PageOpen.
intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=PageOpen)  #-(line 3)
intro_button2.pack(side=tk.LEFT)
#--------------------------------------------------------------------------------------

root.mainloop()
