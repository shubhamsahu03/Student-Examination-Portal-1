"""import csv
flag=True
while flag:
    a=input("Enter deptid:")
    b=input("Enter name")
    c=input("List of batches:")
    with open("csv_files\department.csv","a") as csv_file:
        csv_writer=csv.writer(csv_file)
        csv_writer.writerow([a,b,list(c)])
    csv_file.close()    
    flag=bool(int(input("Enter 1 to contnue\n2. 0 to Exit")))
"""


"""
import ast

string="['PG22','PG20']"
list_=ast.literal_eval(string)
print(list_)"""

"""from tkinter import *

def validate(string):
    # Return False if the string is only digits, True otherwise
    return not string.isdigit()

root = Tk()

entry = Entry(root, validate="key", validatecommand=(root.register(validate), "%S"))
entry.pack()

root.mainloop()"""


'''import pandas as pd
df=pd.read_csv("csv_files\students.csv")

in_lst=df.loc[df[df.columns[3]]=="CSE(AIML)22"]



print(in_lst)    '''


'''excel_file=r"csv_files/exam.csv"
df=pd.read_csv(excel_file)
x=input("Enter course ID:")
y=input("Enter Name")
filtered_df = df.loc[(df['Course ID'] ==x) & (df["Student ID"]==y),["Student ID","Marks"]]
print("Result is:",list(itertools.chain(*filtered_df.to_numpy().tolist())))'''




from texttable import Texttable
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import itertools,ast
def get_list_of_pct(dictionary):
    pct_lst = []
    for key in dictionary:
        sum = 0
        value_list = dictionary[key]
        for element in value_list:
          # Add the element to the total sum
            sum += element
        pct = (sum/(len(value_list)*100))*100
        pct_lst.append(pct)
    if pct_lst != []:

        return pct_lst
    else:
        return ["NA"]


'''tableObj=Texttable()
tableObj.set_cols_align(["l", "r", "c"])
  
# Set datatype of each column
tableObj.set_cols_dtype(["a", "i", "t"])
  
# Adjust columns
tableObj.set_cols_valign(["t", "m", "b"])
  
# Insert rows
tableObj.add_rows([
        ["ORGANIZATION", "ESTABLISHED", "CEO"],
        ["Google", 1998, "Sundar Pichai"],
        ["Microsoft", 1975, "Satya Nadella"],
        ["Nokia", 1865, "Rajeev Suri"],
        ["Geeks for Geeks", 2008, "Sandeep Jain"],
        ["HackerRank", 2007, "Vivek Ravisankar"]
        ])
  
# Display table
print(tableObj.draw())'''


def report_card(student_id):
    def grade(marks):
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        elif marks >= 50:
            grade = 'E'
        else:
            return ['F', 'Failed']
        return [grade, 'Passed']

    df = pd.read_csv("csv_files\exam.csv")
    wanted_rows = df.loc[df[df.columns[1]] ==
                         student_id, [df.columns[0], df.columns[2]]]

    exams = []
    for i in wanted_rows.to_numpy().tolist():
        result = grade(i[1])

        i.append(result)
        exams.append(i)

    marksheet = Texttable()
    marksheet.set_cols_dtype(["t", "i", "i", "a"])
    marksheet.set_cols_align(['l', 'r', 'r', 'c'])
    marksheet.add_row(['Course Id', 'Marks Obtained', 'Full Marks', 'Grade'])
    for i in exams:
        marksheet.add_row([i[0], i[1], 100, i[2]])
    number = len(exams)

    with open(f'outputs/{student_id}-report_card.txt', 'w') as report:
        report.write(f'''
    {student_id} ({student_id[-2:]})

    {marksheet.draw()}

    ID:{student_id}
    Batch:{student_id[:-2]}
    ''')


# Create the scatter plot



# create a dictionary of courses and studentID-marks

# create histogram


def create_histogram(courseid):
    df = pd.read_csv("csv_files/exam.csv")
    filtered_df = df.loc[df['Course ID'] == courseid]
    std_id = []
    for i in filtered_df.to_numpy().tolist():
        std_id.append([i[1], i[2]])
    # print(std_id)

    def grade(marks):
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        elif marks >= 50:
            grade = 'E'
        else:
            return "F"
        return grade
    for i in std_id:
        i[1] = grade(i[1])
    codes = []
    grades = []

    for item in std_id:
        codes.append(item[0])
        grades.append(item[1])

    df = pd.DataFrame({'Course': codes,
                       'Grade': grades})

    # Create the histogram
    sns.countplot(x='Grade', data=df, order=[
                  'A', 'B', 'C', 'D', 'E', 'F'], color='green', edgecolor="black")

    # Add labels and show the plot
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Histogram of Grades')
    plt.show()


def create_scatter_plot(csv_filename):
    df = pd.read_csv(csv_filename)
    df["BatchID"] = df["Student ID"].apply(lambda x: x[:-2])

    sns.scatterplot(x=df.columns[2], y=df.columns[3],
                    hue=df.columns[0], data=df, palette="dark")
    plt.xlabel('Marks')
    plt.ylabel('Batches')
    plt.title('Scatterplot of marks and batches by courses')
    plt.show()
def create_lineplot():
    pass
def get_marks(course_id, student_id):
        excel_file = r"csv_files/exam.csv"
        df = pd.read_csv(excel_file)

        filtered_df = df.loc[(df['Course ID'] == course_id) & (
            df["Student ID"] == student_id), ["Student ID", "Marks"]]

        return list(itertools.chain(*filtered_df.to_numpy().tolist()))

def get_lst_of_courses(batchid):
    df=pd.read_csv("csv_files/Batches.csv")
    filtered_df=df.loc[df["Batch ID"]==batchid]
    return ast.literal_eval(filtered_df.to_numpy().tolist()[0][3])
def get_lst_of_batches(deptid):
    df=pd.read_csv("csv_files/department.csv")
    filtered_df=df.loc[df["Department ID"]==deptid,["Batches"]]
    return ast.literal_eval(filtered_df.to_numpy().tolist()[0][0])
#print(get_lst_of_batches("CSE(AIML)"))    
def get_average(lst):
    total = 0
    for number in lst:
        total += number

    average = total / len(lst)
    return average
# create_histogram("COO1")
