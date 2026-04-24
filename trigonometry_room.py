import tkinter as gui
from PIL import Image, ImageTk
from properties import Properties

# set trigonometry area
class TrigonometryRoom(Properties):
    def __init__(self, manage_game):
        self.game = manage_game
        self.screen = manage_game.screen
        
        self.screen.configure(bg = "#D8BFD8")
        image = Image.open("Assets/trigonometryroom.png") 
        image = image.resize((850, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        # store PhotoImage reference
        self.game.game_images['trigonometry_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)
        
        super().__init__(manage_game)
    
        self.trigonometry()

    def trigonometry(self):  
        self.message.config(text ="You need to click on either north, west, east or south", font=("Roboto", 10))
        self.message.place(x = 350, y = 15)
        pass      
        #empty not needed
        
    def start_probability_area(self):
        self.clear_screen()
        from probability_room import ProbabilityRoom
        self.game.current_room = ProbabilityRoom(self.game)

    def go_north(self):
        self.south_button.place_forget()
        self.west_button.place_forget()
        self.east_button.place_forget()
        self.north_button.place_forget()
        # set the message
        self.message.config(text =
        "The Sage has left an ancient map that contains a trigonometry puzzle. You need to solve this challenge to move to the next room.\n"
        "Challenge: The shadow of a tree forms one side of a right triangle, measuring 24 meters.\n"
        "The distance from the top of the tree to the end of the shadow (the hypotenuse) is 30 meters.\n"
        "How tall is the tree?")
        self.message.place(x = 145, y = 590)

        self.answer.place(x = 390, y = 663)

        # set input for player's answer
        self.input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_north():
            player_answer = int(self.input_box.get())
            if player_answer == 18:
                self.message.config(text = "Correct! The tree is 18 metres tall. You can now move to the next room.")
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Next room", command = self.start_probability_area)
                self.submit_button.place(x = 500, y = 630)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: The Sage's map shows a right triangle.\n" 
                "Remember, the height of the tree is the other side of the triangle which is the one opposite to the shadow.")
                self.message.place(x = 28, y = 590)

        # set submit button
        self.submit_button.config(command = check_north)
        self.submit_button.place(x = 535, y = 663, width = 80, height = 25)

    def go_south(self):
        self.north_button.place_forget()
        self.west_button.place_forget()
        self.east_button.place_forget()
        self.south_button.place_forget()
        # set the message
        self.message.config(text = 
        "The Sage left a diagram of a triangle with different angles, one of which is missing.\n"
        "You have to find the missing angle to move to the next room.\n"
        "Challenge: The Sage has drawn a triangle where one angle is 50° and another is 60°.\n "
        "Calculate the missing angle? ")
        self.message.place(x = 255, y = 590)

        self.answer.place(x = 390, y = 663)

        # set input for player's answer
        self.input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_south():
            player_answer = int(self.input_box.get())
            if player_answer == 70:
                self.message.config(text = "Correct! The missing angle is 70°. You can now move to the next room.")
                self.message.place(x = 280, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Next room", command = self.start_probability_area)
                self.submit_button.place(x = 500, y = 630)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: The sum of all angles in a triangle is always 180°.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_south)
        self.submit_button.place(x = 535, y = 663, width = 80, height = 25)

    def go_east(self):
        self.south_button.place_forget()
        self.west_button.place_forget()
        self.north_button.place_forget()
        self.east_button.place_forget()

        # change the image
        image = Image.open("Assets/treasure.png")
        image = image.resize((880, 500), Image.Resampling.LANCZOS) 
        picture = ImageTk.PhotoImage(image)

        self.game.game_images['treasure_pic'] = picture
        background_images = gui.Label(self.screen, image = picture, bg = "#D8BFD8")
        background_images.place(x = 100, y = 85)

        self.message.config(text = "You found a treasure chest left by the Sage, but it's locked with a trigonometry puzzle.\n" 
        "The Sage has hidden clues at the top of an high cliff. You need to calculate the height of the cliff to move to the next room.\n"
        "Challenge: A cliff casts a shadow of 40 meters on the ground, and the angle between the shadow and the ground is 60°.\n"
        "What is the height of the cliff (2.d.p)?")
        self.message.place(x = 185, y = 590)

        self.answer.place(x = 415, y = 660)

        # set input for player's answer
        self.input_box.place(x = 475, y = 660, width = 80, height = 25)

        def check_east():
            player_answer = float(self.input_box.get())
            if player_answer == 69.28:
                self.message.config(text = "Correct! The height of the cliff is 69.28 meters. You have unlocked the teasure chest.")
                # self.screen.after(2000, lambda: self.message.winfo_exists() and self.message.place_forget())
                self.message.place(x = 250, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.place(x = 520, y = 630, width = 100, height = 30)
                self.submit_button.config(text = "Collect treasure", command = lambda: self.add_inventory("treasure", 5, self.start_probability_area))
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "The shadow on the ground is the adjacent side (40m).\n" 
                "The height of the cliff is the opposite side of the triangle.")
                self.message.place(x = 280, y = 590)

        # set submit button
        self.submit_button.config(command = check_east, text = "Submit")
        # self.submit_button.place_forget()
        self.submit_button.place(x = 560, y = 660, width = 80, height = 25)

    def go_west(self):
        # set the message
        self.south_button.place_forget()
        self.east_button.place_forget()
        self.north_button.place_forget()
        self.west_button.place_forget()

        self.message.config(text = 
        "A magical compass shows the direction to the Sage's treasure, but you need to calculate the distance.\n"
        "Problem: The Sage is located at a bearing of 110° from your current position.\n"
        "You walk 50 meters east, and the Sage is now due south of you. How far are you from the Sage (2.d.p)?")
        self.message.place(x = 220, y = 590)

        self.answer.place(x = 395, y = 650)

        # set input for player's answer
        self.input_box.place(x = 455, y = 650, width = 80, height = 25)
            
        def check_west():
            player_answer = float(self.input_box.get())
            if player_answer == 46.99:
                self.message.config(text = "Correct! The distance to the Sage is 46.99 meters. You can now move to the next room.")
                self.message.place(x = 250, y = 590)
                self.answer.place_forget()
                self.input_box.place_forget()
                self.submit_button.config(text = "Next room", command = self.start_probability_area)
                self.submit_button.place(x = 500, y = 630)
            elif player_answer <= 0:
                self.message.config(text = "Please enter a positive number.")
                self.message.place(x = 280, y = 590)
            else:
                self.message.config(text = "Incorrect answer! Try again.\n"
                "Hint: The magical compass creates a triangle. You've walked 50 meters east which is one side of the triangle\n" 
                "adjacent to the angle at your starting point. The Sage is directly south of you which makes the path to the Sage the triangle's hypotenuse.")
                self.message.place(x = 60, y = 590)

        # set submit button
        self.submit_button.config(command = check_west, text = "Submit")
        # self.submit_button.place_forget()
        self.submit_button.place(x = 545, y = 650, width = 80, height = 25) 