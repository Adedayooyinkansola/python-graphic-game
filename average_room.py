# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from properties import Properties

class AverageRoom(Properties):

    def __init__(self, manage_game):
        super().__init__(manage_game)
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "#D8BFD8") 
        image = Image.open("Assets/averageroom.png") 
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['average_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)
        self.average()
        
    def average(self):
        self.message.config(text ="You need to click on either north, west, east or south", font=("Roboto", 10))
        self.message.place(x = 350, y = 20)
        self.north_button.place_forget()
        self.south_button.place_forget()
        self.west_button.place(x = 390)
        self.east_button.place(x = 515)
        self.message.config(bg = "#D8BFD8")
        self.answer.config(bg = "#D8BFD8")

    def start_speed_area(self):
        self.clear_screen()
        from speed_room import SpeedRoom
        self.game.current_room = SpeedRoom(self.game)
        
    def display_inventory(self):
        super().display_inventory()
        self.inventory_message.config(bg = "#D8BFD8")
        
    def messages(self):
        super().messages()
        self.item_message.config(bg = "#D8BFD8")
    
    def go_west(self):
        self.west_button.place_forget()
        self.east_button.place_forget()

        self.screen.config(bg = "#D8BFD8")
        self.answer.config(bg = "#D8BFD8")

        # change the image
        image = Image.open("Assets/map1.jpg")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['map_picture'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)

        # set the message
        self.message.config(text =
        "As you go deeper into the forest to find the sage, you reached a village where five friends lived.\n"
        "To pass that village, you have to solve the challenge given by the five friends.\n"
        "The five friends will then give you a magical map that will take you to the final room.\n."
        "Challenge: In a quiet village, the ages of five friends are 12, 14, 16, 18, and 20 years.\n" 
        "What is the average age of the friends?", bg = "#D8BFD8")
        self.message.place(x = 240, y = 590)

        self.answer.place(x = 390, y = 680)

        # set input for player's answer
        self.input_box.place(x = 450, y = 680, width = 80, height = 25)
            
        def check_west():
            player_answer = int(self.input_box.get())
            if player_answer == 16:
                self.message.config(text = "Correct! The average age is 16. You can collect the map.")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Collect map", command = lambda: self.add_inventory("final map", 1, self.start_speed_area))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Add the ages of all the friends together.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_west)
        self.submit_button.place(x = 535, y = 680, width = 80, height = 25)

    def go_east(self):
        self.west_button.place_forget()
        self.east_button.place_forget()
        self.screen.config(bg = "#E0FFFF")
        self.answer.config(bg = "#E0FFFF")

        # change the image
        image = Image.open("Assets/armour1.png")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['armour_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#E0FFFF")
        background_images.place(x = 100, y = 85)

        # set the message
        self.message.config(text = 
        "As you continue your journey through the forest, you found yourself at the side of a magical ocean. The ocean glows with a bright light.\n"
        "Under the ocean, is the sage's armour that will take you to the Sage but you have to complete a challenge to get the armour.\n"
        "Challenge: In the enchanted forest, you collect 7 magical stones with the following weights: 3, 5, 7, 9, 11, 13, and 15 grams.\n" 
        "However, one of the stones is replaced by a heavier stone, and the new average weight becomes 11 grams.\n" 
        "What is the weight of the new stone if the stone that was replaced weighed 7 grams?", font = ("Helvetica", 10), bg = "#E0FFFF")
        self.message.place(x = 130, y = 590)

        self.answer.place(x = 390, y = 680)

        # set input for player's answer
        self.input_box.place(x = 450, y = 680, width = 80, height = 25)
            
        def check_east():
            player_answer = int(self.input_box.get())
            if player_answer == 21:
                self.message.config(text = "Correct! The weight is 21. You can collect the armour.")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Collect armour", command = lambda: self.add_inventory("sage armour", 1, self.start_speed_area))
                self.submit_button.place(width = 100)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Count the number of red fish and green fish in the pond.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_east)
        self.submit_button.place(x = 535, y = 680, width = 80, height = 25)
