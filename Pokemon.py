class Pokemon:
    '''
    Base class for all Pokemons
    '''
    HEALTH_POINT = 50  # Default health point.

    def __init__(self, name, pokemon_type, moves):
        self.name = name  # Public attribute
        self.pokemon_type = pokemon_type  # Public attribute
        self._current_health = Pokemon.HEALTH_POINT  # Private attribute
        self.moves = moves  # Public attribute

    def get_current_health(self) -> int:
        '''
        Getter method for current health
        '''
        return self._current_health
    
    def _save_stats_to_file(self, battle_name:str):
        '''
        Private method to save Pokémon stats to a file with battle information
        '''
        with open("pokemon_stats.txt", "a") as file:
            if battle_name == "Health Reset":
                file.write(f"Health Reset for {self.name}\n")
                file.write("-----------------------------------------\n")
            else:
                file.write(f"{self.name}: {self._current_health} HP, Type: {self.pokemon_type}\n")
                file.write("-----------------------------------------\n")

    def take_damage(self, damage: int) -> None:
        '''
        Reduces the current health by the given damage
        '''
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0
        self._save_stats_to_file(damage)  # Save stats whenever damage is taken
        

    def is_defeated(self) -> bool:
        '''
        Checks if the Pokemon is defeated.
        '''
        return self._current_health <= 0

    def reset_health(self):
        '''
        Resets the health back to default health value
        '''
        self._current_health = Pokemon.HEALTH_POINT
        self._save_stats_to_file(battle_name="Health Reset")  # Save reset stats with default battle name


    def __eq__(self, other):
        '''
        Magic method to compare two Pokémon by their current health.
        '''
        if isinstance(other, Pokemon):
            return self._current_health == other.get_current_health()
        return False

    def __str__(self) -> str:
        '''
        Returns a string representation of the Pokemon
        '''
        return f"{self.name} of type {self.pokemon_type} with current health at {self._current_health} out of {Pokemon.HEALTH_POINT}"
