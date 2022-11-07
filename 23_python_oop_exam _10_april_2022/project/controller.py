class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def found_player(self, name):
        return next(filter(lambda x: x.name == name, self.players), None)

    def find_supply(self, type_of_supply):
        found_supply = None
        index = None
        for i, supply in enumerate(self.supplies[::-1]):
            if supply.__class__.__name__ == type_of_supply:
                index = -(i + 1)
                found_supply = supply
                break
        if found_supply:
            self.supplies.pop(index)
        return found_supply

    def add_player(self, *players):
        added_names = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_names.append(player.name)
        return f'Successfully added: {", ".join(x for x in added_names)}'

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.found_player(player_name)
        if player:
            if not player.need_sustenance:
                return f'{player_name} have enough stamina.'
            supply = self.find_supply(sustenance_type)
            if not supply:
                raise Exception(f'There are no {sustenance_type.lower()} supplies left!')
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f'{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.found_player(first_player_name)
        second_player = self.found_player(second_player_name)
        display_strings = []
        if first_player.stamina == 0:
            display_strings.append(f'Player {first_player.name} does not have enough stamina.')
        if second_player.stamina == 0:
            display_strings.append(f'Player {second_player.name} does not have enough stamina.')
        if display_strings:
            return "\n".join(x for x in display_strings)
        if first_player.stamina < second_player.stamina:
            second_player.stamina -= first_player.stamina / 2
            if second_player.stamina <= 0:
                return f'Winner: {first_player.name}'
            first_player.stamina -= second_player.stamina / 2
            if first_player.stamina <= 0:
                return f'Winner: {second_player.name}'
        elif second_player.stamina < first_player.stamina:
            first_player.stamina -= second_player.stamina / 2
            if first_player.stamina <= 0:
                return f'Winner: {second_player.name}'
            second_player.stamina -= first_player.stamina / 2
            if second_player.stamina <= 0:
                return f'Winner: {first_player.name}'
        if first_player.stamina > second_player.stamina:
            return f'Winner: {first_player.name}'
        else:
            return f'Winner: {second_player.name}'

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        display_list = []
        for player in self.players:
            display_list.append(f'{player}')
        for supply in self.supplies:
            display_list.append(f'{supply.details()}')
        return "\n".join(display_list)

