from tkinter import *
root=Tk()
def Quit():
    pass
root.protocol("WM_DELETE_WINDOW", Quit)
root.title('ПОМИЛКА 1000-7')
root.geometry('520x100')
root.resizable(width=False, height=False)
title = Label(text='ПОМИЛКА, закрийте вікно для закриття помилки(якщо зможете)', font=40, bg='red')
title.pack()
root.mainloop()









