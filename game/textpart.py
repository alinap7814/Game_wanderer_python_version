from tkinter import CENTER, NW
from PIL import ImageTk


class TextPart:
    def __init__(self, canvas, hero, width, height, tile):
        self.canvas = canvas
        self.hero = hero
        self.height = height
        self.width = width
        self.num_name = 1
        self.first_tile = tile
        self.first_tile_load = ImageTk.PhotoImage(self.first_tile)

    def hero_info_printing_information(self):
        self.canvas.delete("hero_info", "fight_info")
        text_gen = (f"Hero (level {self.hero.level}) HP:{self.hero.max_health}/{self.hero.health} "
                    f"| DP:{self.hero.defend} | SP:{self.hero.strike} | KEY:{self.hero.key}")
        self.canvas.create_text(
            self.width/2,
            self.height-15,
            text=text_gen,
            fill="black",
            font="tkDefaultFont 24", tag="hero_info"
        )

    def fight_printing_information(self, monster):
        self.canvas.delete("hero_info", "fight_info")
        name = monster.type
        text_hero = (f"Hero (level {self.hero.level}) HP:{self.hero.max_health}/{self.hero.health} "
                     f"| DP:{self.hero.defend} | SP:{self.hero.strike}")
        text_enemy = (f"{name} HP:{monster.max_health}/{monster.health} "
                      f"| DP:{monster.defend} | SP:{monster.strike}")
        text_gen = text_hero + "   VS   " + text_enemy
        self.canvas.create_text(
            self.width/2,
            self.height-15,
            text=text_gen,
            fill="red",
            font="tkDefaultFont 12",
            tag="fight_info"
        )

    def printing_game_over(self):
        text_gen = "GAME OVER"
        self.canvas.create_rectangle(
            0, 0, self.width, self.height, fill="grey")
        self.canvas.create_text(
            self.width/2,
            self.height/2,
            text=text_gen,
            fill="white",
            font="tkDefaultFont 40", tag="game_over"
        )

    def printing_pass_information(self, sample, color="red"):
        tag_name = f"pr{self.num_name}"
        self.canvas.create_text(
            self.width/2,
            self.height/2,
            text=sample,
            fill=color,
            font="tkDefaultFont 20",
            tag=tag_name
        )
        self.canvas.after(500, self.move_up, tag_name)
        self.canvas.after(3500, self.delete_canvas_object, tag_name)
        self.num_name += 1

    def delete_canvas_object(self, what_del):
        self.canvas.delete(what_del)

    def move_up(self, what_move):
        x = 0
        y = -20
        self.canvas.move(what_move, x, y)
        self.canvas.after(1000, self.move_up, what_move)

    def new_level_create(self, level):
        self.canvas.create_rectangle(0, 0,
                                     self.width, self.height,
                                     fill="grey", tag="load")
        self.canvas.create_image(
            self.width/2, self.height/2, image=self.first_tile_load, anchor=CENTER, tag="load")
        self.canvas.create_text(self.width / 2, self.height / 2 + 100, anchor=CENTER,
                                text=f"Level {level}", fill="white",
                                font="tkDefaultFont 40", tag="load")
        self.canvas.after(3000, self.delete_canvas_object, "load")

    def print_points_information(self, points, color, position):
        tag_name = f"points{self.num_name}"
        width, height = position
        if color == "green":
            width += 40
        self.canvas.create_text(
            width,
            height,
            text=points,
            fill=color,
            font="tkDefaultFont 24",
            tag=tag_name,
            anchor=NW
        )
        self.canvas.after(1000, self.move_up, tag_name)
        self.canvas.after(2500, self.delete_canvas_object, tag_name)
        self.num_name += 1

