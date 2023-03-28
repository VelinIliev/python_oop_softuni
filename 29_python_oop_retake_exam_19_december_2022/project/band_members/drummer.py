from project.band_members.musician import Musician


class Drummer(Musician):

    @property
    def possible_skills(self):
        return ['play the drums with drumsticks', 'play the drums with drum brushes', 'read sheet music']
