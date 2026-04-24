# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui
from differentiation_room import differentiation_area
from inventory import inventory

# set trigonometry area
def probability_area(screen, clear_screen):
    clear_screen()

    # set background colour
    screen.configure(bg = "lightblue") # set the background colour

    # load the background image
    image_two = Image.open("Assets/img5.jpg") 
    image_resize = image_two.resize((740, 500), Image.Resampling.LANCZOS)  # resize image on the screen
    load_imagetwo = ImageTk.PhotoImage(image_resize)  # convert the image to PhotoImage format

    # set the background image
    background_images = gui.Label(screen, image = load_imagetwo, bg = "lightblue")
    background_images.image = load_imagetwo # keep a reference to avoid garbage collection
    background_images.place(x = 125, y = 80) # set the position of the image

    message = gui.Label(screen, text = "", font = ("Helvetica", 11), bg = "lightblue", fg = "black", justify = "center")
    # message.place(x = 55, y = 530)

    input_box = gui.Entry(screen, font = ("Helvetica", 10), fg = "black")

    submit_button = gui.Button(screen, text ="Submit", font=("Roboto", 10))

    answer = gui.Label(screen, text = "Answer:", font = ("Helvetica", 11), bg = "lightblue", fg = "black", justify = "center")

    def go_north():
        south_button.place_forget()
        north_button.place(x = 450)
        # set the message
        message.config(text =
        "As you go deeper into the forest to find the sage, you saw a magical deck of cards on a table.\n"
        "Then, a note on the table says after solving this challenge, you can move to the next room:\n"
        "Challenge: In this enchanted deck of 52 cards, what is the probability of drawing either a king or a heart (2.d.p)")
        message.place(x = 140, y = 590)

        answer.place(x = 390, y = 655)

        # set input for player's answer
        input_box.place(x = 450, y = 655, width = 80, height = 25)
            
        def check_north():
            player_answer = float(input_box.get())
            if player_answer == 0.31:
                message.config(text = "Correct! The answer is 0.31. You can now move to the next room.")
                message.place(x = 280, y = 590)
                answer.place_forget()
                input_box.place_forget()
                submit_button.config(text = "Next room", command = start_differentiation_area)
            elif player_answer <= 0:
                message.config(text = "Please enter a positive number.")
                message.place(x = 280, y = 590)
            else:
                message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Think about how many kings and hearts are in a deck.\n" 
                "Remember that one of the hearts is also a king.")
                message.place(x = 150, y = 590)

        # set submit button
        submit_button.config(command = check_north)
        submit_button.place(x = 535, y = 655, width = 80, height = 25)
    
    def start_differentiation_area():
            differentiation_area(screen, clear_screen)

    def go_south():
        north_button.place_forget()
        south_button.place(x = 450)

        # set the message
        image_two = Image.open("Assets/key1.jpg")
        image_resize = image_two.resize((740, 500), Image.Resampling.LANCZOS) 
        load_imagetwo = ImageTk.PhotoImage(image_resize)

        screen.config(bg = "#ADD8E6")
        background_images = gui.Label(screen, image = load_imagetwo, bg = "#ADD8E6")
        background_images.image = load_imagetwo
        background_images.place(x = 125, y = 80)

        # set the message
        message.config(text = 
        "As you continue your journey through the forest, you found two keys locked in a box inside a pond. The pond is clear and you can see fishes swimming in the pond.\n"
        "Then, a note on the side of the pond says after solving this challenge, you can unlock the box to collect the keys\n"
        "Challenge: In this mystical pond, there are 5 red fish, 7 blue fish, and 8 green fish. If you randomly catch one fish\n"
        "What is the probability that it will be either a red fish or a green fish?", font = ("Helvetica", 10))
        message.place(x = 35, y = 590)

        answer.place(x = 390, y = 663)

        # set input for player's answer
        input_box.place(x = 450, y = 663, width = 80, height = 25)
            
        def check_south():
            player_answer = float(input_box.get())
            if player_answer == 0.65:
                message.config(text = "Correct! The answer is 0.65. You have unlocked the key.")
                message.place(x = 280, y = 590)
                answer.place_forget()
                input_box.place_forget()
                submit_button.config(text = "Collect key", command = lambda: add_inventory("key", 2))
            elif player_answer <= 0:
                message.config(text = "Please enter a positive number.")
                message.place(x = 280, y = 590)
            else:
                message.config(text = "Incorrect answer! Try again.\n"
                "Hint: Count the number of red fish and green fish in the pond.")
                message.place(x = 280, y = 590)

        # set submit button
        submit_button.config(command = check_south)
        submit_button.place(x = 535, y = 663, width = 80, height = 25)

    # set up north button
    north_button = gui.Button(screen, text ="Go north", font=("Roboto", 10), command = go_north)
    north_button.place(x = 390, y = 20, width = 90, height = 35) 

    # set up south button
    south_button = gui.Button(screen, text ="Go south", font=("Roboto", 10), command = go_south)
    south_button.place(x = 515, y = 20, width = 90, height = 35) 
