import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("450x350")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

def my_insert(): # adding data to Combobox
    #if e1.get() not in cb1['values']:  # prevent duplicates
    cb1['values'] +=(e1.get(),) # add option
    e1.delete(0,'end') # remove the current selection

def my_delete(): # removing option from the Combobox
    my_new=[] # Blank list to hold new values 
    for opt in cb1['values']: # Loop through all options
        if(opt != cb1.get()): 
            #print(opt)
            my_new.append(opt) # Add to new list 
    cb1['values']=my_new # assign to new list 
    cb1.delete(0,'end') # remove from current selection text 

sel=tk.StringVar() # string variable 

months=['Jan','Feb','Mar']
cb1 = ttk.Combobox(my_w, values=months,width=7,textvariable=sel,font=22)
cb1.grid(row=1,column=1,padx=20,pady=30)

l1=tk.Label(my_w,text='Month')
l1.grid(row=1,column=2)

e1=tk.Entry(my_w,bg='Yellow',width=10,font=22)
e1.grid(row=1,column=3,padx=3)

b1=tk.Button(my_w,text='Add',command=lambda: my_insert(),font=18)
b1.grid(row=1,column=4)

b2=tk.Button(my_w,text='Delete',command=lambda: my_delete(),font=18)
b2.grid(row=1,column=5,padx=5)
#sel.trace('w',my_upd)

my_w.mainloop()