from project.booths.booth import Booth


class PrivateBooth(Booth):
    PER_PERSON = 3.50

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * PrivateBooth.PER_PERSON
        self.is_reserved = True
