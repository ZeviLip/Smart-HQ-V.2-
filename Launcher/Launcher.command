#!/usr/bin/env python
import tkinter

window1 = tkinter.Tk()
window1.title("Smart HQ")
window1.configure(background = '#88324f')
window1.wm_iconbitmap('Icon.ico')
window1.geometry("230x150+650+350")

def callback():
    for i in range(1000):
        import data_QZ
    return()
def hub():
    e = 'mc'
    import hub_data
    return()
def wordcount():
    import WordCount_data
    return()
def search():
    import SearchEngine_data
#highlightbackground=color
btn0 = tkinter.Button(window1, fg = 'black', text="Hi, Welcome to Smart HQ!", font = ('Verdana', 15), borderwidth = '8', highlightbackground='#88324f', highlightthickness=5).grid(row = 0, column = 1, padx = 5)
btn1 = tkinter.Button(window1, fg = 'blue', text="QuickZoom", font = ('Arial', 13), command=callback, highlightbackground='blue', highlightthickness=5).grid(row = 1, column = 1, padx = 10)
btn2 = tkinter.Button(window1, fg = '#88324f', text="TheHub", font = ('Arial', 13), command=hub, highlightbackground='black', highlightthickness=5).grid(row = 2, column = 1, padx = 10)
btn3 = tkinter.Button(window1, fg = 'red', text="WordCount", font = ('Arial', 13), command=wordcount, highlightbackground='orange', highlightthickness=5).grid(row = 3, column = 1, padx = 10)
btn4 = tkinter.Button(window1, fg = 'green', text="SearchEngine", font = ('Arial', 13), command=search, highlightbackground='grey', highlightthickness=5).grid(row = 4, column = 1, padx = 10)


window1.mainloop()

