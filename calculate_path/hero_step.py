from random import choices, randint
from game.hero import Hero


def add_firts_hero(self):
    health = 20 + (3 * randint(1, 6))
    defeat = 2 * randint(1, 6)
    strike = 5 + randint(1, 6)
    self.hero = Hero(self.canvas, health, defeat, strike)


def starting_new_level_with_hero(self):
    chances = [self.hero.max_health,
               int(self.hero.max_health / 3),
               int(self.hero.max_health / 100 * 10)]
    random_chance = choices(chances, weights=(10, 40, 50), k=1)
    self.hero.health += random_chance[0]
    if self.hero.health > self.hero.max_health:
        self.hero.health = self.hero.max_health
    self.hero.level = self.level
    self.hero.return_x_or_y_position_in_game = [0, 0]
    self.hero.move = True
    self.hero.kill_boss = False
    self.hero.key = False
    self.hero.image = self.hero.hero_down
    self.enemy = None

