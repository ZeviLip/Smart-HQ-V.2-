#!/usr/local/bin/python3
import tkinter
#This creates seperate window to open in middle of users screen
window1 = tkinter.Tk()
window1.title("Smart HQ")
window1.configure(background = '#88324f')
window1.iconbitmap('c:/Documents/Launcher/Icon.icon')
window1.geometry("245x150+650+350")
#Applications functions
def quickzoom():
    import data_QZ
    return()
def hub():
    import hub_data
    return()
def wordcount():
    import WordCount_data
    return()
def search():
    import SearchEngine_data
#This creates the buttons which command all the functions above (added to them are style configurations)

btn0 = tkinter.Button(window1, fg = 'black', text="Hi, Welcome to Smart HQ!", font = ('Verdana', 15, 'bold'), borderwidth = '20', highlightbackground='#88324f', highlightthickness=5).grid(row = 0, column = 1, padx = 5)
btn1 = tkinter.Button(window1, fg = 'blue', text="QuickZoom", font = ('Arial', 13, 'bold'), command=quickzoom, highlightbackground='blue', highlightthickness=5).grid(row = 1, column = 1, padx = 10)
btn2 = tkinter.Button(window1, fg = '#88324f', text="TheHub", font = ('Arial', 13, 'bold'), command=hub, highlightbackground='black', highlightthickness=5).grid(row = 2, column = 1, padx = 10)
btn3 = tkinter.Button(window1, fg = 'red', text="WordCount", font = ('Arial', 13, 'bold'), command=wordcount, highlightbackground='orange', highlightthickness=5).grid(row = 3, column = 1, padx = 10)
btn4 = tkinter.Button(window1, fg = 'green', text="SearchEngine", font = ('Arial', 13, 'bold'), command=search, highlightbackground='grey', highlightthickness=5).grid(row = 4, column = 1, padx = 10)
#This runs the window progrom
window1.mainloop()



