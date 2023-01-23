from tkinter import NW
from character import Character
from checking_errors_path import checking_error_loading_image_for_hero


class Hero(Character):
    def __init__(self, canvas, max_health, defend, strike):
        super().__init__(canvas, "Hero", max_health, defend, strike)
        self.img_hero_down = None
        self.hero_down = None
        self.loading_tile_image()
        self.image = self.hero_down
        self.key = False
        self.kill_boss = False
        self.move = True

    def loading_tile_image(self):
        checking_error_loading_image_for_hero.loading_the_image_of_tile(self)

    def draw_the_hero(self):
        if self.health > 0:
            self.canvas.create_image(
                self.x_pos, self.y_pos, image=self.image, anchor=NW, tag="hero")

