from tkinter import NW
from brick import Brick
from checking_errors_path import checking_loading_floor_tile


class Path(Brick):
    def __init__(self, canvas_board, x_coordinate, y_coordinate):
        super().__init__(canvas_board, "path", x_coordinate, y_coordinate)
        self.loading_floor_tile_in_game()
        self.create_tile_in_game()
        self.monster = False

    def loading_floor_tile_in_game(self):
        checking_loading_floor_tile.loading_image_tile_in_game(self)

    def create_tile_in_game(self):
        self.canvas.create_image(
            self.x_pos, self.y_pos, image=self.tile, anchor=NW, tag="path")