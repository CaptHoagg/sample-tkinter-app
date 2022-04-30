from tkinter import *
import Modules.first_page as fp 
import tkinter.ttk as ttk
import csv

class AppPage:
    def __init__(self):

        #Create app page Window
        self.window = Tk()
        self.window.geometry("500x500")
        self.window.configure(bg="#ffffff")
        self.window.title("DICTIONARY BY TEAM 7")
        self.window.iconphoto(False, PhotoImage(file='./Images/icon.png'))
        self.canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        #Create app page background image
        self.background_img = PhotoImage(file=f"./Images/App_page/background.png")
        self.background = self.canvas.create_image(
            250.0, 250.0,
            image=self.background_img)

        self.back_button_image = PhotoImage(file = f"./Images/back_button.png")
        self.back_button = Button(
            image = self.back_button_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.back_button_handle,
            relief = "flat")

        self.back_button.place(
            x = 15, y = 30,
            width = 50,
            height = 50)


        #create a treeview
        self.TableMargin = Frame(self.window, width= 300, height= 200)
        self.TableMargin.place(x = 150, y = 160)
        self.scrollbarx = Scrollbar(self.TableMargin, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(self.TableMargin, columns=("English", "Vietnamese"), height=10, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading("English", text="English", anchor=W)
        self.tree.heading("Vietnamese", text="Vietnamese", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.pack()
        with open('./Data/data.csv', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                eng = row[0]
                vie = row[1]
                self.tree.insert("", 0, values=(eng, vie))

    def back_button_handle(self): 
        self.window.destroy()
        app = fp.FirstPage()
        app.window.mainloop()

    