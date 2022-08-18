from tkinter import *
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520
    
    def __init__(self):
        super().__init__()
        
        self.title("Food Encyclopedia")
        #ICON
        #self.icinbitmap("path")

        # ============ center the screen ============
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        width, height = 750, 420
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cord = int((screen_width/2) - (width/1.5))
        y_cord = int((screen_height/2) - (height/1.5))
        self.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


        # ============ create two frames ============

        # configure grid layout (1x4)
        self.grid_columnconfigure(0, minsize=50)
        self.grid_columnconfigure(3, minsize=50)
        self.grid_columnconfigure((1,2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,corner_radius=0)
        self.frame_left.grid(row=0, column=1,sticky="NSEW",pady=20)

        self.frame_right = customtkinter.CTkFrame(master=self,corner_radius=0)
        self.frame_right.grid(row=0, column=2,sticky="NSEW",pady=20)

        # ============ Right frame ============
        
        # configure grid layout (2x1)
        
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure((0,1), weight=1)
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,text="Eat breakfast like a king,\n" +
                                                        "lunch like a prince, and dinner like a pauper.\n" +
                                                        "– Adelle Davis" ,
                                                   
                                                   fg_color=("white", "gray38"),text_font=("Roboto", -12),corner_radius=10)  # <- custom tuple-color
        self.label_info_1.grid(column=0, row=0,sticky="News",pady=20, padx=20)
        
        # ============ Left frame ============

        self.bg_image = ImageTk.PhotoImage(Image.open("image.jpg").resize((450, 470)))
        self.image_label = Label(master=self.frame_left, image=self.bg_image,borderwidth=0,highlightthickness=0)
        self.image_label.grid(row=0, column=0)

        
        # ============ frame_input ============

        # configure grid layout (3x1)
        self.frame_input = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_input.grid(row=1, column=0, pady=20, padx=20, sticky="nsew")
        
        self.frame_input.rowconfigure((0,1), weight=1)
        self.frame_input.columnconfigure(0, weight=1)

        self.combobox = customtkinter.CTkComboBox(master=self.frame_input, values=["Rice", "Chapthi","idly","roti"])
        self.combobox.grid(row=0, column=0,sticky="S",pady=8)
        self.button = customtkinter.CTkButton(master=self.frame_input, text="Submit", command=self.create_toplevel)
        self.button.grid(row=1, column=0,sticky="N")


        # ============ frame_rad ============
        self.frame_rad = customtkinter.CTkFrame(master=self.frame_input,corner_radius=5)
        self.frame_rad.grid(row=2, column=0,padx=20,pady=10,sticky="NWE",ipadx=9,ipady=9)
        
        # configure grid layout (1x2)
        self.frame_rad.rowconfigure(0, weight=1)
        self.frame_rad.columnconfigure((0,1), weight=1)
        
        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_rad,text="Veg",width=20,height=20)
        self.check_box_2.grid(row=0, column=0)
        self.check_box_3 = customtkinter.CTkCheckBox(master=self.frame_rad,text="Non-Veg",width=20,height=20)
        self.check_box_3.grid(row=0, column=1)

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        window.title("Info")
        width, height = 750, 420
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cord = int((screen_width/2) - (width/1.5))
        y_cord = int((screen_height/2) - (height/1.5))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="Information")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)



if __name__ == "__main__":
    app = App()
    app.mainloop()
