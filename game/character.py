class Character:
    def __init__(self, canvas_main, type_char, max_health, defend, strike):
        self.canvas = canvas_main
        self.type = type_char
        self.max_health = max_health
        self.health = max_health
        self.defend = defend
        self.strike = strike
        self.x_pos = 0
        self.y_pos = 0
        self.level = 1

    @property
    def return_x_or_y_position_in_game(self):
        return [self.x_pos, self.y_pos]

    @return_x_or_y_position_in_game.setter
    def set_position_in_game_from_list(self, position_pass):
        self.x_pos, self.y_pos = position_pass

    def check_character_is_alive(self):
        if self.health <= 0:
            return False
        return True

