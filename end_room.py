# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from properties import Properties

class EndRoom(Properties):

    def __init__(self, manage_game):
        super().__init__(manage_game)
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "#B0C4DE") 
        image = Image.open("Assets/endroom.png") 
        image = image.resize((900, 550), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['sage_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#B0C4DE")
        background_images.place(x = 100, y = 80)
        self.endroom()
        
    def endroom(self):
        self.north_button.place_forget()
        self.east_button.place_forget()
        self.west_button.place_forget()
        self.south_button.place_forget()
        self.answer.config(bg = "#B0C4DE")
        
        self.message.config(text ="You need to click on restart game if you want to continue to play the game", font=("Roboto", 11), bg = "#B0C4DE")
        self.message.place(x = 320, y = 635)
        # self.submit_button.config(text = "Restart game")
        # self.submit_button.config(command = self.game.go_to_start_room)
        self.restart_button.place(x = 480, y = 670, width = 100, height = 30)

        self.congrat_message = gui.Label(self.screen, text = "Congratulations! You have reached the end of the game", font = ("Roboto", 16), bg = "#B0C4DE", justify = "center")
        self.congrat_message.place(x = 250, y = 20)
