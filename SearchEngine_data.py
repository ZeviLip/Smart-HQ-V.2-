#!/usr/local/bin/ python3
import tkinter

root= tkinter.Tk()

canvas1 = tkinter.Canvas(root, width = 400, height = 300)
canvas1.configure(background = 'green')

canvas1.pack()

entry1 = tkinter.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
def search ():  
    x1 = entry1.get()
    import webbrowser
    new=2;
    url = "https://" + x1
    webbrowser.open(url, new=new);
    
    
btn1 = tkinter.Button(root, text='search', command=search, bg='brown')
btn1.pack()


root.mainloop()
