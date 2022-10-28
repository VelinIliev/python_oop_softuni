from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        name = name
        pokemons = []

    def add_pokemon(self, pokemon):
        pokemons_list = [x.name for x in pokemons]
        if pokemon.name in pokemons_list:
            return f'This pokemon is already caught'
        else:
            pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for i, x in enumerate(pokemons):
            if x.name == pokemon_name:
                pokemons.pop(i)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        return_string = ""
        return_string += f'Pokemon Trainer {name}\n'
        return_string += f'Pokemon count {len(pokemons)}\n'
        for data in pokemons:
            return_string += f'- {data.pokemon_details()}\n'
        return return_string


