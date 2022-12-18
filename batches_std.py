from tkinter import *

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

if __name__=="__main__":
    main()               