class SteamUser:
    def __init__(self, username: str, games: list):
        username = username
        games = games
        played_hours = 0

    def play(self, game: str, hours: int):
        if game in games:
            played_hours += hours
            return f'{username} is playing {game}'
        else:
            return f'{game} is not in library'

    def buy_game(self, game):
        if game not in games:
            games.append(game)
            return f'{username} bought {game}'
        else:
            return f'{game} is already in your library'

    def status(self):
        return f"{username} has {len(games)} games. Total play time: {played_hours}"

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
