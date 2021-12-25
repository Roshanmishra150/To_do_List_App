from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class to_do:
    def __init__(self,root):
        self.root = root
        self.root.minsize(600,500)
        self.root.maxsize(600,500)
        self.root.title("To_Do_List")

        self.Lable1=Label(self.root,text=" To_Do_List_App ",font="arial,25,bold",bg="skyblue",fg="black",width=10,bd=3)
        self.Lable1.pack(side="top",fill=BOTH)

        self.Lable2=Label(self.root,text=" Task Functions ",bg="green",width=15,fg="white",font="arial,25,bold")
        self.Lable2.place(x=50,y=60)

        self.Lable3=Label(root,text=" Tasks ",bg="green",width=15,fg="white",font="arial,25,bold")
        self.Lable3.place(x=330,y=60)

        self.main_text = Listbox(self.root,height=13,bd=5,width=27,font="arial,1")
        self.Label_text=Label(root,text="To delete single item select and press delete button",width=39,height=2,font="arial 10",fg="red")
        self.Label_text.place(x=250,y=110)
        self.main_text.place(x=270,y=150)

        self.text = Entry(self.root,font=('arial',11,'italic bold'),bd=4,width=20,justify=LEFT)
        self.text.insert(0,"Enter text")
        self.text.configure(state=DISABLED)
        self.text.place(x=50,y=130)

        self.btn1 = Button(self.root,text=" Add ",width=15,height=0,bg="green",fg="white",font="arial,20,bold",command=lambda:add())
        self.btn1.place(x=50,y=200)

        self.btn2 = Button(self.root,text=" Delete ",width=15,height=0,bg="green",fg="white",font="arial,20,bold",command=lambda:deletes())
        self.btn2.place(x=50,y=280)
        
        self.btn2 = Button(self.root,text=" Delete All ",width=15,height=0,bg="green",fg="white",font="arial,20,bold",command=lambda:delete_all())
        self.btn2.place(x=50,y=360)

        def add():
            task = self.text.get()
            if task != "":
                self.main_text.insert(END, task)
                self.text.delete(0, "end")
            else:
                messagebox.showwarning("warning","please insert something ")

        def deletes():
            self.main_text.delete(ANCHOR)

        def delete_all():
            self.main_text.delete(0,END)

        def screen(event):
            self.text.configure(state=NORMAL)
            self.text.delete(0,END)
            self.text.unbind('<Button-1>',on_click)
        on_click = self.text.bind('<Button-1>',screen)

root = Tk()
ui = to_do(root)

root.mainloop()