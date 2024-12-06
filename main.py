import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Catch!")

label = tk.Label(root, text="Catch!", font=("Helvetica, 18"))
label.pack()

root.mainloop()
