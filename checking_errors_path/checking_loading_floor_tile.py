from PIL import Image, ImageTk


def loading_image_tile_in_game(self):
    try:
        self.image_tile = Image.open("../pictures/floor.png")
        self.tile = ImageTk.PhotoImage(self.image_tile)
    except IOError as error:
        print(error)

