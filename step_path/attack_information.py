def fight_with_monster(self):
    result = self.battle(self.hero, self.enemy)
    if result == "next level":
        self.text.delete_canvas_object("fight_information")
        self.hero.move = False
        self.canvas.unbind("<KeyPress>")
        self.floor = None
        self.level += 1
        self.restore_hero()
        self.create_new_level()

    elif result == "kill_death":
        self.canvas.bind("<KeyPress>", self.attack_monster)
        self.canvas.focus_set()
        self.text.delete_canvas_object("fight_information")
        self.text.hero_info_printing_information()
        self.hero.move = True
        self.enemy = False
        self.canvas.bind("<KeyPress>", self.user_input)
        self.canvas.focus_set()

    elif result == "counter_result":
        result_monster = self.battle(self.enemy, self.hero)

        if result_monster == "information_attack_result":
            self.canvas.bind("<KeyPress>", self.attack_monster)
            self.canvas.focus_set()
            self.text.printing_pass_information("You can attack!")

        elif result_monster == "dead_result":
            self.text.delete_canvas_object("fight_info")
            self.hero.move = False
            self.canvas.unbind("<Keypress")
            self.canvas.delete("hero", "wall", "path", "skeleton", "boss")
            del self.floor
            del self.hero
            self.text.printing_game_over()

