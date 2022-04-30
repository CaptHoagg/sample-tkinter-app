from tkinter import *
from tkinter import messagebox
import pandas as pd

import Modules.first_page as fp


class SearchPage:
    def __init__(self):
        # create search page window
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

        # create search page background image
        self.background_img = PhotoImage(
            file=f"./Images/Search_page/background.png")
        self.background = self.canvas.create_image(
            250.0, 250.0,
            image=self.background_img)

        # Create search Entry
        self.searh_image = PhotoImage(
            file=f"./Images/Search_page/search_entry.png")
        self.search_image_bg = self.canvas.create_image(
            250.0, 165.0,
            image=self.searh_image)

        self.search_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.search_entry.place(
            x=105.0, y=145,
            width=290.0,
            height=38)

        # Create search button
        self.search_button_image = PhotoImage(
            file=f"./Images/Search_page/search_button.png")
        self.search_button = Button(
            image=self.search_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_button_handle,
            relief="flat")

        self.search_button.place(
            x=374, y=150,
            width=30,
            height=30)

        self.back_button_image = PhotoImage(file=f"./Images/back_button.png")
        self.back_button = Button(
            image=self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_handle,
            relief="flat")

        self.back_button.place(
            x=15, y=30,
            width=50,
            height=50)

        self.eng_text = Text(self.window, width=20, height=8)
        self.eng_text.place(x=80, y=220)

        self.vie_text = Text(self.window, width=20, height=8)
        self.vie_text.place(x=250, y=220)

    def back_button_handle(self):
        self.window.destroy()
        app = fp.FirstPage()
        app.window.mainloop()

    def search_button_handle(self):
        eng = self.search_entry.get()
        df = pd.read_csv('./Data/data.csv', names=['English', 'Vietnamese'])
        for i in range(len(df)):
            if eng == df.iloc[i][0]:
                messagebox.showinfo("Notification", "Word Founded")
                self.eng_text.insert(END, df.iloc[i][0])
                self.vie_text.insert(END, df.iloc[i][1])
                self.search_entry.delete(0, END)
                return 
        messagebox.showinfo("Notification", "Word Not Founded")
        self.search_entry.delete(0, END)

