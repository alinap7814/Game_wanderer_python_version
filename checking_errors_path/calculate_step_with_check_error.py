def step_count_error(self):
    if self.tile.width == self.tile.height:
        self.step = self.tile.width
    else:
        raise ValueError("Picture must be square!")

