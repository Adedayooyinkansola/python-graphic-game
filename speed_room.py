# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from properties import Properties

class SpeedRoom(Properties):

    def __init__(self, manage_game):
        super().__init__(manage_game)
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "lightblue") 
        image = Image.open("Assets/speedroom.png") 
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['speed_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "lightblue")
        background_images.place(x = 100, y = 85)
        self.speed()
        
    def speed(self):
        self.message.config(text ="You need to click on either north, west, east or south", font=("Roboto", 10))
        self.message.place(x = 350, y = 20)
        self.west_button.place_forget()
        self.south_button.place_forget()
        self.north_button.place(x = 390)
        self.east_button.place(x = 515)
        self.message.config(bg = "lightblue")
        self.answer.config(bg = "lightblue")

    def start_end_area(self):
        self.clear_screen()
        from end_room import EndRoom
        self.game.current_room = EndRoom(self.game)
        
    def display_inventory(self):
        super().display_inventory()
        self.inventory_message.config(bg = "lightblue")
        
    def messages(self):
        super().messages()
        self.item_message.config(bg = "lightblue")

    def go_north(self):
        self.east_button.place_forget()
        self.north_button.place_forget()

        self.screen.config(bg = "lightblue")
        self.answer.config(bg = "lightblue")

        # change the image
        image = Image.open("Assets/door.png")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['door_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "lightblue")
        background_images.place(x = 100, y = 85)

        # set the message
        self.message.config(text =
        "As you reached the final room in the forest, you saw a magical door that has a note on it.\n"
        "The note says, to open the door, you have to solve the challenge on the note.\n"
        "After solving the challenge, you will have to use the armour to find the sage\n."
        "Challenge: A mystical bird flies from one end of the enchanted forest to the other at a speed of 50 miles per hour.\n" 
        "If the bird takes 2 hours to complete the journey, what is the distance it travels?", bg = "lightblue")
 
        self.message.place(x = 190, y = 590)

        self.answer.place(x = 390, y = 690)

        # set input for player's answer
        self.input_box.place(x = 450, y = 690, width = 80, height = 25) 
            
        def check_north():
            player_answer = int(self.input_box.get())
            if player_answer == 100:
                self.message.config(text = "Correct! The distance is 100 miles. You can use an armour now")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Use armour", command = lambda: self.use_inventory("sage armour", 1, self.start_end_area, self.game.go_to_start_room))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Add the ages of all the friends together.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_north)
        self.submit_button.place(x = 535, y = 690, width = 80, height = 25)

    def go_east(self):
        self.north_button.place_forget()
        self.east_button.place_forget()

        self.screen.config(bg = "lightblue")
        self.answer.config(bg = "lightblue")

        # change the image
        image = Image.open("Assets/beast1.jpg")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['beast_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "lightblue")
        background_images.place(x = 100, y = 85)

        # set the message
        self.message.config(text = 
        "As you continue your journey through the forest, you found yourself at dead-end.\n"
        "A magical beast appears and eats you. To revive yourself, you have to complete a challenge.\n"
        "Challenge: A magical horse travels from the village to the Sage's hidden location at a speed of 30 miles per hour.\n" 
        "The distance between the village and the Sage's location is 90 miles.\n" 
        "How long does it take for the horse to reach the Sage's location?", font = ("Helvetica", 10), bg = "lightblue")
        self.message.place(x = 160, y = 590)

        self.answer.place(x = 390, y = 680)

        # set input for player's answer
        self.input_box.place(x = 450, y = 680, width = 80, height = 25)
            
        def check_east():
            player_answer = int(self.input_box.get())
            if player_answer == 3:
                self.message.config(text = "Correct! It takes 3 hours. You can revive yourself in the start room.")
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Revive", width = 100, command = self.game.go_to_start_room)
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


