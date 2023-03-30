from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey

horse_mapper = {
    "Appaloosa": lambda name, speed: Appaloosa(name, speed),
    "Thoroughbred": lambda name, speed: Thoroughbred(name, speed)
}


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        horse = next(filter(lambda x: x.name == horse_name, self.horses), None)

        if horse:
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in horse_mapper:
            new_horse = horse_mapper[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {new_horse.name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

        if jockey:
            raise Exception(f'Jockey {jockey_name} has been already added!')

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f'Jockey {new_jockey.name} is added.'

    def create_horse_race(self, race_type: str):

        race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

        if race:
            raise Exception(f'Race {race_type} has been already created!')

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f'Race {new_race.race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        horse = next(filter(lambda x: x.__class__.__name__ == horse_type and x.is_taken == False, self.horses[::-1]),
                     None)

        if not horse:
            raise Exception(f'Horse breed {horse_type} could not be found!')

        if jockey.horse:
            return f'Jockey {jockey.name} already has a horse.'

        jockey.horse = horse
        horse.is_taken = True

        return f'Jockey {jockey.name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f'Race {race_type} could not be found!')

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not jockey.horse:
            raise Exception(f'Jockey {jockey.name} cannot race without a horse!')

        if jockey in race.jockeys:
            return f'Jockey {jockey.name} has been already added to the {race.race_type} race.'

        race.jockeys.append(jockey)

        return f'Jockey {jockey.name} added to the {race.race_type} race.'

    def start_horse_race(self, race_type: str):

        race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f'Race {race_type} could not be found!')

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner = None
        winner_speed = 0
        for jockey in race.jockeys:
            if jockey.horse.speed > winner_speed:
                winner_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
