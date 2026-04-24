# import tkinter and image library to create graphic based game and load images
from PIL import Image, ImageTk
import tkinter as gui

# set game area
class Game:
    def __init__(self):        
        self.game_images = {}  # set up dictionary to store PhotoImage references
        self.inventory = {"treasure": 0, "key": 0, "map": 0, "final map": 0, "sage armour": 0}
        self.current_room = None
        
        #start the game
        self.screen = gui.Tk()
        self.screen.geometry("1050x730")
        self.screen.title("Graphic Based Adventure Game")
        self.screen.configure(bg = "pink")

        self.start_game()
        self.screen.mainloop()

    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    def start_game(self):
        # Load and show background image

        image = Image.open("Assets/startroom.png")
        image_resized = image.resize((880,500), Image.Resampling.LANCZOS)
        load_image = ImageTk.PhotoImage(image_resized)

        background_image = gui.Label(self.screen, image = load_image, bg = "pink")
        background_image.image = load_image
        background_image.place (x = 90, y = 20)
      
        # set up message
        game_message = """
        You heard stories about a legendary Sage hidden somewhere deep in the same forest you are living.
        However, you are living in a quiet village which is not deep in the forest. This sage is a master of magical mathematics. 
        It is said that anyone who finds him and passes all his challenges will have his mighty wisdom and powers. 
        Fueled by curiosity and the gifts promised after the adventure, you set out to find the Sage. 
        However, the forest is not an ordinary and simple one, it's enchanted and filled with areas that 
        test your knowledge and problem-solving skills. Click on Start game button to start the game.
        """

        message = gui.Label(self.screen, text = game_message, font = ("Helvetica", 11), bg = "pink", justify = "center")
        message.place(x= 110, y=530)

        # Start game button
        start_button = gui.Button(self.screen, text = "Start game", font=("Roboto", 14), command = self.start_trigonometry_area)
        start_button.place(x = 450, y = 400, width = 130, height = 50)
        
        #set up exit button
        self.exit_button = gui.Button(self.screen, text = "Exit game", font = ("Roboto", 10), command = self.screen.destroy)
        self.exit_button.place(x = 6, y = 340, width = 80, height = 35)

    def start_trigonometry_area(self):
        self.clear_screen()

        from trigonometry_room import TrigonometryRoom
        self.current_room = TrigonometryRoom(self)

    def go_to_start_room(self):
        self.clear_screen()
        self.start_game() 
        self.screen.config(bg = "pink")
        self.inventory = {"treasure": 0, "key": 0, "map": 0, "final map": 0, "sage armour": 0}

if __name__ == "__main__":
    Game()
