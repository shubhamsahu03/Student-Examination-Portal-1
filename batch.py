from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import ast
import threading
import time
import itertools
from tabulate import tabulate
from pandas_tut import *
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    root = Tk()
    obj = Batches(root)
    root.mainloop()


class Batches:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Management")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2)-(1000/2)
        y = (screen_height/2)-(500/2)
        self.root.geometry("1000x500+{}+{}".format(int(x)+100, int(y)))
        self.root.resizable(False, False)

    # ========frames====================
        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=10, y=20, height=200, width=960)
        self.frame2 = Frame(self.root, bg="white", relief=RIDGE)
        self.frame2.place(x=10, y=230, height=250, width=960)
        self.frame3 = Frame(self.frame1, bg="white", relief=RIDGE)
        self.frame3.place(x=800, y=50)
    # ===================StringVar=========================
        self.combo_id_var = StringVar()
        self.entry_name_var = StringVar()
        self.course_var = StringVar()
        self.txt_search = StringVar()
    # =======frame1_content============
        self.lbl_id = Label(self.frame1, text="Batch ID", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=0, column=0)
        self.lbl_name = Label(self.frame1, text="Batch Name", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=1, column=0)
        self.lbl_course_lst = Label(self.frame1, text="List of Courses", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=2, column=0)

        self.combo_id = ttk.Combobox(self.frame1, textvariable=self.combo_id_var, font=(
            "times new roman", 15, "bold"), state="readonly", justify=RIGHT)
        self.combo_id.grid(row=0, column=1, padx=2, pady=2)
        self.entry_name = Entry(self.frame1, textvariable=self.entry_name_var, font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=1, column=1, padx=5, pady=5)
        self.listbox = Listbox(self.frame1, bg="azure3",
                               highlightcolor="orange", width=33, height=5)
        self.listbox.grid(row=2, column=1)
        self.entry_course = Entry(self.frame1, textvariable=self.course_var, font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=3, column=1, padx=5, pady=5)
        # ================RELOAD button================
        self.reset_image = ImageTk.PhotoImage(ImageTk.Image.open(
            "pictures_1/reset_btn.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.reset_btn = Button(self.frame1, image=self.reset_image, height=23, borderwidth=1,
                                relief=GROOVE, command=self.update_combobox()).place(x=310, y=5)

        self.btn1 = Button(self.frame1, text="Add", justify=CENTER,
                           command=self.add_course).grid(row=2, column=3,)
        self.btn2 = Button(self.frame1, text="Delete", justify=CENTER,
                           command=lambda: self.listbox.delete(ANCHOR)).grid(row=2, column=4,)
        self.text_std = Text(self.frame1, height=10, width=50, bg="yellow")
        self.text_std.place(x=390, y=10)

        self.btn_pie = Button(self.frame1, text="Plot Piechart",
                              justify=CENTER,command=lambda:self.display_piechart(self.combo_id_var.get())).place(x=800, y=10)
        self.btn1_crud = Button(self.frame3, text="Add", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", relief=RIDGE, bd=2, command=self.crud_add).pack(side=TOP, fill=X)
        self.btn2_crud = Button(self.frame3, text="Update", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", relief=RIDGE, bd=2, command=self.update_crud).pack(side=LEFT)
        self.btn3_crud = Button(self.frame3, text="Delete", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", relief=RIDGE, bd=2, command=self.crud_delete).pack(side=RIGHT)
        self.btn4_crud = Button(self.frame3, text="Clear", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", relief=RIDGE, bd=2, command=self.clear_crud).pack(side=BOTTOM)
        self.lbl_search_by = Label(self.frame1, text="Search By BatchID", font=(
            "Comic Sans MS", 10, "bold"), bg="white").place(x=800, y=125)
        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open(
            "pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.search_entry = Entry(self.frame1, textvariable=self.txt_search, font=(
            "times new roman", 10, "bold"), bg="azure2").place(x=800, y=150)
        self.btn_search = Button(self.frame1, image=self.search_image, height=23,
                                 borderwidth=1, relief=GROOVE, bg="white", command=self.search_data)
        self.btn_search.place(x=880, y=170)
        self.show_allbtn = Button(self.frame1, command=self.fetch_data, text="Show All", width=10,
                                  height=0, pady=1, bg="OrangeRed3", font=("times new roman", 10, "bold")).place(x=800, y=170)

    # ===========Content Under frame2
        scroll_x = ttk.Scrollbar(self.frame2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="grey71",
                             foreground="black", rowheight=25, fieldbackground="grey71")
        self.style.map("Treeview", background=[("selected", "green")])

        self.batches_headings = pd.read_csv("csv_files\Batches.csv")
        self.Batch_Table = ttk.Treeview(self.frame2, columns=list(
            self.batches_headings.columns), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Batch_Table.xview)
        scroll_y.config(command=self.Batch_Table.yview)

        for i in self.Batch_Table["columns"]:
            self.Batch_Table.heading(i, text=i)

        self.Batch_Table["show"] = "headings"
        for i in self.Batch_Table["columns"]:
            self.Batch_Table.column(i, width=10)
        self.Batch_Table.pack(fill=BOTH, expand=1)
        self.Batch_Table["displaycolumns"] = list(
            self.batches_headings.columns)

        self.Batch_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.update_combobox()
        self.fetch_data()
    # ===========================Functions====================================

    def update_combobox(self):
        df = pd.read_csv("csv_files\department.csv")
        content = df[df.columns[2]]
        batch_id = []

        for i in range(len(content.to_numpy().tolist())):
            batch_id.append(ast.literal_eval(content.to_numpy().tolist()[i]))

        a = [num for sublist in batch_id for num in sublist]
        self.combo_id["values"] = a

    def add_course(self):
        if self.course_var.get() != "":
            if self.course_var.get() not in self.listbox.get(0, END):

                self.listbox.insert(END, self.course_var.get())

                self.course_var.set("")

            else:
                self.course_var.set("")

    def fetch_data(self):
        excel_filename = r"csv_files\batches.csv"
        if excel_filename:
            try:
                df = pd.read_csv(excel_filename)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
        self.Batch_Table.delete(*self.Batch_Table.get_children())

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.Batch_Table.insert("", END, values=row)

    def crud_delete(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "" or list(self.listbox.get(0, END)) == []:

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files\Batches.csv"
                self.df = pd.read_csv(excel_filename)

                self.df.drop(self.df.index[(
                    self.df[self.batches_headings.columns[0]] == self.combo_id_var.get())], axis=0, inplace=True)

                self.df.to_csv(excel_filename, index=False)

                self.clear_crud()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def update_crud(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "" or list(self.listbox.get(0, END)) == []:

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files\Batches.csv"
                self.df = pd.read_csv(excel_filename)
                for i in self.df.index:

                    if (self.df.loc[i, self.batches_headings.columns[0]] == self.combo_id_var.get()):
                        print("Hello world")
                        self.df.loc[i, self.batches_headings.columns[1]
                                    ] = self.entry_name_var.get()
                        self.df.loc[i, self.batches_headings.columns[3]] = list(
                            self.listbox.get(0, END))

                        self.df.to_csv(excel_filename, index=False)
                        self.clear_crud()
                        self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def clear_crud(self):
        self.combo_id_var.set("")
        self.entry_name_var.set("")
        self.course_var.set("")
        self.listbox.delete(0, END)
        self.text_std.delete("1.0", "end")

    def get_cursor(self, ev):
        cursor_row = self.Batch_Table.focus()
        content = self.Batch_Table.item(cursor_row)
        self.Entry_fill = content["values"]
        self.combo_id_var.set(self.Entry_fill[0])
        self.entry_name_var.set(self.Entry_fill[1])
        self.listbox.delete(0, END)
        a = ast.literal_eval(self.Entry_fill[3])
        for i in a:
            self.listbox.insert(END, i)
        self.text_std.delete(1.0, "end")
        self.student_lst = self.student_lister(self.Entry_fill[0])
        pct_list=self.return_lst_ofmarks(self.student_lst)
        self.student_lst["Percentages(%)"]=pct_list

        self.text_std.insert(END, tabulate(self.student_lst, tablefmt="grid"))
        
    def display_piechart(self,batchid):
        student_lst = self.student_lister(batchid)
        pct_list=self.return_lst_ofmarks(student_lst)
        student_lst["Percentages(%)"]=pct_list
        filtered_rows=student_lst.loc[:,[student_lst.columns[0],student_lst.columns[2]]]
        studentID = []
        marks = []

        for item in filtered_rows.to_numpy().tolist():#[["stdid","percentage"],["C",]]
            studentID.append(item[0])
            marks.append(item[1])

        colors = sns.color_palette('bright')[0:5]

        #create pie chart
        plt.pie(marks, labels = studentID, colors = colors, autopct='%.0f%%')
        plt.title(f"{batchid}: Percentage of All students")
        plt.show()
    def search_data(self):
        if self.txt_search.get() == "":
            messagebox.showerror(
                "Error", "Entry box shouldn't be empty.", parent=self.root)
        else:
            try:
                df_filtered = self.batches_headings.loc[self.batches_headings[self.batches_headings.columns[0]] == self.txt_search.get(
                )]

                df_rows = df_filtered.to_numpy().tolist()
                self.Batch_Table.delete(*self.Batch_Table.get_children())
                for i in df_rows:
                    self.Batch_Table.insert(
                        "", END, values=(i[0], i[1], i[2], i[3], i[4]))
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def crud_add(self):
        if self.combo_id_var.get() == "" or self.entry_name_var.get() == "" or list(self.listbox.get(0, END)) == []:

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:

            try:
                excel_filename = r"csv_files\batches.csv"
                df = pd.read_csv(excel_filename)
                if self.combo_id_var.get() not in list(df.loc[:, self.batches_headings.columns[0]]):
                    batch_ids = self.find_students_in_batch(
                        self.combo_id_var.get())
                    data = {self.batches_headings.columns[0]: [self.combo_id_var.get()], self.batches_headings.columns[1]: [
                        self.entry_name_var.get()], self.batches_headings.columns[2]: [self.combo_id_var.get()[:-2]], self.batches_headings.columns[3]: [list(self.listbox.get(0, END))], self.batches_headings.columns[4]: [batch_ids]}

                    self.df = pd.DataFrame(data)
                    self.df.to_csv(excel_filename, mode='a',
                                   index=False, header=False)
                    self.clear_crud()
                    self.fetch_data()
                else:
                    messagebox.showerror(
                        "Error", "Department ID should be unique.", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def find_students_in_batch(self, batch_id):
        df = pd.read_csv("csv_files\students.csv")
        in_lst = df.loc[df[df.columns[3]] == batch_id].to_numpy().tolist()
        return [i[0] for i in in_lst]

    def student_lister(self, batch_id):
        df = pd.read_csv("csv_files\students.csv")

        in_lst = df.loc[df[df.columns[3]] ==
                        batch_id, [df.columns[0], df.columns[1]]]
        #pct_lst=self.return_lst_ofmarks()  
        #in_lst["Percentages(%)"]=pct_lst              
        #in_lst=in_lst.assign(Percentages=self.return_lst_ofmarks())                
        return in_lst
    

    def return_lst_ofmarks(self,c):
        # print([i for i in self.listbox.get(0,END)])

        a = []
        
        for i in [i[0] for i in c.to_numpy().tolist()]:
            for j in self.listbox.get(0, END):
                b = self.get_marks(j, i)
                if b != []:
                    a.append(b)
        dictionary = {}

        for item in a:
            key = item[0]
            value = item[1]
            if key in dictionary:
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]
        
        return get_list_of_pct(dictionary)

    def get_marks(self, course_id, student_id):
        excel_file = r"csv_files/exam.csv"
        df = pd.read_csv(excel_file)

        filtered_df = df.loc[(df['Course ID'] == course_id) & (
            df["Student ID"] == student_id), ["Student ID", "Marks"]]

        return list(itertools.chain(*filtered_df.to_numpy().tolist()))


if __name__ == "__main__":
    main()
