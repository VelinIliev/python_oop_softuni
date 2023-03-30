from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def train(self):
        if self.speed + 2 > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += 2
