from tkinter import * 
import Modules.first_page as fp 


class LandingPage: 
    def __init__(self):

        #Create window 
        self.window = Tk()
        self.window.geometry("500x500")
        self.window.configure(bg = "#ffffff")
        self.window.title("DICTIONARY BY TEAM 7")
        self.window.iconphoto(False, PhotoImage(file='./Images/icon.png'))
        
        #Create Canvas 
        self.canvas = Canvas(self.window,bg = "#ffffff",height = 500,width = 500,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        
        #Set up background image
        self.background_img = PhotoImage(file = f"./Images/Landing/background.png")
        self.background = self.canvas.create_image(250.0, 250.0,image=self.background_img)
        self.window.after(2000, self.delay)
        
    #delay function
    def delay(self): 
        self.window.destroy()
        app = fp.FirstPage()
        app.window.mainloop()
