# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:22:14 2023

@author: Ankan Datta
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
root.title("CLASSES")
root.geometry("900x750")
root.configure(bg = "cyan")


selected = ""
class createElements:
    
    def _init_ (self):
        print("This is create element class")
        
    def createLabel(self):
        label = Label(root, text = "A new label has been created using classes", bg = "yellow")
        label.pack()
        
    def createButton(self):
        btn = Button(root, text = "Button", command = self.showMessage, bg = "lightgreen")
        btn.pack(padx = 20, pady = 10)
        
    def showMessage(self):
        messagebox.showinfo("Show Info", "You clicked the button created using classes")
        
    def createDropdown(self):
        dropdown_list = ["1", "2", "3"]
        dd1 = ttk.Combobox(root, state = "readonly", values=dropdown_list)
        dd1.pack()
        
    def choosing(self):
        global selected
        selected = d1.get()
        
        if(selected == "Label"):
            self.createLabel()
            
        elif(selected == "Dropdown"):
            self.createDropdown()
            
        elif(selected == "Button"):
            self.createButton()
        
obj_of_createElements = createElements()

elements_using = ["Label", "Dropdown", "Button"]
d1 = ttk.Combobox(root, state = "readonly", values=elements_using)
d1.pack()

btn1 = Button(root, text = "Click To Create Elements", command = obj_of_createElements.choosing, bg = "blue", fg = "white")
btn1.pack(padx = 20, pady = 10)

root.mainloop()
