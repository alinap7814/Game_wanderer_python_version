from path import Path
from wallpart import WallPart
from monster import Monsters


class Floor:
    def __init__(self, canvas_main, width_floor_main, height_floor_main, level_main, step_main):
        self.level = level_main
        self.canvas = canvas_main
        self.width_floor = width_floor_main
        self.height_floor = height_floor_main
        self.step = step_main
        self.keep_floor = {}
        self.monsters = None
        self.path_only = None
        self.initial_map()

    def initial_map(self):
        self.generation_floor()
        self.map_of_the_walls()
        self.path_only = self.get_path_position()
        self.monsters = Monsters(self.canvas, self.level, self.path_only)
        self.monsters.add_monsters_in_the_game(5)
        self.monsters.add_boss_in_the_game()
        self.monsters.generate_first_monsters_in_the_game()

    def get_path_position(self):
        path_position = []
        for value in self.keep_floor.values():
            for each_obj in value.values():
                if each_obj.type == "path":
                    x_number = each_obj.get_x_position()
                    y_number = each_obj.get_y_position()
                    path_position.append([x_number, y_number])
        return path_position

    def generation_floor(self):
        y_position = 0
        while y_position < self.height_floor:
            self.keep_floor[y_position] = {}
            x_position = 0
            while x_position < self.width_floor:
                tile = Path(self.canvas, x_position, y_position)
                new_pair = {x_position: tile}
                self.keep_floor[y_position].update(new_pair)
                x_position += self.step
            y_position += self.step

    def add_wall_to_the_floor(self, raw, column):
        self.keep_floor[raw][column] = WallPart(self.canvas, column, raw)

    def map_of_the_walls(self):
        list_wall = [
            [1, 4], [2, 4], [2, 6], [2, 8], [2, 9],
            [3, 2], [3, 3], [3, 4], [3, 6],
            [3, 8], [3, 9], [4, 6], [5, 1], [5, 2],
            [5, 3], [5, 4], [5, 6], [5, 7],
            [5, 8], [5, 9], [6, 2], [6, 4], [7, 2],
            [7, 4], [7, 6], [7, 7], [7, 9],
            [8, 6], [8, 7], [8, 9], [9, 2], [9, 3],
            [9, 4], [9, 9], [10, 4], [10, 6], [10, 7]
        ]
        for element in list_wall:
            row, col = element
            row_cor = (row * self.step) - self.step
            col_cor = (col * self.step) - self.step
            self.add_wall_to_the_floor(row_cor, col_cor)

    def check_cross(self, x_f, y_f):
        obj = [x_f, y_f]
        path = self.path_only
        if obj in path:
            return True
        else:
            return False

