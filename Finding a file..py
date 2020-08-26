def write_File (name):
            filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Open file",
                                                  filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            try:
                if filename:
                    the_file = open(filename)
                    textArea.insert(tk.END, the_file.read())
                    the_file.close()
                elif filename == '':
                    messagebox.showinfo("Cancel", "You clicked cancel")
            except IOError:
                messagebox.showinfo("Error", "Couyld not open file")
