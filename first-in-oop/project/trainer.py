from project.pokemon import Pokemon


class Trainer:
    pokemons = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            # return f"Caught {pokemon.name} with health {pokemon.health}"
            return "Caught " + pokemon.pokemon_details()
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for po in self.pokemons:
            if pokemon_name == po.name:
                self.pokemons.remove(po)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        result += "\n".join([f"- {po.pokemon_details()}" for po in self.pokemons])
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
