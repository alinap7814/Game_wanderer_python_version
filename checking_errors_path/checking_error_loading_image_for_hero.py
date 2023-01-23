from PIL import Image, ImageTk


def loading_the_image_of_tile(self):
    try:
        self.image_hero_down = Image.open("../pictures/hero-down.png")
        self.hero_down = ImageTk.PhotoImage(self.image_hero_down)

        self.image_hero_go_up = Image.open("../pictures/hero-up.png")
        self.hero_up = ImageTk.PhotoImage(self.image_hero_go_up)

        self.image_hero_go_left = Image.open("../pictures/hero-left.png")
        self.hero_left = ImageTk.PhotoImage(self.image_hero_go_left)

        self.image_hero_go_right = Image.open("../pictures/hero-right.png")
        self.hero_right = ImageTk.PhotoImage(self.image_hero_go_right)
    except IOError as error:
        print(error)

