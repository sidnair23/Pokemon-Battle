from Pokemon import Pokemon
import random

class Charmander(Pokemon):
    '''
    Charmander class with Grass-type move.
    '''
    MOVES = {1: ("Slash", 7, 0.85), 2: ("Punch", 9, 0.80), 3: ("Flamethrower", 30, 0.45), 4: ("Ember", 15, 0.75)} #Default moves. In format: Key: (Move Name, Base Value, Modifier) 

    def __init__(self):
        super().__init__(name = "Charmander", pokemon_type = "Fire", moves = Charmander.MOVES) #Initializes with the name, pokemon type and moves.

    
    def attack(self, move_list: tuple, opponent_type: str) -> int:
        '''
        Calculates the damage of the given move for the given opponent_type.
        '''
        base = move_list[1]
        hp_modifier = random.uniform(move_list[2], 1.00)
        move_name = move_list[0]
        if move_name == "Slash" or "Punch":
            type_modifier = 1
        else:
            if opponent_type == "Grass":
                type_modifier = 1.25
            elif opponent_type == "Water":
                type_modifier = 0.75
            else:
                type_modifier = 1
        damage = base * hp_modifier * type_modifier
        damage = int(round(damage, 0))
        return damage
