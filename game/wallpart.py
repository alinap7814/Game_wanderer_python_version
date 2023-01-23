from tkinter import NW
from brick import Brick
from checking_errors_path import error_checking_loading_wall


class WallPart(Brick):
    def __init__(self, canvas_board, x_coordinate, y_coordinate):
        super().__init__(canvas_board, "wall", x_coordinate, y_coordinate)
        self.loading_imaging_to_wall()
        self.create_wall()
        self.crossability = False

    def loading_imaging_to_wall(self):
        error_checking_loading_wall.load_image_of_wall(self)

    def create_wall(self):
        self.canvas.create_image(
            self.x_pos, self.y_pos, image=self.wall, anchor=NW, tag="wall")

