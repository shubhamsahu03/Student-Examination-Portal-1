from tkinter import *
from tkinter import ttk,messagebox



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
        self.frame3=Frame(self.root,bg="white")
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

    def batches_add(self):
        if self.batches_add_txt_var.get() not in self.my_list:
            self.my_list.append(self.batches_add_txt_var.get())
            self.listbox.insert(END,self.batches_add_txt_var.get())
            self.batches_add_txt_var.set("")
        else:
            self.batches_add_txt_var.set("")
    



    #def print_(self):
     #   print("Random stuff about MJ")


if __name__=="__main__":
    main()    


