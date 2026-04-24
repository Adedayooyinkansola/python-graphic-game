# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from properties import Properties

class SimpleinterestRoom(Properties):

    def __init__(self, manage_game):
        super().__init__(manage_game)
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "#D8BFD8") 
        image = Image.open("Assets/simpleinterestroom.png") 
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['simpleinterest_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)
        self.simpleinterest()
        
    def simpleinterest(self):
        self.message.config(text ="You need to click on either north, west, east or south", font=("Roboto", 10), bg = "#D8BFD8")
        self.message.place(x = 350, y = 15)
        self.north_button.place_forget()
        self.west_button.place(x = 350)
        self.east_button.place(x = 475)
        self.south_button.place(x = 600)
        self.message.config(bg = "#D8BFD8")
        self.answer.config(bg = "#D8BFD8")

    def start_average_area(self):
        self.clear_screen()
        from average_room import AverageRoom
        self.game.current_room = AverageRoom(self.game)
        
    def display_inventory(self):
        super().display_inventory()
        self.inventory_message.config(bg = "#D8BFD8")

    def messages(self):
        super().messages()
        self.item_message.config(bg = "#D8BFD8")

    def go_west(self):
        self.east_button.place_forget()
        self.south_button.place_forget()
        self.west_button.place_forget()
        # self.south_button.place(x = 515)

        # change the image
        image = Image.open("Assets/map2.png")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['map_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)
        self.screen.config(bg = "#D8BFD8")
        self.answer.config(bg = "#D8BFD8")
        

        # set the message
        self.message.config(text = 
        "You came across a glass box that contains four maps that will be used to find the Sage.\n"
        "Then, on the box there is a note saying after solving the challenge given, the glass box will be broken.\n"
        "Challenge: You come across a scroll that promises to double your investment in 4 years at a simple interest rate.\n"
        "If you invest 400 gold coins, what is the annual interest rate?", bg = "#D8BFD8")
        self.message.place(x = 190, y = 590)

        self.answer.place(x = 390, y = 663)

        # set input for player's answer
        self.input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_west():
            player_answer = int(self.input_box.get())
            if player_answer == 25:
                self.message.config(text = "Correct! The answer is 25. The glass has been broken.")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Collect map", command = lambda: self.add_inventory("map", 4, self.start_average_area))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: The interest earned will be equal to the initial investment since it doubles.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_west)
        self.submit_button.place(x = 535, y = 663, width = 80, height = 25)

    def go_east(self):
        self.south_button.place_forget()
        self.west_button.place_forget()
        self.east_button.place_forget()
        # set the message
        self.message.config(text =
        "You reached a dead-end when moving around the forest. A magical beast appears and injures you.\n"
        "To recover, you have to complete this challenge to go back to the start room\n"
        "Challenge: You found a treasure that contains 600 gold coins, if invested at a simple interest rate of 6% per year.\n"
        "How many years will it take for the interest to amount to 180 gold coins?")
        self.message.place(x = 170, y = 590)

        self.answer.place(x = 390, y = 670)

        # set input for player's answer
        self.input_box.place(x = 450, y = 670, width = 80, height = 25)
            
        def check_east():
            player_answer = int(self.input_box.get())
            if player_answer == 5:
                self.message.config(text = "Correct! The answer is 5 years. You have to go back to the start room to recover.")
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Recover", command = self.game.go_to_start_room)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Use the formula for simple interest, Interest = Principal * Rate * Time")
                self.message.place(x = 150, y = 590)

        # set submit button
        self.submit_button.config(command = check_east)
        self.submit_button.place(x = 535, y = 670, width = 80, height = 25)

    def go_south(self):
        self.west_button.place_forget()
        self.east_button.place_forget()
        self.south_button.place_forget()

        # change the image
        image = Image.open("Assets/goldimage3.png")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['goldimage_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)
        self.screen.config(bg = "#D8BFD8")
        self.answer.config(bg = "#D8BFD8")

        # set the message
        self.message.config(text = 
        "As you continue going deeper into the forest, you came across a magical box that contains 500 gold coins.\n"
        "Then, on the box there is a note saying after solving the challenge given, you can use a key to open the box.\n"
        "Challenge: The Sage tells you that if you invest the coins found in the box at a simple interest rate of 5% per year.\n"
        "How much interest will you earn after 3 years?", bg = "#D8BFD8")
        self.message.place(x = 120, y = 590)

        self.answer.place(x = 390, y = 663)

        # set input for player's answer
        self.input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_south():
            player_answer = int(self.input_box.get())
            if player_answer == 75:
                self.message.config(text = "Correct! The answer is 75. You can now use a key to open the box.")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Use a key", command = lambda: self.use_inventory("key", 1, self.start_average_area, self.game.go_to_start_room))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Use the formula for simple interest, Interest = Principal * Rate * Time")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_south)
        self.submit_button.place(x = 535, y = 663, width = 80, height = 25)