from random import randint


def calculate_attack(self, attacking_calculate, defender_calculate):
    self.canvas.unbind("<KeyPress>")
    random_number = randint(1, 6)
    strike_value = 2 * random_number + attacking_calculate.strike
    if strike_value > defender_calculate.defend:
        defender_calculate.health = defender_calculate.health - \
                                    (strike_value - defender_calculate.defend)
        if defender_calculate.type == "Hero":
            color = "red"
        else:
            color = "green"
        self.text.print_points_information(
            f"-{(strike_value - defender_calculate.defend)}",
            color,
            self.hero.return_x_or_y_position_in_game)
    self.text.fight_printing_information(self.enemy)

