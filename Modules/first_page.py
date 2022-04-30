from tkinter import * 
import Modules.add_page as addp
import Modules.app_page as appp 
import Modules.delete_page as delp 
import Modules.search_page as sp

class FirstPage: 
    def __init__(self): 

        #create first page window 
        self.window = Tk()
        self.window.geometry("500x500")
        self.window.configure(bg = "#ffffff")
        self.window.title("DICTIONARY BY TEAM 7")
        self.window.iconphoto(False, PhotoImage(file='./Images/icon.png'))
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 500,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        #create first page background image
        self.background_img = PhotoImage(file = f"./Images/First_page/background.png")
        self.background = self.canvas.create_image(
            250.0, 250.0,
            image= self.background_img)

        #Create search button
        self.search_image = PhotoImage(file = f"./Images/First_page/search_button.png")
        self.search_button = Button(
            image = self.search_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.search_page_button_handle,
            relief = "flat")

        self.search_button.place(
            x = 100, y = 140,
            width = 300,
            height = 50)
        

        #Create add button
        self.add_image = PhotoImage(file = f"./Images/First_page/add_button.png")
        self.add_button = Button(
            image = self.add_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.add_page_button_handle,
            relief = "flat")

        self.add_button.place(
            x = 100, y = 220,
            width = 300,
            height = 50)
        
        #Create app button 
        self.app_image = PhotoImage(file = f"./Images/First_page/app_button.png")
        self.app_button = Button(
            image = self.app_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.app_page_button_handle,
            relief = "flat")

        self.app_button.place(
            x = 100, y = 300,
            width = 300,
            height = 50)

        #Create delele button
        self.delete_image = PhotoImage(file = f"./Images/First_page/delete_button.png")
        self.delete_button = Button(
            image = self.delete_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.delete_page_button_handle,
            relief = "flat")

        self.delete_button.place(
            x = 100, y = 380,
            width = 300,
            height = 50)

    #call add page
    def add_page_button_handle(self):
        self.window.destroy() 
        app = addp.AddPage()
        app.window.mainloop()

    #call app page
    def app_page_button_handle(self):
        self.window.destroy()
        app = appp.AppPage()
        app.window.mainloop()
    
    #call delete page    
    def delete_page_button_handle(self):
        self.window.destroy()
        app = delp.DeletePage()
        app.window.mainloop()

    #call search page
    def search_page_button_handle(self):
        self.window.destroy()
        app = sp.SearchPage()
        app.window.mainloop()
