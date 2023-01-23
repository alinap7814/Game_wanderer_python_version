from PIL import Image, ImageTk


def load_image_of_wall(self):
    try:
        self.image_tile = Image.open("../pictures/wall.png")
        self.wall = ImageTk.PhotoImage(self.image_tile)
    except IOError as error:
        print(error)

