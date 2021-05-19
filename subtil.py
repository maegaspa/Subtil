from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox


def pdf2img():
    try:
        images = convert_from_path(str(e1.get()))
        for img in images:
            img.save('output.jpg', 'JPEG')

    except  :
        Result = "NO pdf found"
        messagebox.showinfo("Result", Result)

    else:
        Result = "success"
        messagebox.showinfo("Result", Result)



master = Tk()
master.title("Subtil")
master.geometry("500x50")
Label(master, text="File Location").grid(row=2, sticky=W)

e1 = Entry(master)
e1.grid(row=2, column=1, ipadx=50)

b = Button(master, text="Convert", command=pdf2img)
b.grid(row=2, column=2,columnspan=2, rowspan=2,padx=5, pady=5)

mainloop()