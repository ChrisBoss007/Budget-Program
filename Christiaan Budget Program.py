import tkinter as tk
#A comment
#Another comment
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



def createNewWindow():
   intro_slide.destroy()
   Slide2 = tk.Tk()
   Slide2.title("Budget calculator")
   Slide2.geometry("480x380")
   windowWidth = Slide2.winfo_reqwidth()
   windowHeight = Slide2.winfo_reqheight()
   positionRight = int(Slide2.winfo_screenwidth() / 2 - windowWidth / 2)
   positionDown = int(Slide2.winfo_screenheight() / 2 - windowHeight / 2)
   Slide2.geometry("+{}+{}".format(positionRight, positionDown))

   slide2_label1 = tk.Label(Slide2, text="Okay lets start off with some basic questions", font=("times", 15))
   slide2_label1.pack()
   slide2_label1.place(x=0, y=0)



   ##Part 3 last slide.

   def submit():
       Slide2.destroy()
       Slide3 = tk.Tk()
       Slide3.title("Budject calculator")
       Slide3.geometry("480x380")
       windowWidth = Slide3.winfo_reqwidth()
       windowHeight = Slide3.winfo_reqheight()
       positionRight = int(Slide3.winfo_screenwidth() / 2 - windowWidth / 2)
       positionDown = int(Slide3.winfo_screenheight() / 2 - windowHeight / 2)
       Slide3.geometry("+{}+{}".format(positionRight, positionDown))

       intro_message3 = "Here you can deposit or withdraw money and see your progress towards your goals, you can insert your income and expenses and we will draw up a plan to solve your finance situation."
       intro_msg3 = tk.Message(Slide3, text = intro_message3)
       intro_msg3.config(bg='white', relief="sunken", width=480, borderwidth = 3, font=('times', 13))
       intro_msg3.place(x=2, y=7)


       class App(object):
           def new_row(self):
               # Create widgets
               new_entry = tk.Entry(Slide3, width=15)
               name = new_entry.insert(0, "Name of income")

               print(name)


               new_entry2 = tk.Entry(Slide3, width=8)
               new_entry2.insert(0, "Amount")

               rate = OptionList = [
                "Hourly",
                "Daily",
                "Weekly",
                "Monthly"
                ]
               variable = tk.StringVar(Slide3)
               variable.set(OptionList[0])

               opt = tk.OptionMenu(Slide3, variable, *OptionList)
               opt.config(width=5, font=('Helvetica', 6))

               print(rate)

               #Get it to save the value that the user inserted for thier rate of payment







               # Put widgets in grid
               self.num_rows += 1
               self.num_rows2 += 1
               self.num_rows3 += 1

               opt.grid(column=4, row=self.num_rows3)
               opt.bind("<Button-1>")


               new_entry.grid(column=0, row=self.num_rows)
               def some_callback(event):
                   new_entry.delete(0, "end")
                   return None
               new_entry.bind("<Button-1>", some_callback)

               new_entry2.grid(column=2, row=self.num_rows2)
               def some_callback(event):
                   new_entry2.delete(0, "end")
                   return None
               new_entry2.bind("<Button-1>", some_callback)



           def __init__(self):
               self.num_rows = 1
               self.num_rows2 = 1
               self.num_rows3 = 1
               createRow_button = tk.Button(
                      Slide3, text='New Row', command=self.new_row)
               createRow_button.place(x=10, y=120)

               print()

       app = App()


   Label_name = tk.Label(Slide2, text="Name:", font=("times", 11))
   Label_name.pack()
   Label_name.place(x=12, y=27)

   entry_name = tk.Entry(Slide2)
   entry_name.insert(0, "Type your text here")
   entry_name.pack()
   entry_name.place(x=80, y=30)

   def some_callback(event):
       entry_name.delete(0, "end")
       return None

   entry_name.bind("<Button-1>", some_callback)

   Label_surname = tk.Label(Slide2, text="Surname:", font=("times", 11))
   Label_surname.pack()
   Label_surname.place(x=12, y=50)

   entry_Surname = tk.Entry(Slide2)
   entry_Surname.insert(0, "Type your text here")
   entry_Surname.pack()
   entry_Surname.place(x=80, y=51)

   slide2_button1 = tk.Button(Slide2,
                             text="Submit",
                             fg="green",
                             command=submit)
   slide2_button1.pack()
   slide2_button1.place(x=230, y=100)

   def some_callback(event):
       entry_Surname.delete(0, "end")
       return None

   entry_Surname.bind("<Button-1>", some_callback)

   Label_age = tk.Label(Slide2, text="Age:", font=("times", 11))
   Label_age.pack()
   Label_age.place(x=12, y=87)

   scale_age = tk.Scale(Slide2, from_=0, to=200, orient=tk.HORIZONTAL)
   scale_age.pack()
   scale_age.place(x=77, y=69)

   Label_gender = tk.Label(Slide2, text="Gender:", font=("times", 11))
   Label_gender.pack()
   Label_gender.place(x=205, y=28)

   check_gender = tk.Checkbutton(Slide2, text="Male")
   check_gender2 = tk.Checkbutton(Slide2, text="Female")
   check_gender3 = tk.Checkbutton(Slide2, text="Other")

   check_gender.pack()
   check_gender.place(x=260, y=27)

   check_gender2.pack()
   check_gender2.place(x=260, y=48)

   check_gender3.pack()
   check_gender3.place(x=260, y=70)





   ##Part 2 of the second slide
   Label_job = tk.Label(Slide2, text="1. Do you have a Job?", font=("times", 14))
   Label_job.pack()
   Label_job.place(x=30, y=120)

   radioValue = tk.IntVar()
   radiobutton_widget1 = tk.Radiobutton(Slide2,
                                             text="Yes",
                                             variable=radioValue, value=1,
                                             indicatoron=False)

   radiobutton_widget2 = tk.Radiobutton(Slide2,
                                             text="No",
                                             variable=radioValue, value=2,
                                             indicatoron=False)
   radiobutton_widget1.place(x=90, y=150)
   radiobutton_widget2.place(x=117, y=150)

   Label_job2 = tk.Label(Slide2, text="1. Do you have a Degree?", font=("times", 14))
   Label_job2.pack()
   Label_job2.place(x=30, y=179)

   radioValue = tk.IntVar()
   radiobutton_widget3 = tk.Radiobutton(Slide2,
                                             text="Yes",
                                             variable=radioValue, value=1,
                                             indicatoron=False)

   radiobutton_widget4 = tk.Radiobutton(Slide2,
                                             text="No",
                                             variable=radioValue, value=2,
                                             indicatoron=False)
   radiobutton_widget3.place(x=90, y=210)
   radiobutton_widget4.place(x=117, y=210)

   Label_job2 = tk.Label(Slide2, textvariable=radioValue)
   Label_job2.pack()
   Label_job2.place(x=63, y=1165)

   Label_job2 = tk.Label(Slide2, textvariable=radioValue)
   Label_job2.pack()
   Label_job2.place(x=63, y=1165)




#part 1, close button, intro slide
intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=createNewWindow)

intro_button2.pack(side=tk.LEFT)

def clear_widget(event):

    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if username_box == root.focus_get() and username_box.get() == 'Enter Username':
        username_box.delete(0, END)
    elif password_box == password_box.focus_get() and password_box.get() == '     ':
        password_box.delete(0, END)

def repopulate_defaults(event):

    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if username_box != root.focus_get() and username_box.get() == '':
        username_box.insert(0, 'Enter Username')
    elif password_box != root.focus_get() and password_box.get() == '':
        password_box.insert(0, '     ')

def login(*event):

    # Able to be called from a key binding or a button click because of the '*event'
    print('Username: ' + username_box.get())
    print('Password: ' + password_box.get())
    root.destroy()
    # If I wanted I could also pass the username and password I got above to another
    # function from here.


# defines a grid 50 x 50 cells in the main window
rows = 0
while rows < 10:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1


# adds username entry widget and defines its properties
username_box = tk.Entry(root)
username_box.insert(0, 'Enter Username')
username_box.bind("<FocusIn>", clear_widget)
username_box.bind('<FocusOut>', repopulate_defaults)
username_box.grid(row=1, column=5, sticky='NS')


# adds password entry widget and defines its properties
password_box = tk.Entry(root, show='*')
password_box.insert(0, '     ')
password_box.bind("<FocusIn>", clear_widget)
password_box.bind('<FocusOut>', repopulate_defaults)
password_box.bind('<Return>', login)
password_box.grid(row=2, column=5, sticky='NS')


# adds login button and defines its properties
login_btn = tk.Button(root, text='Login', command=login)
login_btn.bind('<Return>', login)
login_btn.grid(row=5, column=5, sticky='NESW')

root.mainloop()


