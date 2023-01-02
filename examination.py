from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pandas as pd
import ast,itertools
from pandas_tut import *


def main():
    root = Tk()
    obj = Exam(root)
    root.mainloop()


class Exam:
    def __init__(self, root):
        self.root = root
        self.root.title("Examinations Management")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2)-(1000/2)
        y = (screen_height/2)-(500/2)
        self.root.geometry("1000x500+{}+{}".format(int(x)+100, int(y)))
        self.root.resizable(False, False)

    # ===============frames============================
        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=10, y=20, height=200, width=960)
        self.frame2 = Frame(self.root, bg="white", relief=RIDGE)
        self.frame2.place(x=10, y=230, height=250, width=960)
    #==================StringVar
        self.combo_id_var=StringVar()
        self.course_id_combo_var=StringVar()
        self.entry_roll_var=StringVar()
        self.entry_marks_var=StringVar()
        self.txt_search=StringVar()
    # ============Content_under_frame1==================
        self.lbl_id = Label(self.frame1, text="Student ID", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=0, column=0)
        self.lbl_roll = Label(self.frame1, text="Class Roll Number", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=1, column=0)
        self.lbl_enter_marks=Label(self.frame1, text="1.Enter Course\n2.Enter Marks", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=2,column=0)

        self.combo_id = ttk.Combobox(self.frame1,textvariable=self.combo_id_var, font=(
            "times new roman", 15, "bold"), state="readonly", justify=RIGHT)
        self.combo_id.grid(row=0, column=1, padx=2, pady=2)
        self.entry_roll = Entry(self.frame1, font=(
            "times new roman", 15, "bold"),textvariable=self.entry_roll_var, bg="azure2", state="readonly").grid(row=1, column=1,padx=5,pady=5)
        self.course_id_combo=ttk.Combobox(self.frame1,textvariable=self.course_id_combo_var,font=("times new roman",10,"bold"),width=10,state="readonly",justify=RIGHT)
        self.course_id_combo.place(x=120,y=75)
        self.marks_entry=Entry(self.frame1, textvariable=self.entry_marks_var,validate="key", validatecommand=(root.register(self.validate), '%P'),font=("times new roman", 15, "bold"),width=10, bg="azure2").place(x=215,y=75)
        #===============Buttons-CRUD===================
        self.btn1_crud=Button(self.frame1,text="Add",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black",command=self.crud_add).place(x=20,y=150)
        self.btn2_crud=Button(self.frame1,text="Update",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black",command=self.update_crud).place(x=60,y=150)
        self.btn3_crud=Button(self.frame1,text="Delete",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black",command=self.crud_delete).place(x=120,y=150)
        self.btn4_crud=Button(self.frame1,text="Clear",font=("Comic Sans MS", 10, "bold"),activebackground="green",activeforeground="white",fg="black",command=self.clear_crud).place(x=175,y=150)

        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.reset_image= ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/reset_btn.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.search_entry=Entry(self.frame1,textvariable=self.txt_search,font=("times new roman",15,"bold"),bg="azure2").place(x=350,y=150)
        self.btn_search=Button(self.frame1,command=self.search_data,image=self.search_image,height=23,borderwidth=1,relief=GROOVE,bg="white")
        self.btn_search.place(x=550,y=150)
        self.reset_btn = Button(self.frame1, command=self.fetch_data,image=self.reset_image, height=23,borderwidth=1,relief=GROOVE).place(x=590, y=150)
        self.plot_scatter_btn=Button(self.frame1,command=lambda: create_scatter_plot(r"csv_files/exam.csv"),text="Plot Scatter Plot",font=("times new roman", 10, "bold"),justify=CENTER,bg="red",activebackground="yellow",activeforeground="blue").place(x=350,y=100)
    #======Treeview==============================
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",background="grey71",foreground="black",rowheight=25,fieldbackground="grey71")
        self.style.map("Treeview",background=[("selected","green")])
        self.exam_headings=pd.read_csv("csv_files\exam.csv")
        self.exams_Table=ttk.Treeview(self.frame2,columns=list(self.exam_headings.columns),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.exams_Table.xview)
        scroll_y.config(command=self.exams_Table.yview)

        for i in self.exams_Table["columns"]:
                self.exams_Table.heading(i,text=i)

        self.exams_Table["show"]="headings"
        for i in self.exams_Table["columns"]:
                self.exams_Table.column(i,width=10)
        self.exams_Table.pack(fill=BOTH,expand=1)
        self.exams_Table["displaycolumns"]=list(self.exam_headings.columns)  
        self.fetch_data()
        self.exams_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.bind("<Button-1>",self.update_student_ids)
        self.combo_id.bind("<<ComboboxSelected>>",self.get_course_contents)
        self.combo_id_var.trace("w",self.upd)

    #====================================================================
    def upd(self,*args):
        self.entry_roll_var.set("")
        self.entry_roll_var.set(self.combo_id_var.get()[-2:])
    def validate(self,P):
        if P.isdigit() or P=="":
            return True
        return False
    def update_student_ids(self,ev):
        df=pd.read_csv("csv_files\students.csv")
        content=df[df.columns[0]]
        batch_id=[]
        self.combo_id["values"]=content.to_numpy().tolist()
    def get_course_contents(self,ev):
        selection=self.combo_id_var.get()
        df=pd.read_csv("csv_files\Batches.csv")
        df_filtered=df.loc[df[df.columns[0]]==self.combo_id_var.get()[:-2]]
        df_rows=df_filtered.to_numpy().tolist()
        
        self.course_id_combo["values"]=ast.literal_eval(df_rows[0][3])
    def clear_crud(self):
        self.entry_marks_var.set("")
        self.combo_id_var.set("")
        self.course_id_combo.set("")
        self.entry_roll_var.set("")  
    def get_cursor(self,ev):
        cursor_row = self.exams_Table.focus()
        content = self.exams_Table.item(cursor_row)
        self.Entry_fill = content["values"]    
        self.course_id_combo_var.set(self.Entry_fill[0])
        self.combo_id_var.set(self.Entry_fill[1])
        self.entry_marks_var.set(self.Entry_fill[2])
    def update_crud(self):
        if self.entry_marks_var.get()=="" or self.combo_id_var.get()=="" or self.course_id_combo_var.get()=="":
            messagebox.showerror("Error","Entry bars should not be empty",parent=self.root)    
        else:
            try:
                excel_filename = r"csv_files/exam.csv"
                self.df = pd.read_csv(excel_filename)
                for i in self.df.index:

                    if (self.df.loc[i, self.exam_headings.columns[1]] == self.combo_id_var.get()):
                        print("Hello world")
                        self.df.loc[i, self.exam_headings.columns[2]
                                    ] = self.entry_marks_var.get()

                        self.df.to_csv(excel_filename, index=False)
                        self.clear_crud()
                        self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
    def search_data(self):
        if self.txt_search.get() == "":
            messagebox.showerror(
                "Error", "Entry box shouldn't be empty.", parent=self.root)
        else:
            try:    
                df_filtered = self.exam_headings.loc[self.exam_headings[self.exam_headings.columns[0]] == self.txt_search.get(
                )]

                df_rows = df_filtered.to_numpy().tolist()
                
                self.exams_Table.delete(*self.exams_Table.get_children())
                for i in df_rows:
                    self.exams_Table.insert(
                        "", END, values=(i[0], i[1], i[2]))
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
    def crud_delete(self):
        if self.entry_marks_var.get()=="" or self.combo_id_var.get()=="" or self.course_id_combo_var.get()=="":
            messagebox.showerror("Error","Entry bars should not be empty",parent=self.root)    
        else:
            try:
                excel_filename = r"csv_files/exam.csv"
                self.df = pd.read_csv(excel_filename)
                self.df.drop(self.df.index[(
                    self.df[self.exam_headings.columns[1]] == self.combo_id_var.get())], axis=0, inplace=True)

                self.df.to_csv(excel_filename, index=False)

                self.clear_crud()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
    def fetch_data(self):
        excel_filename = r"csv_files/exam.csv"
        if excel_filename:
            try:
                df = pd.read_csv(excel_filename)
                 
                df=df.drop_duplicates(subset=[self.exam_headings.columns[0],self.exam_headings.columns[1]])
                df.to_csv("csv_files\exam.csv",index=False)  
                df_2=   pd.read_csv(excel_filename)    

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
        self.exams_Table.delete(*self.exams_Table.get_children())

        df_rows = df_2.to_numpy().tolist()
        for row in df_rows:
            self.exams_Table.insert("", END, values=row)      
    def crud_add(self):
        if self.entry_marks_var.get()=="" or self.combo_id_var.get()=="" or self.course_id_combo_var.get()=="":
            messagebox.showerror("Error","Entry bars should not be empty",parent=self.root)    
        else:
            try:
                #print(self.entry_marks_var.get(),type(self.entry_marks_var.get()))
                if int(self.entry_marks_var.get())>100:
                    messagebox.showinfo("Info","Marks Obtained should be less than or equal to 100",parent=self.root)
                else:
                    df = pd.read_csv("csv_files\exam.csv")
                    data={self.exam_headings.columns[0]: [self.course_id_combo_var.get()], self.exam_headings.columns[1]: [
                            self.combo_id_var.get()], self.exam_headings.columns[2]: [self.entry_marks_var.get()]}
                    self.df = pd.DataFrame(data)
                    self.df.to_csv("csv_files\exam.csv", mode='a',
                                    index=False, header=False)
                        
                        
                    self.clear_crud()  
                    self.fetch_data()      
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)    
       
        
if __name__ == "__main__":
    main()
