from tkinter import *
import pandas as pd
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import ast
import itertools
from pandas_tut import *


def main():
    root = Tk()
    obj = Course(root)
    root.mainloop()


class Course:
    def __init__(self, root):

        self.root = root
        self.root.title("Course Management")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2)-(1000/2)
        y = (screen_height/2)-(500/2)
        self.root.geometry("1000x500+{}+{}".format(int(x)+100, int(y)))
        self.root.resizable(False, False)

        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=10, y=20, height=200, width=960)
        self.frame2 = Frame(self.root, bg="white", relief=RIDGE)
        self.frame2.place(x=10, y=230, height=250, width=960)
    # =======================StringVar=======================
        self.lbl_roll_var = StringVar()
        self.lbl_marks_var = StringVar()
        self.entry_name_var = StringVar()
        self.search_entry_var = StringVar()
        self.combo_id_var = StringVar()
        self.combo_std_id_var = StringVar()

    # ==========Content Under frame1=====================
        self.lbl_id = Label(self.frame1, text="Course ID", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=0, column=0)
        self.lbl_name = Label(self.frame1, text="Course Name", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=1, column=0)
        self.lbl_marks_obtained = Label(self.frame1, text="Marks Obtained", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=2, column=0)
        self.combo_id = ttk.Combobox(self.frame1, textvariable=self.combo_id_var, font=(
            "times new roman", 15, "bold"), state="readonly", justify=RIGHT)
        self.combo_id.grid(row=0, column=1, padx=2, pady=2)
        self.entry_name = Entry(self.frame1, textvariable=self.entry_name_var, font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=1, column=1, padx=5, pady=5)
        self.combo_std_id = ttk.Combobox(self.frame1, textvariable=self.combo_std_id_var, font=(
            "times new roman", 10, "bold"), width=10, state="readonly", justify=RIGHT)
        self.combo_std_id.place(x=100, y=75)
        self.lbl_roll = Label(self.frame1, textvariable=self.lbl_roll_var, text="Roll", bg="white", font=(
            "times new roman", 10, "bold"), borderwidth=1, relief="solid").place(x=200, y=75)
        self.lbl_marks = Label(self.frame1, textvariable=self.lbl_marks_var, text="Marks", bg="white", font=(
            "times new roman", 10, "bold"), borderwidth=1, relief="solid").place(x=270, y=75)

    #    self.entry_course=Entry(self.frame1,font=("times new roman",15,"bold"),bg="azure2").grid(row=3,column=1,padx=5,pady=5)
    # ===Buttons==========
        self.btn1_crud = Button(self.frame1, text="Add", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.crud_add).place(x=20, y=150)
        self.btn2_crud = Button(self.frame1, text="Update", font=("Comic Sans MS", 10, "bold"),
                                activebackground="green", activeforeground="white", fg="black",command=self.update_crud).place(x=60, y=150)
        self.btn3_crud = Button(self.frame1, text="Delete", font=("Comic Sans MS", 10, "bold"),
                                activebackground="green", activeforeground="white", fg="black",command=self.crud_delete).place(x=120, y=150)
        self.btn4_crud = Button(self.frame1, text="Clear", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.clear_crud).place(x=175, y=150)

        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open(
            "pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.search_entry = Entry(self.frame1, textvariable=self.search_entry_var, font=(
            "times new roman", 15, "bold"), bg="azure2").place(x=350, y=150)
        self.btn_search = Button(self.frame1,command=self.search_data, image=self.search_image,
                                 height=23, borderwidth=1, relief=GROOVE, bg="white")
        self.btn_search.place(x=550, y=150)
        self.show_allbtn = Button(self.frame1, text="Show All", width=10, height=0, pady=1, bg="OrangeRed3", font=(
            "times new roman", 10, "bold"),command=self.fetch_data).place(x=590, y=150)
        self.histo_btn = Button(
            self.frame1, text="Histogram", justify=CENTER,command=lambda:create_histogram(self.combo_id_var.get())).place(x=350, y=100)

    # ===========Content Under frame2====================
        scroll_x = ttk.Scrollbar(self.frame2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="grey71",
                             foreground="black", rowheight=25, fieldbackground="grey71")
        self.style.map("Treeview", background=[("selected", "green")])
        self.course_headings = pd.read_csv("csv_files\courses.csv")
        self.Course_Table = ttk.Treeview(self.frame2, columns=list(
            self.course_headings.columns), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Course_Table.xview)
        scroll_y.config(command=self.Course_Table.yview)

        for i in self.Course_Table["columns"]:
            self.Course_Table.heading(i, text=i)

        self.Course_Table["show"] = "headings"
        for i in self.Course_Table["columns"]:
            self.Course_Table.column(i, width=10)
        self.Course_Table.pack(fill=BOTH, expand=1)
        self.Course_Table["displaycolumns"] = list(
            self.course_headings.columns)

        self.fetch_data()
        self.Course_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.bind("<Button-1>", self.update_course)
        self.combo_id.bind("<<ComboboxSelected>>", self.update_ids_marks)
        self.combo_std_id.bind("<<ComboboxSelected>>", self.update_ids_marks_2)

    # =====================Functions=========================================
    def update_course(self, ev):
        df = pd.read_csv("csv_files\Batches.csv")
        content = df[df.columns[3]]
        batch_id = []

        for i in range(len(content.to_numpy().tolist())):
            batch_id.append(ast.literal_eval(content.to_numpy().tolist()[i]))

        a = [num for sublist in batch_id for num in sublist]
        self.combo_id["values"] = list(set(a))

    def update_ids_marks(self, ev):
        df = pd.read_csv("csv_files/exam.csv")
        filtered_df = df.loc[df['Course ID'] == self.combo_id_var.get()]
        std_id = []
        for i in filtered_df.to_numpy().tolist():
            std_id.append(i[1])

        self.combo_std_id["values"] = std_id

    def update_ids_marks_2(self, ev):
        df = pd.read_csv("csv_files/exam.csv")
        filtered_df = df.loc[df['Student ID'] == self.combo_std_id_var.get()]

        self.lbl_marks_var.set(
            "Marks:"+str(filtered_df.to_numpy().tolist()[0][2]))
        self.lbl_roll_var.set(
            "Rollno:"+filtered_df.to_numpy().tolist()[0][1][-2:])

    def get_data_indict(self, courseid):
        excel_file = r"csv_files/exam.csv"
        df = pd.read_csv(excel_file)
        filtered_df = df.loc[df['Course ID'] ==
                             courseid, ["Student ID", "Marks"]]
        return dict(filtered_df.to_numpy().tolist())

    def clear_crud(self):
        self.combo_id_var.set("")
        self.entry_name_var.set("")
        self.combo_std_id_var.set("")
        self.lbl_marks_var.set("")
        self.lbl_roll_var.set("")
    def search_data(self):
        if self.search_entry_var.get() == "":
            messagebox.showerror(
                "Error", "Entry box shouldn't be empty.", parent=self.root)
        else:
            try:
                df_filtered = self.course_headings.loc[self.course_headings[self.course_headings.columns[0]] == self.search_entry_var.get(
                )]
                df_rows = df_filtered.to_numpy().tolist()  
                for i in df_rows:
                    i[2] = self.get_data_indict(i[0])
                self.Course_Table.delete(*self.Course_Table.get_children())    
                for row in df_rows:
                    self.Course_Table.insert("", END, values=(row[0],row[1],row[2]))


            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)          
    def fetch_data(self):
        excel_filename = r"csv_files/courses.csv"
        if excel_filename:
            try:
                df = pd.read_csv(excel_filename)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
        self.Course_Table.delete(*self.Course_Table.get_children())
        df_rows = df.to_numpy().tolist()
        for i in df_rows:
            i[2] = self.get_data_indict(i[0])
        for row in df_rows:
            self.Course_Table.insert("", END, values=row)
    def get_cursor(self,ev):
        cursor_row = self.Course_Table.focus()
        content = self.Course_Table.item(cursor_row)
        self.Entry_fill = content["values"]         
        self.combo_id_var.set(self.Entry_fill[0])
        self.entry_name_var.set(self.Entry_fill[1])
    def crud_delete(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "":
            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files/courses.csv"
                self.df = pd.read_csv(excel_filename)
                self.df.drop(self.df.index[(
                    self.df[self.course_headings.columns[0]] == self.combo_id_var.get())], axis=0, inplace=True)

                self.df.to_csv(excel_filename, index=False)

                self.clear_crud()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
    def update_crud(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "":
            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files/courses.csv"
                self.df = pd.read_csv(excel_filename)
                for i in self.df.index:

                    if (self.df.loc[i, self.course_headings.columns[0]] == self.combo_id_var.get()):
                        
                        self.df.loc[i, self.course_headings.columns[1]
                                    ] = self.entry_name_var.get()

                        self.df.to_csv(excel_filename, index=False)
                        self.clear_crud()
                        self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)       
        
    def crud_add(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "":
            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                df = pd.read_csv("csv_files\courses.csv")
                if self.combo_id_var.get() not in list(df.loc[:, self.course_headings.columns[0]]):

                    data = {self.course_headings.columns[0]: [self.combo_id_var.get()], self.course_headings.columns[1]: [
                    self.entry_name_var.get()], self.course_headings.columns[2]: [[]]}
                
                    self.df = pd.DataFrame(data)
                    self.df.to_csv("csv_files\courses.csv", mode='a',
                                index=False, header=False)

                    self.clear_crud()
                    self.fetch_data()
                else:
                    messagebox.showerror(
                            "Error", "Course ID Already There.", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    main()
