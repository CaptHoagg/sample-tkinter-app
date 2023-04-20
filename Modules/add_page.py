from tkinter import *
import Modules.first_page as fp 
import pandas as pd 
from tkinter import messagebox


class AddPage:
    def __init__(self):

        # create add page window
        self.window = Tk()
        self.window.geometry("500x500")
        self.window.configure(bg="#ffffff")
        self.window.title("DICTIONARY BY Team 5555555")
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

        # create add page background image
        self.background_img = PhotoImage(
            file=f"./Images/Add_page/background.png")
        self.background = self.canvas.create_image(
            250.0, 250.0,
            image=self.background_img)

        # Create add button
        self.add_button_image = PhotoImage(file=f"./Images/Add_page/img0.png")
        self.add_button = Button(
            image=self.add_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_button_handle,
            relief="flat")

        self.add_button.place(
            x=225, y=409,
            width=50,
            height=50)

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

        self.eng_text = Text(self.window, width=20, height= 10)    
        self.eng_text.place(x=70, y =180)

        self.vie_text = Text(self.window, width=20, height= 10) 
        self.vie_text.place(x =270, y = 180 )

    def back_button_handle(self): 
        self.window.destroy()
        app = fp.FirstPage()
        app.window.mainloop()

    def add_button_handle(self):
        #Get Data from Text Widget
        eng = self.eng_text.get("1.0", "end-1c")
        vie = self.vie_text.get("1.0", "end-1c")

        #check if data is exitsed
        df = pd.read_csv('./Data/data.csv', names= ['English', 'Vietnamese'])
        for i in range(len(df)):
            if df.iloc[i, 0] == eng:
                messagebox.showerror("Error", "This word is existed")
                self.vie_text.delete("1.0", END)
                self.eng_text.delete("1.0", END)
                return 

        #add new data to data.csv
        with open("./Data/data.csv", "a", encoding="utf8") as f:
            f.writelines((f"{eng},{vie}\n"))
            messagebox.showinfo("Success", "Added successfully")
            self.vie_text.delete("1.0", END)
            self.eng_text.delete("1.0", END)


