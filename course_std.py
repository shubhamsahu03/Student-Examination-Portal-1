from tkinter import *
import pandas as pd
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

def main():
    root=Tk()
    obj=Course(root)
    root.mainloop()
class Course:
        def __init__(self,root):

            self.root=root
            self.root.title("Course Management")
            screen_width=self.root.winfo_screenwidth()
            screen_height=self.root.winfo_screenheight()
            x=(screen_width/2)-(1000/2)
            y=(screen_height/2)-(500/2)
            self.root.geometry("1000x500+{}+{}".format(int(x),int(y)))
            self.root.resizable(False,False)   

            self.frame1=Frame(self.root,bg="white")
            self.frame1.place(x=10,y=20,height=200,width=960)
            self.frame2=Frame(self.root,bg="white",relief=RIDGE)
            self.frame2.place(x=10,y=230,height=250,width=960) 

        #==========Content Under frame1=====================
            self.lbl_id=Label(self.frame1,text="Course ID",bg="white",font=("times new roman",10,"bold")).grid(row=0,column=0)
            self.lbl_name=Label(self.frame1,text="Course Name",bg="white",font=("times new roman",10,"bold")).grid(row=1,column=0)
            self.lbl_marks_obtained=Label(self.frame1,text="Marks Obtained",bg="white",font=("times new roman",10,"bold")).grid(row=2,column=0)
            self.combo_id=ttk.Combobox(self.frame1,font=("times new roman",15,"bold"),state="readonly",justify=RIGHT).grid(row=0,column=1,padx=2,pady=2)
            self.entry_name=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=1,column=1,padx=5,pady=5)
            self.combo_std_id=ttk.Combobox(self.frame1,font=("times new roman",10,"bold"),width=10,state="readonly",justify=RIGHT).place(x=100,y=75)
            self.lbl_roll=Label(self.frame1,text="Roll",bg="white",font=("times new roman",10,"bold"),borderwidth=1, relief="solid").place(x=200,y=75)
            self.lbl_marks=Label(self.frame1,text="Marks",bg="white",font=("times new roman",10,"bold"),borderwidth=1, relief="solid").place(x=230,y=75)

        #    self.entry_course=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=3,column=1,padx=5,pady=5)
        #===Buttons==========
            self.btn1_crud=Button(self.frame1,text="Add",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black").place(x=20,y=150)
            self.btn2_crud=Button(self.frame1,text="Update",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black").place(x=60,y=150)
            self.btn3_crud=Button(self.frame1,text="Delete",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black").place(x=120,y=150)
            self.btn4_crud=Button(self.frame1,text="Clear",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black").place(x=175,y=150)

            self.search_image = ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
            self.search_entry=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").place(x=350,y=150)
            self.btn_search=Button(self.frame1,image=self.search_image,height=23,borderwidth=1,relief=GROOVE,bg="white")
            self.btn_search.place(x=550,y=150)
            self.show_allbtn = Button(self.frame1, text="Show All", width=10,height=0, pady=1, bg="OrangeRed3",font=("times new roman", 10, "bold")).place(x=590, y=150)
            self.histo_btn=Button(self.frame1,text="Histogram",justify=CENTER).place(x=350,y=100)

        #===========Content Under frame2====================
            scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
            self.style=ttk.Style()
            self.style.theme_use("clam")
            self.style.configure("Treeview",background="grey71",foreground="black",rowheight=25,fieldbackground="grey71")
            self.style.map("Treeview",background=[("selected","green")])
            course_headings=pd.read_csv("csv_files\courses.csv")
            self.Course_Table=ttk.Treeview(self.frame2,columns=list(course_headings.columns),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Course_Table.xview)
            scroll_y.config(command=self.Course_Table.yview)

            for i in self.Course_Table["columns"]:
                self.Course_Table.heading(i,text=i)

            self.Course_Table["show"]="headings"
            for i in self.Course_Table["columns"]:
                self.Course_Table.column(i,width=10)
            self.Course_Table.pack(fill=BOTH,expand=1)
            self.Course_Table["displaycolumns"]=list(course_headings.columns)  

if __name__=="__main__":
    main()    