from project.booths.booth import Booth


class OpenBooth(Booth):
    PER_PERSON = 2.50

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * OpenBooth.PER_PERSON
        self.is_reserved = True

