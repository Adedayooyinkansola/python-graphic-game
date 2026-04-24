# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from properties import Properties

class ProbabilityRoom(Properties):
    def __init__(self, manage_game):
        super().__init__(manage_game)
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "lightblue") 
        image = Image.open("Assets/probabilityroom.png") 
        image = image.resize((850, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['probability_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "lightblue")
        background_images.place(x = 100, y = 85)
        self.probability()

    def probability(self):
        self.message.config(text ="You need to click on either north, west, east or south", font=("Roboto", 10), bg = "lightblue")
        self.message.place(x = 350, y = 20)
        self.west_button.place_forget()
        self.east_button.place_forget()
        self.north_button.place(x = 390)
        self.south_button.place(x = 515)
        self.message.config(bg = "lightblue")
        self.answer.config(bg = "lightblue")

    def start_simpleinterest_area(self):
        self.clear_screen()
        from simpleinterest_room import SimpleinterestRoom
        self.game.current_room = SimpleinterestRoom(self.game)

    def display_inventory(self):
        super().display_inventory()
        self.inventory_message.config(bg = "lightblue")
        
    def messages(self):
        super().messages()
        self.item_message.config(bg = "lightblue")

    def go_north(self):
        self.south_button.place_forget()
        self.north_button.place_forget()
        # set the message
        self.message.config(text =
        "As you go deeper into the forest to find the sage, you saw a magical deck of cards on a table.\n"
        "Then, a note on the table says after solving this challenge, you can move to the next room:\n"
        "Challenge: In this enchanted deck of 52 cards, what is the probability of drawing either a king or a heart (2.d.p)")
        self.message.place(x = 200, y = 590)

        self.answer.place(x = 390, y = 655)

        # set input for player's answer
        self.input_box.place(x = 450, y = 655, width = 80, height = 25)
            
        def check_north():
            player_answer = float(self.input_box.get())
            if player_answer == 0.31:
                self.message.config(text = "Correct! The answer is 0.31. You can now move to the next room.")
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Next room", command = self.start_simpleinterest_area)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Think about how many kings and hearts are in a deck.\n" 
                "Remember that one of the hearts is also a king.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_north)
        self.submit_button.place(x = 535, y = 655, width = 80, height = 25)

    def go_south(self):
        self.north_button.place_forget()
        self.south_button.place_forget()

        self.screen.config(bg = "lightblue")

        # change the image
        image = Image.open("Assets/key1.jpg")
        image = image.resize((850, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['key_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "lightblue")
        background_images.place(x = 100, y = 85)

        # set the message
        self.message.config(text = 
        "As you continue your journey through the forest, you found keys locked in a box inside a pond. The pond is clear and you can see fishes swimming in the pond.\n"
        "Then, a note on the side of the pond says after solving this challenge, you can unlock the box to collect the keys\n"
        "Challenge: In this mystical pond, there are 5 red fish, 7 blue fish, and 8 green fish. If you randomly catch one fish\n"
        "What is the probability that it will be either a red fish or a green fish?", font = ("Helvetica", 10))
        self.message.place(x = 75, y = 590)

        self.answer.place(x = 390, y = 663)

        # set input for player's answer
        self.input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_south():
            player_answer = float(self.input_box.get())
            if player_answer == 0.65:
                self.message.config(text = "Correct! The answer is 0.65. You have unlocked the box.")
                self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Collect keys", command = lambda: self.add_inventory("key", 12, self.start_simpleinterest_area))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Count the number of red fish and green fish in the pond.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_south)
        self.submit_button.place(x = 535, y = 663, width = 80, height = 25)

