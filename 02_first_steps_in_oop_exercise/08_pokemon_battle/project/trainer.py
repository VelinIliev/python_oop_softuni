from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons), 0)
        if pokemon:
            self.pokemons.remove(pokemon)
            return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        output = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        [output.append(f'- {pokemon.pokemon_details()}') for pokemon in self.pokemons]
        return '\n'.join(output)


