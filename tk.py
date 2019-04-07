from tkinter import *
def list_screen():
    root = Tk()
    root.title("UGS")
    root.geometry("800x640")
    label1 = Label(text="Лист задания", fg="#eee", bg="#333", font="Arial 14")
    label1.pack()
    list_job = "Поставить линию на самописце, \nПроверить циклы, \nПроверить пораметры T и RH, \nПроверить бумагу в самописцах"
    label2 = Label(text=list_job, justify=LEFT, font="Arial 14")
    label2.place(relx=.2, rely=.3)
    '''root.insert(END, "a list entry")
    with open('output.txt', 'r') as file:
        lst = file.readlines()
    for item in lst:
        root.insert(END, item)'''
    root.mainloop()
def loadme():
    f = open('output.txt.txt','r')
    line = f.readlines()
    print(line)
loadme()
