
#test_string = input("Type document: ") 
#print ("The original string is : " +  test_string) 
#res = len(test_string.split()) 
#print ("The number of words in string are : " +  str(res))


import tkinter

root= tkinter.Tk()
root.title("WordCount")
canvas1 = tkinter.Canvas(root, width = 400, height = 300)
canvas1.configure(background = 'black')
canvas1.pack()

entry1 = tkinter.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

label2 = tkinter.Label(root, text='Type your Document:', fg= 'blue')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

def word_count ():  
    x1 = entry1.get()
    res = len(x1.split()) 
    label3 = tkinter.Label(root, text='The number of words in string are :', fg= 'blue')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tkinter.Label(root, text= str(len(x1.split())), fg= 'blue')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(200, 230, window=label4)
    

    
    
btn1 = tkinter.Button(root, text='Calculate', command=word_count, bg='brown')

btn1.pack()

root.mainloop()
