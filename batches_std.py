from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pandas as pd

def main():
    root=Tk()
    obj=Batches(root)
    root.mainloop()

class Batches:
    def __init__(self,root):
        self.root=root
        self.root.title("Batch Management")
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
        self.frame3=Frame(self.frame1,bg="white",relief=RIDGE)
        self.frame3.place(x=800,y=50) 

    #=======frame1_content============
        self.lbl_id=Label(self.frame1,text="Batch ID",bg="white",font=("times new roman",10,"bold")).grid(row=0,column=0)
        self.lbl_name=Label(self.frame1,text="Batch Name",bg="white",font=("times new roman",10,"bold")).grid(row=1,column=0)
        self.lbl_course_lst=Label(self.frame1,text="List of Courses",bg="white",font=("times new roman",10,"bold")).grid(row=2,column=0)
        
        self.combo_id=ttk.Combobox(self.frame1,font=("times new roman",15,"bold"),state="readonly",justify=RIGHT).grid(row=0,column=1,padx=2,pady=2)
        self.entry_name=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=1,column=1,padx=5,pady=5)
        self.listbox=Listbox(self.frame1,bg="azure3",highlightcolor="orange",width=33,height=5)
        self.listbox.grid(row=2,column=1)
        self.entry_course=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=3,column=1,padx=5,pady=5)
        
        self.btn1=Button(self.frame1,text="Add",justify=CENTER,command=None).grid(row=2,column=3,)
        self.btn2=Button(self.frame1,text="Delete",justify=CENTER,command=lambda: self.listbox.delete(ANCHOR)).grid(row=2,column=4,)
        self.text_std=Text(self.frame1,height=10,width=45,bg="yellow").place(x=400,y=10)
        
        self.btn_pie=Button(self.frame1,text="Plot Piechart",justify=CENTER).place(x=800,y=10)
        self.btn1_crud=Button(self.frame3,text="Add",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white").pack(side=TOP,)
        self.btn2_crud=Button(self.frame3,text="Update",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white").pack(side=LEFT)
        self.btn3_crud=Button(self.frame3,text="Delete",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white").pack(side=RIGHT)
        self.btn4_crud=Button(self.frame3,text="Clear",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white").pack(side=BOTTOM)

        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.search_entry=Entry(self.frame1,font=("times new roman",10,"bold"),bg="azure2").place(x=800,y=150)
        self.btn_search=Button(self.frame1,image=self.search_image,height=23,borderwidth=1,relief=GROOVE,bg="white")
        self.btn_search.place(x=880,y=170)
        self.show_allbtn = Button(self.frame1, text="Show All", width=10,height=0, pady=1, bg="OrangeRed3",font=("times new roman", 10, "bold")).place(x=800, y=170)
        
    #===========Content Under frame2
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",background="grey71",foreground="black",rowheight=25,fieldbackground="grey71")
        self.style.map("Treeview",background=[("selected","green")])

        self.Depart_Table=ttk.Treeview(self.frame2,columns=("Batch ID","Batch Name","Department Name","List of Courses","List of Students"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Depart_Table.xview)
        scroll_y.config(command=self.Depart_Table.yview)

        self.Depart_Table.heading("Batch ID",text="Department ID")
        self.Depart_Table.heading("Batch Name", text="Department Name")
        self.Depart_Table.heading("Department Name", text="List of Batches")
        self.Depart_Table.heading("List of Courses", text="List of Batches")
        self.Depart_Table.heading("List of Students", text="List of Batches")

        self.Depart_Table["show"]="headings"
        self.Depart_Table.column("Batch ID",width=10)
        self.Depart_Table.column("Batch Name", width=10)
        self.Depart_Table.column("Department Name", width=10)
        self.Depart_Table.column("List of Courses", width=10)
        self.Depart_Table.column("List of Students", width=10)

        self.Depart_Table.pack(fill=BOTH,expand=1)


        self.Depart_Table["displaycolumns"]=("Batch ID","Batch Name","Department Name","List of Courses","List of Students")
if __name__=="__main__":
    main()               