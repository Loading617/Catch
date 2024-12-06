import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Catch!")

label = tk.Label(root, text="Catch!", font=("Helvetica, 18"))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=("Helvetica, 14"))
textbox.pack()

root.mainloop()
