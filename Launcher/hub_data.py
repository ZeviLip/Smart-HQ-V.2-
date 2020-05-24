#Functions for each website (New:2) is new tab, (url) = webaddress
    


#Tkinter module that creates window configured to the center of users screen
import tkinter

root= tkinter.Tk()

canvas1 = tkinter.Canvas(root, width = 400, height = 300)
canvas1.configure(background = 'orange')
root.title("TheHub")

canvas1.pack()

entry1 = tkinter.Entry (root) 
canvas1.create_window(200, 120, window=entry1)

label2 = tkinter.Label(root, text='Type Domain Name:', fg= 'blue')
label2.config(font=('helvetica', 15))
canvas1.create_window(200, 90, window=label2)

entry2 = tkinter.Entry (root) 
canvas1.create_window(200, 140, window=entry2)

label3 = tkinter.Label(root, text='Type Extension e.g. (.com, .gov):', fg= 'blue')
label3.config(font=('helvetica', 15))
canvas1.create_window(200, 170, window=label3)


def comm ():
    x1 = entry1.get()
    x2 = entry2.get()
    import webbrowser
    new=2;
    url = "https://" + entry1.get() + entry2.get()
    webbrowser.open(url, new=new);
    x1.delete(0, tkinter.END)
    x2.delete(0, tkinter.END)
def hulu():
    x1 = entry1.get()
    btn1 = tkinter.Button(root, text= x1, highlightbackground='orange', highlightthickness=5, command=comm)
    btn1.pack()
btn = tkinter.Button(root, text= 'create', highlightbackground='orange', highlightthickness=5, command=hulu)
btn.pack()
def quit():
    root.destroy()
    import Launcher
        
btnquit = tkinter.Button(root, text= 'quit', highlightbackground='red', highlightthickness=5, command=quit)
btnquit.pack()

root.mainloop()
