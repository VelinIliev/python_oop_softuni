from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert

mapper = {
    "Guitarist": lambda name, age: Guitarist(name, age),
    "Drummer": lambda name, age: Drummer(name, age),
    "Singer": lambda name, age: Singer(name, age),
}
skills_needed = {
    "Rock": {
        "Drummer": "play the drums with drumsticks",
        "Singer": "sing high pitch notes",
        "Guitarist": "play rock"
    },
    "Metal": {
        "Drummer": "play the drums with drumsticks",
        "Singer": "sing low pitch notes",
        "Guitarist": "play metal"
    },
    "Jazz": {
        "Drummer": "play the drums with drum brushes",
        "Singer": "sing low pitch notes",
        "Guitarist": "play jazz"
    }
}


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in mapper:
            raise ValueError("Invalid musician type!")

        if next(filter(lambda x: x.name == name, self.musicians), None):
            raise Exception(f'{name} is already a musician!')

        musician = mapper[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if next(filter(lambda x: x.name == name, self.bands), None):
            raise Exception(f'{name} band is already created!')

        band = Band(name)
        self.bands.append(band)

        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda x: x.place == place, self.concerts), None)

        if concert:
            raise Exception(f'{place} is already registered for {concert.genre} concert!')

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda x: x.name == musician_name, self.musicians), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next(filter(lambda x: x.name == band_name, self.bands), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next(filter(lambda x: x.name == band_name, self.bands), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda x: x.name == musician_name, band.members), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda x: x.name == band_name, self.bands), None)
        concert = next(filter(lambda x: x.place == concert_place, self.concerts), None)

        members = []
        for member in band.members:
            type_musician = member.__class__.__name__
            if type_musician not in members:
                members.append(type_musician)

        if len(members) != 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for member in band.members:
            type_musician = member.__class__.__name__
            if skills_needed[concert.genre][type_musician] not in member.skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}.'
