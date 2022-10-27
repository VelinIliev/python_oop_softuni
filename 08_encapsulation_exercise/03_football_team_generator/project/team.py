from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, new_player: Player):
        for player in self.__players:
            if player.name == new_player.name:
                return f'Player {new_player.name} has already joined'
        self.__players.append(new_player)
        return f'Player {new_player.name} joined team {self.__name}'

    def remove_player(self, player_name):
        for i, player in enumerate(self.__players):
            if player.name == player_name:
                return self.__players.pop(i)
        return f'Player {player_name} not found'