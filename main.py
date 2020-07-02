from tkinter import *
from ocr import *


root = Tk()
root.geometry("500x300")
root.title("Tesseract-Ocr-demo")
root.resizable(height="False",width="False")


class TessOcr:

    def __init__(self,master):

        self.label1= Label(master,text="")
        self.label1.pack()
        self.but1 = Button(master,text="Convert",command=self.Change)
        self.but1.place(x=150,y=200)
        self.but2 = Button(master,text="Quit",command=self.quit)
        self.but2.place(x=300,y=200)

    def Change(self):

        self.label1.configure(text= convert())
    


    def quit(self):
    
        exit()






run = TessOcr(root)
root.mainloop()

