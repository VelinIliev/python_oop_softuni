class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player(self, name):
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
        player = self.find_player(player_name)
        if player.stamina == 100:
            return f'{player_name} have enough stamina.'
        if sustenance_type == "Food" or sustenance_type == "Drink":
            supply = self.find_supply(sustenance_type)
            if not supply:
                raise Exception(f'There are no {sustenance_type.lower()} supplies left!')
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f'{player_name} sustained successfully with {supply.name}.'

    @staticmethod
    def battle(attacker, defender):
        defender.stamina -= attacker.stamina / 2
        if attacker.stamina - defender.stamina / 2 <= 0:
            attacker.stamina = 0
        else:
            attacker.stamina -= defender.stamina / 2
        if attacker.stamina > defender.stamina:
            return f'Winner: {attacker.name}'
        else:
            return f'Winner: {defender.name}'

    @staticmethod
    def not_ready_players(*players):
        display_string = []
        for player in players:
            if player.stamina == 0:
                display_string.append(f'Player {player.name} does not have enough stamina.')
        return "\n".join(display_string)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player(first_player_name)
        second_player = self.find_player(second_player_name)
        not_ready_players = self.not_ready_players(first_player, second_player)
        if not_ready_players:
            return not_ready_players
        if first_player.stamina < second_player.stamina:
            battle_result = self.battle(first_player, second_player)
        else:
            battle_result = self.battle(second_player, first_player)
        return battle_result

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
