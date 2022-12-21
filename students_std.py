from tkinter import *
import pandas as pd
from tkinter import ttk,messagebox

def main():
    root=Tk()
    obj=Student(root)
    root.mainloop()

class Student:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Management")
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(1000/2)
        y=(screen_height/2)-(500/2)
        self.root.geometry("1000x500+{}+{}".format(int(x),int(y)))
        self.root.resizable(False,False)

    #========frames====================
        self.frame1=Frame(self.root,bg="white")
        self.frame1.place(x=10,y=20,height=200,width=960)
        self.frame2=Frame(self.root,bg="white",relief=RIDGE)
        self.frame2.place(x=10,y=230,height=250,width=960) 

    #============Treeview==================
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",background="grey71",foreground="black",rowheight=25,fieldbackground="grey71")
        self.style.map("Treeview",background=[("selected","green")])
        student_headings=pd.read_csv("csv_files\students.csv")
        self.Student_Table=ttk.Treeview(self.frame2,columns=list(student_headings.columns),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        for i in self.Student_Table["columns"]:
                self.Student_Table.heading(i,text=i)

        self.Student_Table["show"]="headings"
        for i in self.Student_Table["columns"]:
                self.Student_Table.column(i,width=10)
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table["displaycolumns"]=list(student_headings.columns)
if __name__=="__main__":
    main()        