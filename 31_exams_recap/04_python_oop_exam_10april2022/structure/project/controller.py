class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_sustenance(self, sustenance_type):

        found = None
        index = None

        for i, supply in enumerate(self.supplies[::-1]):
            if supply.__class__.__name__ == sustenance_type:
                found = supply
                index = -(i + 1)
                break

        if found:
            self.supplies.pop(index)

        return found

    def add_player(self, *players):

        added_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f'Successfully added: {", ".join(added_players)}'

    def add_supply(self, *supplies):

        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):

        player = next(filter(lambda x: x.name == player_name, self.players), None)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type in ["Food", "Drink"]:

            sustenance = self.find_sustenance(sustenance_type)

            if not sustenance:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            if player.stamina + sustenance.energy > 100:
                player.stamina = 100
            else:
                player.stamina += sustenance.energy

            return f'{player_name} sustained successfully with {sustenance.name}.'

    def duel(self, first_player_name: str, second_player_name: str):

        player1 = next(filter(lambda x: x.name == first_player_name, self.players), None)
        player2 = next(filter(lambda x: x.name == second_player_name, self.players), None)

        not_enough = []
        for player in [player1, player2]:
            if player.stamina == 0:
                not_enough.append(f'Player {player.name} does not have enough stamina.')

        if not_enough:
            return "\n".join(not_enough)

        winner = None

        if player1.stamina > player2.stamina:
            player1, player2 = player2, player1

        player2.stamina -= player1.stamina / 2

        if player1.stamina - player2.stamina / 2 < 0:
            player1.stamina = 0
            winner = player2
        else:
            player1.stamina -= player2.stamina / 2

        if not winner:
            winner = player1 if player1.stamina > player2.stamina else player2

        return f'Winner: {winner.name}'

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join([*[p.__str__() for p in self.players], *[s.details() for s in self.supplies]])
