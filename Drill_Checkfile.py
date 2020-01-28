

import tkinter
from tkinter import*

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 300))
        self.master.title('Check files')
        self.master.config(bg='whitesmoke')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.btnBrowse = Button(self.master,text='Browse...', width=17, font=('Helvitica',12), fg='black',bg='whitesmoke')
        self.btnBrowse.grid(row=0, column=0,padx=(30,0), pady=(30,0))
                    
        self.btnBrowse2 = Button(self.master,text='Browse...', width=17, font=('Helvitica',12), fg='black',bg='whitesmoke')
        self.btnBrowse2.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.btnBrowse2 = Button(self.master,text='Check for files...', width=17, height=3, font=('Helvitica',12), fg='black',bg='whitesmoke')
        self.btnBrowse2.grid(row=2, column=0,padx=(30,0), pady=(30,0))

        self.input = Entry(font=('Helvetica', 12), width=49, fg='black', bg='white')
        self.input.grid(row=0, column= 2, padx=(30,0), pady=(30,0))

        self.input2 = Entry(font=("Helvetica", 12), width=49, fg='black', bg='white')
        self.input2.grid(row=1, column= 2, padx=(30,0), pady=(30,0))
        
        self.btnCancel = Button(self.master, text='Close Program', width=17, height=3, font=("Helvetica", 12), command=self.cancel)
        self.btnCancel.grid(row=2, column=2, padx=(30,0), pady=(30,0), sticky=E)
                    
                    
    def cancel(self):
        self.master.destroy()
                    
                
if __name__ == '__main__':
        root = Tk()
        App = ParentWindow(root)
        root.mainloop()
