from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        __name = name
        __rating = rating
        __players = []

    def add_player(self, new_player: Player):
        for player in __players:
            if player.name == new_player.name:
                return f'Player {new_player.name} has already joined'
        __players.append(new_player)
        return f'Player {new_player.name} joined team {__name}'

    def remove_player(self, player_name):
        for i, player in enumerate(__players):
            if player.name == player_name:
                return __players.pop(i)
        return f'Player {player_name} not found'