from tkinter import *
from tkinter import ttk, messagebox


def main():
    root = Tk()
    obj = TabMenu(root)
    root.mainloop()


class TabMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Examination Portal")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2)-(1200/2)
        y = (screen_height/2)-(500/2)
        self.root.geometry("1200x500+{}+{}".format(int(x), int(y)))
        self.root.resizable(False, False)

        # ==================NavBar===============================
        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftMenu.place(x=0, y=0, width=200, height=499)
        lbl_menu = Label(leftMenu, text="Menu", fg="azure1", font=(
            "times new roman", 20), bg="#009688").pack(side=TOP, fill=X)
        btn_department = Button(leftMenu, text="Department", compound=LEFT, padx=5, anchor="w", bg="white", cursor="hand2", bd=3, font=(
            "times new roman", 20, "bold"), command=self.toplevel_department).pack(side=TOP, fill=X)
        btn_batch = Button(leftMenu, text="Batch", compound=LEFT, padx=5, anchor="w", bg="white", cursor="hand2", bd=3, font=(
            "times new roman", 20, "bold"), command=self.toplevel_batch).pack(side=TOP, fill=X)
        btn_course = Button(leftMenu, text="Course", compound=LEFT, padx=5, anchor="w", bg="white", cursor="hand2", bd=3, font=(
            "times new roman", 20, "bold"), command=self.toplevel_course).pack(side=TOP, fill=X)
        btn_student = Button(leftMenu, text="Student", compound=LEFT, padx=5, anchor="w", bg="white", cursor="hand2", bd=3, font=(
            "times new roman", 20, "bold"), command=self.toplevel_student).pack(side=TOP, fill=X)
        btn_exam = Button(leftMenu, text="Examination", compound=LEFT, padx=5, anchor="w", bg="white", cursor="hand2", bd=3, font=(
            "times new roman", 20, "bold"), command=self.toplevel_exam).pack(side=TOP, fill=X)
        btn_logout = Button(leftMenu, text="Logout", fg="azure1", font=(
            "times new roman", 20, "bold"), bg="#FF0000", command=lambda: self.root.destroy()).pack(side=TOP, fill=X)

        self.batch_window = None
        self.student_window = None
        self.course_window = None
        self.exam_window = None
        self.dpt_window = None

    def toplevel_batch(self):

        if self.batch_window is None or not self.batch_window.winfo_exists():
            self.batch_window = Toplevel(self.root)
            from batches_std import Batches
            self.batches = Batches(self.batch_window)
        else:
            self.batch_window.focus_force()

    def toplevel_student(self):

        if self.student_window is None or not self.student_window.winfo_exists():
            self.student_window = Toplevel(self.root)
            from students_std import Student
            self.batches = Student(self.student_window)
        else:
            self.student_window.focus_force()

    def toplevel_exam(self):

        if self.exam_window is None or not self.exam_window.winfo_exists():
            self.exam_window = Toplevel(self.root)
            from examinations_std import Exam
            self.exam_ = Exam(self.exam_window)
        else:
            self.exam_window.focus_force()

    def toplevel_course(self):

        if self.course_window is None or not self.course_window.winfo_exists():
            self.course_window = Toplevel(self.root)
            from course_std import Course
            self.courses = Course(self.course_window)
        else:
            self.course_window.focus_force()

    def toplevel_department(self):

        if self.dpt_window is None or not self.dpt_window.winfo_exists():
            self.dpt_window = Toplevel(self.root)
            from department_std import Department
            self.dpt = Department(self.dpt_window)
        else:
            self.dpt_window.focus_force()


if __name__ == "__main__":
    main()
