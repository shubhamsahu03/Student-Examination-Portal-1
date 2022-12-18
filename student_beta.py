from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pandas as pd



def main():
    root = Tk()

    obj = Student(root)
    root.mainloop()
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management")
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(1000/2)
        y=(screen_height/2)-(500/2)
        self.root.geometry("1000x500+{}+{}".format(int(x),int(y)))
        self.root.resizable(False,False)
        #====Menu===========
        
        self.mymenu=Menu(self.root)
        self.mymenu.add_command(label="Student")
        self.mymenu.add_command(label="Course")
        self.mymenu.add_command(label="Batch")
        self.mymenu.add_command(label="Department")
        self.mymenu.add_command(label="Examinations")

        self.root.config(menu=self.mymenu)
        scrollbar=Scrollbar(self.root,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)

   
        #========Frame1======
        self.frame1=Frame(self.root,bg="white")
        self.frame1.place(x=10,y=20,height=200,width=600)

        #====Frame2==========
        self.frame2=Frame(self.root,bg="white")
        self.frame2.place(x=620,y=20,height=200,width=350)
        #Frame3=================
        self.frame3=Frame(self.root,bg="white",relief=RIDGE)
        self.frame3.place(x=10,y=230,height=250,width=960)

        #Frame1 content======
        self.depart_id=Label(self.frame1,text="Department ID",font=("times new roman",10,"bold"),bg="white").grid(row=0,column=0,pady=5,padx=5)
        self.depart_name=Label(self.frame1,text="Department Name",font=("times new roman",10,"bold"),bg="white").grid(row=1,column=0,padx=5,pady=5)
        self.batches_under=Label(self.frame1,text="List Of Batches",font=("times new roman",10,"bold"),bg="white").grid(row=2,column=0,padx=5,pady=5)
        #self.scrollbar=Scrollbar(self.frame1,orient=VERTICAL)
        #=====All variables==========
        self.depart_id_txt_var=StringVar()
        self.depart_name_txt_var=StringVar()
        self.batches_add_txt_var=StringVar()
        self.avg_batchesvar=StringVar()
        self.txt_search=StringVar()

        
        
        self.my_list=[]
        self.depart_id_txt=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=0,column=1,padx=5,pady=5)
        self.depart_name_txt=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=1,column=1,padx=5,pady=5)
        self.batches_add_txt=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2",textvariable=self.batches_add_txt_var).place(x=120,y=165)
        
        self.listbox=Listbox(self.root,bg="azure3",highlightcolor="orange",width=33,height=5)
        self.listbox.place(x=129,y=100)
        #self.scrollbar.config(command=self.listbox.yview)
       # self.scrollbar.grid(row=5 ,column=3)
    
        
        #buttons under frame1====================
        self.btn1=Button(self.frame1,text="Add",justify=CENTER,command=self.batches_add).grid(row=2,column=3,)
        self.btn2=Button(self.frame1,text="Delete",justify=CENTER,command=lambda: self.listbox.delete(ANCHOR)).grid(row=2,column=4,)
        self.btn1_crud=Button(self.frame1,text="Add",justify=CENTER,font=("Comic Sans MS", 10, "bold")).place(x=408,y=165)
        self.btn2_crud=Button(self.frame1,text="Update",justify=CENTER,font=("Comic Sans MS", 10, "bold")).place(x=445,y=165)
        self.btn3_crud=Button(self.frame1,text="Delete",justify=CENTER,font=("Comic Sans MS", 10, "bold")).place(x=503,y=165)
        self.btn4_crud=Button(self.frame1,text="Clear",justify=CENTER,font=("Comic Sans MS", 10, "bold")).place(x=555,y=165)

    #===Content under frame2======================
        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))


        self.average_batches=Label(self.frame2,textvariable=self.avg_batchesvar,background="white",font=("times new roman",10,"bold"),text="hello").grid(row=1,column=1,columnspan=2)
        self.avg_batchesvar.set("Average Performance of Batches: {}".format(str(69)+"%"))
        self.plot_graph_btn=Button(self.frame2,text="Plot Graph",activeforeground="green").grid(row=2,column=2,ipadx=20,pady=20,padx=10)
        self.entry_search=Entry(self.frame2,textvariable=self.txt_search,relief=GROOVE,bg="white",borderwidth=1,font=("times new roman",17,"bold"),bd=3).grid(row=3 ,column=2)
        self.btn_search=Button(self.frame2,image=self.search_image,borderwidth=1,relief=GROOVE,bg="white")
        self.btn_search.place(x=0,y=125)
        self.show_allbtn = Button(self.frame2, text="Show All", width=10,height=2, pady=3, bg="OrangeRed3",font=("times new roman", 10, "bold")).place(x=50, y=125)
    #==================Treeview=============================
        scroll_x=ttk.Scrollbar(self.frame3,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame3, orient=VERTICAL)
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",background="grey71",foreground="black",rowheight=25,fieldbackground="grey71")
        self.style.map("Treeview",background=[("selected","green")])
        self.Depart_Table=ttk.Treeview(self.frame3,columns=("Department ID","Department Name","List of Batches"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Depart_Table.xview)
        scroll_y.config(command=self.Depart_Table.yview)

        self.Depart_Table.heading("Department ID",text="Department ID")
        self.Depart_Table.heading("Department Name", text="Department Name")
        self.Depart_Table.heading("List of Batches", text="List of Batches")

        self.Depart_Table["show"]="headings"
        self.Depart_Table.column("Department ID",width=10)
        self.Depart_Table.column("Department Name", width=10)
        self.Depart_Table.column("List of Batches", width=10)
        self.Depart_Table.pack(fill=BOTH,expand=1)


        self.Depart_Table["displaycolumns"]=("Department ID","Department Name","List of Batches")
    def batches_add(self):
        if self.batches_add_txt_var.get() not in self.my_list:
            self.my_list.append(self.batches_add_txt_var.get())
            self.listbox.insert(END,self.batches_add_txt_var.get())
            self.batches_add_txt_var.set("")
        else:
            self.batches_add_txt_var.set("")
    
    def crud_add(self):
        if self.depart_name_txt_var.get()=="" or self.depart_id_txt_var.get()=="" or self.my_list==[]:
            messagebox.showerror("Error","Entry bars should not be empty",parent=self.root)
        else:
            try:
                excel_filename=r"department.csv"
                if excel_filename[-4:]==".csv":
                    self.df=pd.read_csv(excel_filename)
                else:
                    self.df = pd.read_excel(excel_filename)
                data={self.df[0]:[self.depart_id_txt_var.get()],self.df[1]:[self.depart_name_txt_var.get()],self.df[2]:[self.my_list]}
                
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}",parent=self.root)        



    #def print_(self):
     #   print("Random stuff about MJ")


if __name__=="__main__":
    main()    


