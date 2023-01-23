from floor import Floor
from textpart import TextPart
from checking_errors_path import checking_who_on_the_position
from calculate_path import count__points_attack
from calculate_path import hero_step
from step_path import attack_information


class Level:
    def __init__(self, canvas_main, step_main, tile):
        self.text = None
        self.canvas = canvas_main
        self.level = 1
        self.step = step_main
        self.width = self.step * 10
        self.height = self.step * 10
        self.first_tile = tile
        self.hero = None
        self.floor = None
        self.hero_act = None
        self.create_first_level_for_start()
        self.monsters = None
        self.bind_key = None
        self.enemy = None

    def create_first_level_for_start(self):
        self.level = 1
        self.add_hero()
        self.text = TextPart(self.canvas, self.hero, self.width, self.height + 30, self.first_tile)
        self.create_new_level()

    def create_new_level(self):
        self.canvas.delete("skeleton", "path", "wall", "hero")
        self.floor = Floor(self.canvas, self.step*10, self.step*10, self.level, self.step)
        self.text.new_level_create(self.level)
        self.canvas.after(3000, self.hero.draw_the_hero)
        self.canvas.after(3000, self.text.hero_info_printing_information)
        self.canvas.after(3000, self.user_input_move_hero)

    def user_input_move_hero(self):
        self.canvas.bind("<KeyPress>", self.user_input)
        self.canvas.focus_set()

    def user_input(self, enter):
        if self.floor is False:
            self.canvas.unbind("<Keypress>")
        if self.hero.move is False:
            self.text.printing_pass_information("Fight! You can't run away!")
        elif enter.keycode in (38, 87):
            self.hero.image = self.hero.hero_up
            if self.hero.y_pos - self.step >= 0:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos - self.step):
                    self.hero.y_pos = self.hero.y_pos - self.step
        elif enter.keycode in (40, 83):
            self.hero.image = self.hero.hero_down
            if self.hero.y_pos + self.step <= self.height - self.step:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos + self.step):
                    self.hero.y_pos = self.hero.y_pos + self.step
        elif enter.keycode in (39, 68):
            self.hero.image = self.hero.hero_right
            if self.hero.x_pos + self.step <= self.width - self.step:
                if self.floor.check_cross(self.hero.x_pos + self.step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos + self.step
        elif enter.keycode in (37, 65):
            self.hero.image = self.hero.hero_left
            if self.hero.x_pos - self.step >= 0:
                if self.floor.check_cross(self.hero.x_pos - self.step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos - self.step
        self.canvas.delete("hero")
        self.hero.draw_the_hero()
        self.check_monster()

    def check_monster(self):
        checking_who_on_the_position.check_position_monster(self)

    def check_enemy(self):
        checking_who_on_the_position.check_position_enemy(self)

    def attack_monster(self, enter):
        if enter.keycode == 32:
            if self.enemy is not None:
                self.start_fight_with_monster()

    def start_fight_with_monster(self):
        attack_information.fight_with_monster(self)

    def calculate_points(self):
        count__points_attack.calculate_attack(self, attacking_calculate=0, defender_calculate=0)

    def battle(self, defender_calculate):
        self.calculate_points()
        if defender_calculate.type == "Hero":
            if defender_calculate.check_character_is_alive() is False:
                return "_dead_"
            return "attack_battle"
        if defender_calculate.type != "Hero":
            if defender_calculate.check_character_is_alive() is True:
                return "counter_hero_attack"
            if defender_calculate.check_character_is_alive() is False:
                if defender_calculate.type == "Boss":
                    if self.hero.key is True:
                        return "next_attack"
                    self.hero.kill_boss = True
                    self.canvas.delete("boss")
                    self.floor.monsters.boss = False
                    return "kill_monster"
                if defender_calculate.type == "Skeleton":
                    if defender_calculate.key is True:
                        self.hero.key = True
                        if self.hero.kill_boss is True:
                            return "next"
                    self.canvas.delete("skeleton")
                    self.floor.monsters.drawing_process()
                    for num, obj in enumerate(self.floor.monsters.keep_skeletons):
                        if obj == defender_calculate:
                            del self.floor.monsters.keep_skeletons[num]
                    return "kill_the_boss"

    def add_hero(self):
        hero_step.add_firts_hero(self)

    def restore_hero(self):
        hero_step.starting_new_level_with_hero(self)

