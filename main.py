import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Catch!")

label = tk.Label(root, text="Catch!", font=("Helvetica, 18"))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=4, font=("Helvetica, 14"))
textbox.pack()

myentry = tk.Entry(root)
myentry.pack()

root.mainloop()
