class Brick:
    def __init__(self, canvas_board, type_of_brick, x_coordinate, y_coordinate):
        try:
            if not isinstance(x_coordinate, int) or not isinstance(y_coordinate, int):
                raise TypeError("Coordinate should be integers")
        except ValueError:
            print("Argument 'coordinates' should be list with two integers.")
        self.x_pos = x_coordinate
        self.y_pos = y_coordinate
        self.canvas = canvas_board
        self.type = type_of_brick
        if self.type == "path":
            self.crossability = True
        elif self.type == "wall":
            self.crossability = False
        else:
            raise ValueError("Type of brick could be 'path' or 'wall'.")

    def get_x_position(self):
        return self.x_pos

    def get_y_position(self):
        return self.y_pos

