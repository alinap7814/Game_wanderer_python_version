from PIL import Image, ImageTk
from character import Character


class Skeleton(Character):
    def __init__(self, canvas, max_health, defend, strike, num):
        super().__init__(canvas, "Skeleton", max_health, defend, strike)
        self.load_assets()
        self.image = self.skeleton
        self.key = False
        self.number = num

    def load_assets(self):
        try:
            self.img_skeleton = Image.open("../pictures/skeleton.png")
            self.skeleton = ImageTk.PhotoImage(self.img_skeleton)
        except IOError as error:
            print(error)

