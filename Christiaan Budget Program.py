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

   def clear_widget(event):
        # will clear out any entry boxes defined below when the user shifts
        # focus to the widgets defined below
        if username_box == Slide2.focus_get() and username_box.get() == 'Enter Username':
            username_box.delete(0, "end")
        elif password_box == password_box.focus_get() and password_box.get() == '     ':
            password_box.delete(0, "end")

   def repopulate_defaults(event):
        # will repopulate the default text previously inside the entry boxes defined below if
        # the user does not put anything in while focused and changes focus to another widget
        if username_box != Slide2.focus_get() and username_box.get() == '':
            username_box.insert(0, 'Enter Username')
        elif password_box != Slide2.focus_get() and password_box.get() == '':
            password_box.insert(0, '     ')

   def login(*event):
        # Able to be called from a key binding or a button click because of the '*event'
        print('Username: ' + username_box.get())
        print('Password: ' + password_box.get())
        Slide2.destroy()
        # If I wanted I could also pass the username and password I got above to another
        # function from here.




    # defines a grid 50 x 50 cells in the main window
   rows = 0
   while rows < 10:
        Slide2.rowconfigure(rows, weight=1)
        Slide2.columnconfigure(rows, weight=1)
        rows += 1

   # adds username entry widget and defines its properties
   username_box = tk.Entry(Slide2)
   username_box.insert(0, 'Enter Username')
   username_box.bind("<FocusIn>", clear_widget)
   username_box.bind('<FocusOut>', repopulate_defaults)
   username_box.grid(row=1, column=5, sticky='NS')


    # adds password entry widget and defines its properties
   password_box = tk.Entry(Slide2, show='*')
   password_box.insert(0, '     ')
   password_box.bind("<FocusIn>", clear_widget)
   password_box.bind('<FocusOut>', repopulate_defaults)
   password_box.bind('<Return>', login)
   password_box.grid(row=2, column=5, sticky='NS')


    # adds login button and defines its properties
   login_btn = tk.Button(Slide2, text='Login', command=login)
   login_btn.bind('<Return>', login)
   login_btn.grid(row=5, column=5, sticky='NESW')




#part 1, close button, intro slide
intro_button2 = tk.Button(frame,
                         text="YES",
                         fg="green",
                         command=createNewWindow)

intro_button2.pack(side=tk.LEFT)

root.mainloop()

#fgjhdfjkghdfjkg
