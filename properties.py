import tkinter as gui
from PIL import Image, ImageTk

class Properties:
    def __init__(self, manage_game):
        self.game = manage_game
        self.screen = manage_game.screen

        self.buttons()
        self.messages()
        # self.display_inventory()

    def buttons(self):
        # set up north button
        self.north_button = gui.Button(self.screen, text ="Go north", font=("Roboto", 10), command = self.go_north)
        self.north_button.place(x = 250, y = 40, width = 90, height = 35) 

        # set up south button
        self.south_button = gui.Button(self.screen, text ="Go south", font=("Roboto", 10), command = self.go_south)
        self.south_button.place(x = 400, y = 40, width = 90, height = 35) 

        # set up east button
        self.east_button = gui.Button(self.screen, text ="Go east", font=("Roboto", 10), command = self.go_east)
        self.east_button.place(x = 550, y = 40, width = 90, height = 35) 

        # set up west button
        self.west_button = gui.Button(self.screen, text ="Go west", font=("Roboto", 10), command = self.go_west)
        self.west_button.place(x = 700, y = 40, width = 90, height = 35)         

        # set up help button
        self.help_button = gui.Button(self.screen, text = "Help", font = ("Roboto", 10), command = self.help_button)
        self.help_button.place(x = 10, y = 300, width = 80, height = 35)

        #set up inventory button
        self.inventory_button = gui.Button(self.screen, text = "Inventory", font = ("Roboto", 10), command = self.display_inventory)
        
        #set up exit button
        self.exit_button = gui.Button(self.screen, text = "Exit game", font = ("Roboto", 10), command = self.screen.destroy)

        #set up restart button
        self.restart_button = gui.Button(self.screen, text ="Restart", font = ("Roboto", 10), command = self.game.go_to_start_room)

        #set up submit button
        self.submit_button = gui.Button(self.screen, text ="Submit", font=("Roboto", 10))
        
    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    def help_button(self):
        if self.inventory_button.winfo_ismapped():
            self.hide_help_buttons()
        else:
            self.show_help_buttons()

    def show_help_buttons(self):
        self.inventory_button.place(x = 10, y = 340, width = 80, height = 35)
        self.exit_button.place(x = 10, y = 380, width = 80, height = 35)
        self.restart_button.place(x= 10, y = 420, width = 80, height = 35)

    def hide_help_buttons(self):
        self.inventory_button.place_forget()
        self.exit_button.place_forget()
        self.restart_button.place_forget()

    def messages(self):
        self.inventory_text = None
        self.message = gui.Label(self.screen, text = "#D8BFD8", font = ("Helvetica", 11), bg = "#D8BFD8", justify = "center")
        self.item_message = gui.Label(self.screen, font = ("Helvetica", 11, "bold"), justify = "center")
        self.input_box = gui.Entry(self.screen, font = ("Helvetica", 10))
        self.answer = gui.Label(self.screen, text = "Answer:", font = ("Helvetica", 11), bg = "#D8BFD8", justify = "center")

    def display_inventory(self):
        inventory_text = ", ".join([f"{item}: {qty}" for item, qty in self.game.inventory.items()])
        self.inventory_message = gui.Label(self.screen, text = f"Inventory: {inventory_text}", bg = "#D8BFD8", font = ("Helvetica", 10))
        self.inventory_message.place(x = 5, y = 1)

    def add_inventory(self, item, number, next_room = None):
        self.game.inventory[item] = self.game.inventory.get(item, 0) + number

        self.item_message.place(x = 360, y = 600)
        self.item_message.config(text = f"You have {number} {item}(s)")

        self.message.place(x = 360, y = 620)
        self.message.config(text = "You can now move to the next room.")

        self.submit_button.config(text = "Next room", command = next_room) 
        self.submit_button.place(x = 500, y = 650, width = 80, height = 25)

        # self.display_inventory()

    def use_inventory(self, item, number, next_room = None, alternative_room = None):
        if item in self.game.inventory and self.game.inventory[item] >= number :
            self.game.inventory[item] -= number
            self.item_message.place(x = 360, y = 600)
            self.item_message.config(text = f"You have used {number} {item}")
            self.message.config(text = "You can now move to the next room.")

            self.submit_button.config(text = "Next room", command = next_room) 
            self.submit_button.place(x = 500, y = 650, width = 80, height = 25) 
        else:
            self.item_message.place(x = 360, y = 600)
            self.item_message.config(text = f"You do not have {number} {item} to use")
            self.message.config(text = "You can now move to the next room and continue your journey.")

            self.submit_button.config(text = "Next room", command = alternative_room) 
            self.submit_button.place(x = 500, y = 650, width = 80, height = 25)

        # self.display_inventory()

    def go_north(self):
        raise NotImplementedError("Implemented by child class")
    
    def go_south(self):
        raise NotImplementedError("Implemented by child class")
    
    def go_east(self):
        raise NotImplementedError("Implemented by child class")
    
    def go_west(self):
        raise NotImplementedError("Implemented by child class")