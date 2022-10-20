from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        pokemons_list = [x.name for x in self.pokemons]
        if pokemon.name in pokemons_list:
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for i, x in enumerate(self.pokemons):
            if x.name == pokemon_name:
                self.pokemons.pop(i)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        return_string = ""
        return_string += f'Pokemon Trainer {self.name}\n'
        return_string += f'Pokemon count {len(self.pokemons)}\n'
        for data in self.pokemons:
            return_string += f'- {data.pokemon_details()}\n'
        return return_string


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())

# TODO: not ready
