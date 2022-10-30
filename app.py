from tkinter import *
from tkinter import filedialog
import main as main
from tkinter import ttk

root = Tk()
root.title('Table Excractor')
root.geometry('510x300')

filename=""
def browse_button():
    global filename
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*'))

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print("FILENAAAAAAAAAME  : "+filename)

   
    
def ok_button(type,page):
    print("TYPE "+type)
    print("PAGE "+page)

    main.main(filename, page,type)


frame = LabelFrame(root)
frame.grid(row=10, column=3)

MODES = [("One table in the page", "1"), ("Multiple tables in the page", "2"), ]
type = StringVar()
type.set("1")
Type_file = ttk.Label(root,text = "Type").place(relx = 0.2,rely = 0.5) 
Page_Number = ttk.Label(root,text = "Page Number").place(relx = 0.2,rely = 0.3) 
File_name = ttk.Label(root,text = "File").place(relx = 0.2,rely = 0.1) 

c = 0
for text, mode in MODES:
    ttk.Radiobutton(root, text=text, variable=type,
                value=mode).place(relx = 0.4,rely = 0.5+c)
    c += 0.08

e = ttk.Entry(root, width=25)
e.place(relx=0.4, rely=0.3)

button1 = ttk.Button(root, text="Select a PDF file", width=25, command=browse_button)
button1.place(relx = 0.4,rely = 0.1)
button2 = ttk.Button(root, text="Extract", width=40, command=lambda: ok_button(type.get(),e.get()))
button2.place(relx = 0.2,rely = 0.8)

root.mainloop()
