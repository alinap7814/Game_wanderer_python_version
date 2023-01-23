from PIL import Image, ImageTk


def error_boss_assets(self):
    try:
        self.image_boss = Image.open("../pictures/boss.png")
        self.boss = ImageTk.PhotoImage(self.image_boss)
    except IOError as error:
        print(error, "You got the error")
