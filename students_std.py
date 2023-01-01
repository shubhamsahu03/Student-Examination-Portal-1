from tkinter import *
import pandas as pd
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import ast
from pandas_tut import *


def main():
    root = Tk()
    obj = Student(root)
    root.mainloop()


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
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
    # ===============StringVAR==============================
        self.entry_id_var = StringVar()
        self.entry_roll_var = StringVar()
        self.entry_name_var = StringVar()
        self.combo_batch_id_var = StringVar()
        self.txt_search = StringVar()
    # =====Content Under frame1============
        self.lbl_id = Label(self.frame1, text="Student ID", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=0, column=0)
        self.lbl_name = Label(self.frame1, text="Student Name", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=1, column=0)
        self.lbl_roll = Label(self.frame1, text="Class Roll Number", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=2, column=0)
        self.lbl_marks_obtained = Label(self.frame1, text="Batch ID", bg="white", font=(
            "times new roman", 10, "bold")).grid(row=3, column=0)
        self.entry_id = Entry(self.frame1, textvariable=self.entry_id_var, state="readonly", font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=0, column=1, padx=5, pady=5)
        self.entry_name = Entry(self.frame1, textvariable=self.entry_name_var, font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=1, column=1, padx=5, pady=5)
        self.entry_roll = Entry(self.frame1, textvariable=self.entry_roll_var, font=(
            "times new roman", 15, "bold"), bg="azure2").grid(row=2, column=1, padx=5, pady=5)
        self.combo_batch_id = ttk.Combobox(self.frame1, textvariable=self.combo_batch_id_var, font=(
            "times new roman", 15, "bold"), state="readonly", justify=RIGHT)
        self.combo_batch_id.grid(row=3, column=1, padx=2, pady=2)
        self.btn1_crud = Button(self.frame1, text="Add", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.crud_add).place(x=20, y=150)
        self.btn2_crud = Button(self.frame1, text="Update", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.update_crud).place(x=60, y=150)
        self.btn3_crud = Button(self.frame1, text="Delete", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.crud_delete).place(x=120, y=150)
        self.btn4_crud = Button(self.frame1, text="Clear", font=("Comic Sans MS", 10, "bold"), activebackground="green",
                                activeforeground="white", fg="black", command=self.clear_crud).place(x=175, y=150)
        self.resetbtn = Button(self.frame1, text="Reset", bg="OrangeRed3", font=(
            "times new roman", 10, "bold")).place(x=220, y=150)

        self.search_image = ImageTk.PhotoImage(ImageTk.Image.open(
            "pictures_1/search_icon_2.jpg").resize((40, 40), ImageTk.Image.ANTIALIAS))
        self.search_entry = Entry(self.frame1, textvariable=self.txt_search, font=(
            "times new roman", 15, "bold"), bg="azure2").place(x=350, y=150)
        self.btn_search = Button(self.frame1, command=self.search_data,
                                 image=self.search_image, height=23, borderwidth=1, relief=GROOVE, bg="white")
        self.btn_search.place(x=550, y=150)
        self.show_allbtn = Button(self.frame1, command=self.fetch_data, text="Show All", width=10,
                                  height=0, pady=1, bg="OrangeRed3", font=("times new roman", 10, "bold")).place(x=590, y=150)
        self.generate_btn = Button(self.frame1, text="Generate Report Text File", font=(
            "times new roman", 10, "bold"), justify=CENTER, bg="red", activebackground="yellow", activeforeground="blue",command=lambda: report_card(self.entry_id_var.get())).place(x=350, y=100)

    # ============Treeview==================
        scroll_x = ttk.Scrollbar(self.frame2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame2, orient=VERTICAL)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="grey71",
                             foreground="black", rowheight=25, fieldbackground="grey71")
        self.style.map("Treeview", background=[("selected", "green")])
        self.student_headings = pd.read_csv("csv_files\students.csv")
        self.Student_Table = ttk.Treeview(self.frame2, columns=list(
            self.student_headings.columns), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        for i in self.Student_Table["columns"]:
            self.Student_Table.heading(i, text=i)

        self.Student_Table["show"] = "headings"
        for i in self.Student_Table["columns"]:
            self.Student_Table.column(i, width=10)
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table["displaycolumns"] = list(
            self.student_headings.columns)
        self.update_combobox()
        self.fetch_data()
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.combo_batch_id_var.trace("w", self.upd)
        self.entry_roll_var.trace("w", self.upd_2)


# =======================Functions===================================

    def upd_2(self, *args):
        self.entry_id_var.set(
            self.combo_batch_id_var.get()+self.entry_roll_var.get())

    def upd(self, *args):
        self.entry_id_var.set("")
        self.entry_id_var.set(self.combo_batch_id_var.get())

    def update_combobox(self):
        df = pd.read_csv("csv_files\department.csv")
        content = df[df.columns[2]]
        batch_id = []

        for i in range(len(content.to_numpy().tolist())):
            batch_id.append(ast.literal_eval(content.to_numpy().tolist()[i]))

        a = [num for sublist in batch_id for num in sublist]
        self.combo_batch_id["values"] = a

    def clear_crud(self):
        self.entry_id_var.set("")
        self.entry_name_var.set("")
        self.entry_roll_var.set("")
        self.combo_batch_id_var.set("")

    def crud_delete(self):
        if self.entry_id_var.get() == "" or self.entry_name_var.get() == "" or self.entry_roll_var.get() == "":

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files\students.csv"
                self.df = pd.read_csv(excel_filename)

                self.df.drop(self.df.index[(
                    self.df[self.student_headings.columns[0]] == self.entry_id_var.get())], axis=0, inplace=True)

                self.df.to_csv(excel_filename, index=False)

                self.clear_crud()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def update_crud(self):
        if self.entry_id_var.get() == "" or self.entry_name_var.get() == "" or self.entry_roll_var.get() == "":

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:
            try:
                excel_filename = r"csv_files\students.csv"
                self.df = pd.read_csv(excel_filename)
                for i in self.df.index:

                    if (self.df.loc[i, self.student_headings.columns[0]] == self.entry_id_var.get()):
                        print("Hello world")
                        self.df.loc[i, self.student_headings.columns[1]
                                    ] = self.entry_name_var.get()

                        self.df.to_csv(excel_filename, index=False)
                        self.clear_crud()
                        self.fetch_data()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        excel_filename = r"csv_files\students.csv"
        if excel_filename:
            try:
                df = pd.read_csv(excel_filename)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
        self.Student_Table.delete(*self.Student_Table.get_children())

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.Student_Table.insert("", END, values=row)

    def get_cursor(self, ev):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        self.Entry_fill = content["values"]
        self.entry_id_var.set(self.Entry_fill[0])
        self.entry_name_var.set(self.Entry_fill[1])
        self.combo_batch_id_var.set(self.Entry_fill[3])
        self.entry_roll_var.set(self.Entry_fill[2])

    def search_data(self):
        if self.txt_search.get() == "":
            messagebox.showerror(
                "Error", "Entry box shouldn't be empty.", parent=self.root)
        else:
            try:
                df_filtered = self.student_headings.loc[self.student_headings[self.student_headings.columns[0]] == self.txt_search.get(
                )]

                df_rows = df_filtered.to_numpy().tolist()
                self.Student_Table.delete(*self.Student_Table.get_children())
                for i in df_rows:
                    self.Student_Table.insert(
                        "", END, values=(i[0], i[1], i[2]))
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def crud_add(self):

        if self.entry_id_var.get() == "" or self.entry_name_var.get() == "" or self.entry_roll_var.get() == "":

            messagebox.showerror(
                "Error", "Entry bars should not be empty", parent=self.root)
        else:

            try:
                excel_filename = r"csv_files\students.csv"
                df = pd.read_csv(excel_filename)
                if self.entry_id_var.get() not in list(df.loc[:, self.student_headings.columns[0]]):
                    data = {self.student_headings.columns[0]: [self.entry_id_var.get()], self.student_headings.columns[1]: [
                        self.entry_name_var.get()], self.student_headings.columns[2]: [self.entry_roll_var.get()], self.student_headings.columns[3]: [self.combo_batch_id_var.get()]}

                    self.df = pd.DataFrame(data)
                    self.df.to_csv(excel_filename, mode='a',
                                   index=False, header=False)
                    self.clear_crud()
                    self.fetch_data()
                else:
                    messagebox.showerror(
                        "Error", "Student ID should be unique.", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    main()
