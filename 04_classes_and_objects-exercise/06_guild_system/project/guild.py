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
        else:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        found_player = False
        for i, player in enumerate(self.players):
            if player_name == player.name:
                self.players.pop(i)
                player.guild = 'Unaffiliated'
                found_player = True
                return f'Player {player_name} has been removed from the guild.'
        if not found_player:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        return_string = ""
        return_string += f'Guild: {self.name}\n'
        # print(self.players)
        for player in self.players:
            return_string += f'{player.player_info()}'
        return return_string


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())

