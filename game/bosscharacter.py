from character import Character
from checking_errors_path import errors_path_for_boss


class BossCharacter(Character):
    def __init__(self, canvas, max_health, defend, strike):
        super().__init__(canvas, "Boss", max_health, defend, strike)
        self.boss = None
        self.image_boss = None
        self.boss_assets()
        self.image = self.boss

    def boss_assets(self):
        errors_path_for_boss.error_boss_assets(self)

