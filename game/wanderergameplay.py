from tkinter import Tk, Canvas, CENTER
from PIL import Image
from level import Level
from checking_errors_path import calculate_step_with_check_error


class WandererGamePlay:
    def __init__(self):
        self.tile = Image.open("../pictures/floor.png")
        self.area_number = 1
        self.canvas = None
        self.step = None
        self.width = self.count_width()
        self.height = self.count_height()
        self.level = None
        self.hero = None
        self.text = None
        self.bind_key = None
        self.count_your_steps()
        self.start_game()

    def start_game(self):
        root = Tk()
        root.title("My wanderer game")
        screen_width = root.winfo_screenwidth()
        width_geometry = 722
        y_for_root = int((screen_width/2) - (width_geometry/2))
        root.geometry(f"{width_geometry}x752+{y_for_root}+10")
        root.resizable(False, False)
        root.configure(background='green')
        self.canvas = Canvas(root, width=self.width, height=self.height + 30, background="green")
        self.canvas.create_rectangle(0, 720, self.width, self.height+30, fill="white")
        self.canvas.pack(anchor=CENTER, expand=True)
        self.level = Level(self.canvas, self.step, self.tile)
        root.mainloop()

    def count_your_steps(self):
        calculate_step_with_check_error.step_count_error(self)

    def count_width(self):
        side = (self.tile.width * 10)
        return side

    def count_height(self):
        side = (self.tile.height * 10)
        return side


if __name__ == "__main__":
    game = WandererGamePlay()

