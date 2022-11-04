from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type_):
        found_horse = next(filter(lambda x: (type(x).__name__ == horse_type_ and not x.is_taken), reversed(self.horses)), None)
        if not found_horse:
            raise Exception(f'Horse breed {horse_type_} could not be found!')
        return found_horse

    def find_jockey(self, jockey_name_):
        found_jockey = next(filter(lambda x: (x.name == jockey_name_), self.jockeys), None)
        if not found_jockey:
            raise Exception(f'Jockey {jockey_name_} could not be found!')
        return found_jockey

    def find_race(self, race_type_):
        found_race = next(filter(lambda x: x.race_type == race_type_, self.horse_races), None)
        if not found_race:
            raise Exception(f'Race {race_type_} could not be found!')
        return found_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f'Horse {horse_name} has been already added!')

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f'Jockey {jockey_name} has been already added!')
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f'Race {race_type} has been already created!')
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = self.find_jockey(jockey_name)
        current_horse = self.find_horse(horse_type)

        if current_jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'
        else:
            current_jockey.horse = current_horse
            current_horse.is_taken = True
            return f'Jockey {jockey_name} will ride the horse {current_horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        current_race = self.find_race(race_type)
        current_jockey = self.find_jockey(jockey_name)

        if not current_jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if current_jockey in current_race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        else:
            current_race.jockeys.append(current_jockey)
            return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):
        current_race = None
        for race in self.horse_races:
            if race.race_type == race_type:
                current_race = race
        if not current_race:
            raise Exception(f'Race {race_type} could not be found!')
        if len(current_race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')
        high_speed = 0
        winner = None
        for jockey in current_race.jockeys:
            if jockey.horse.speed > high_speed:
                high_speed = jockey.horse.speed
                winner = jockey
        return f"The winner of the {race_type} race, with a speed of {high_speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."
