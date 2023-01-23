from tkinter import NW
import random
from skeleton import Skeleton
from bosscharacter import BossCharacter


class Monsters:
    def __init__(self, canvas_main, level_floor_main, path_only_floor):
        self.canvas = canvas_main
        self.level_area = level_floor_main
        self.path_only = path_only_floor
        self.keep_skeletons = []
        self.boss = None

    @property
    def calculate_level_monster(self):
        chances = [self.level_area, self.level_area+1, self.level_area+2]
        random_indicate = random.choices(chances, weights=(50, 40, 10), k=1)
        return random_indicate[0]

    @property
    def return_list_with_monsters(self):
        list_positions = []
        try:
            if self.boss.check_character_is_alive() is True:
                list_positions.append(self.boss.return_x_or_y_position_in_game)
        except (ValueError, AttributeError):
            pass
        for obj in self.keep_skeletons:
            try:
                if obj.check_character_is_alive() is True:
                    list_positions.append(obj.return_x_or_y_position_in_game)
            except (ValueError, AttributeError):
                pass
        return list_positions

    def add_monsters_in_the_game(self, number):
        while number > 0:
            health_max = 2 * self.calculate_level_monster * random.randint(1, 6)
            defend = self.calculate_level_monster / 2 * random.randint(1, 6)
            strike = self.calculate_level_monster * random.randint(1, 6)
            skeleton = Skeleton(self.canvas, health_max, defend, strike, number)
            if number == 1:
                skeleton.key = True
            self.keep_skeletons.append(skeleton)
            number -= 1

    def add_boss_in_the_game(self):
        health_max = 2 * self.calculate_level_monster * random.randint(1, 6)
        defend = (self.calculate_level_monster / 2 * random.randint(1, 6)) + \
                 (random.randint(1, 6)/2)
        strike = self.calculate_level_monster * random.randint(1, 6) + self.calculate_level_monster
        self.boss = BossCharacter(self.canvas, health_max, defend, strike)

    def generate_first_monsters_in_the_game(self):
        floor_available = self.path_only[:]
        try:
            floor_available.remove([0, 0])
        except ValueError:
            pass
        for i in range(len(floor_available)):
            spots = random.sample(floor_available, len(self.keep_skeletons)+1)
        self.boss.x_pos = spots[0][0]
        self.boss.y_pos = spots[0][1]
        for_sk_spots = spots[1:]
        for num, skeleton in enumerate(self.keep_skeletons):
            skeleton.x_pos = for_sk_spots[num][0]
            skeleton.y_pos = for_sk_spots[num][1]
        self.canvas.after(3000, self.drawing_process)

    def drawing_process(self):
        try:
            if self.boss.check_character_is_alive() is True:
                self.canvas.create_image(
                    self.boss.x_pos, self.boss.y_pos, image=self.boss.image, anchor=NW, tag="boss")
        except (ValueError, AttributeError):
            pass
        for skeletons in self.keep_skeletons:
            try:
                if skeletons.check_character_is_alive() is True:
                    self.canvas.create_image(
                        skeletons.x_pos, skeletons.y_pos, image=skeletons.image, anchor=NW, tag="skeleton")
            except (ValueError, AttributeError):
                pass

