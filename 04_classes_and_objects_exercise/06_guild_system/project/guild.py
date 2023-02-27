from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        player = next(filter(lambda x: x.name == player_name, self.players), 0)
        if player:
            self.players.remove(player)
            player.guild = 'Unaffiliated'
            return f'Player {player_name} has been removed from the guild.'

        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        output = [f'Guild: {self.name}']
        for player in self.players:
            output.append(f'{player.player_info()}')
        return '\n'.join(output)




