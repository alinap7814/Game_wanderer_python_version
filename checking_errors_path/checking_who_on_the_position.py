def check_position_enemy(self):
    try:
        if self.floor.monsters.boss.return_x_or_y_position_in_game is not False:
            boss_position = self.floor.monsters.boss.return_x_or_y_position_in_game
            if boss_position == self.hero.return_x_or_y_position_in_game:
                self.enemy = self.floor.monsters.boss
    except AttributeError:
        pass

    for number, skeleton in enumerate(self.floor.monsters.keep_skeletons):
        if skeleton.return_x_or_y_position_in_game == self.hero.return_x_or_y_position_in_game:
            self.enemy = self.floor.monsters.keep_skeletons[number]
    self.text.fight_printing_information(self.enemy)


def check_position_monster(self):
    monster = self.floor.monsters.return_list_with_monsters
    if self.hero.return_x_or_y_position_in_game not in monster:
        pass
    elif self.hero.return_x_or_y_position_in_game in monster:
        self.canvas.bind("<KeyPress>", self.attack_monster)
        self.canvas.focus_set()
        self.text.delete_canvas_object("hero_info")
        self.hero.move = False
        self.check_enemy()


