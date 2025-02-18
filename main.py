'''
Main.py that runs the game
'''

# IMPORTS
from Pokemon import Pokemon
from Pikachu import Pikachu
from Bulbasaur import Bulbasaur
from Squirtle import Squirtle
from Charmander import Charmander
import random

# FUNCTIONS
def reset_stats_file():
    '''
    Recreates the stats file at the beginning of each game session
    '''
    with open("pokemon_stats.txt", "w") as file:
        file.write("========== Pokemon Battle Stats ==========\n")
        file.write("New Game Session\n")
        file.write("-----------------------------------------\n")


def display_pokemon_stats():
    '''
    Reads and displays saved Pokemon stats from the file
    '''
    print("\nBattle Log - Pokemon Stats:")
    try:
        with open("pokemon_stats.txt", "r") as file:
            stats = file.read()
            print(stats)
    except FileNotFoundError:
        print("No battle stats found.")


def validate_input(prompt: str, valid_range: range) -> int:
    '''
    Validates integer input within a given range.
    '''
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value in valid_range:
                return value
            else:
                print(f"Please enter a valid number between {valid_range.start} and {valid_range.stop - 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate_continue(prompt: str) -> bool:
    '''
    Validates yes/no input.
    '''
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["y", "n"]:
            return user_input == "y"
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


def battle(pokemon: Pokemon, opponent: Pokemon, used_moves: set) -> bool:
    '''
    Single battle between two Pokemon until one is defeated.
    '''
    print(f"\nYou are now battling {opponent.name}!")
    print("-" * 150)

    while not (pokemon.is_defeated() or opponent.is_defeated()):
        # Display moves
        print("Your Moves:")
        for key, value in pokemon.moves.items():
            print(f"{key}. {value[0]} - Base Power: {value[1]}, Modifier Range: {(value[2]*100):.0f}%")
        print("-" * 150)

        # User's turn
        move_choice = validate_input("Choose a move (1-4): ", range(1, 5))
        user_move_stat = pokemon.moves[move_choice]
        used_moves.add(user_move_stat[0])  # Add move to the set
        user_damage = pokemon.attack(user_move_stat, opponent.pokemon_type)
        opponent.take_damage(user_damage)

        print(f"{pokemon.name} used {user_move_stat[0]}! It dealt {user_damage} damage.")
        print(f"{opponent.name} has {opponent.get_current_health()} HP left.")
        print("-" * 150)

        if opponent.is_defeated():
            print(f"{opponent.name} has been defeated!")
            return True

        # Opponent's turn
        opponent_move = random.choice(list(opponent.moves.values()))
        opponent_damage = opponent.attack(opponent_move, pokemon.pokemon_type)
        pokemon.take_damage(opponent_damage)

        print(f"{opponent.name} used {opponent_move[0]}! It dealt {opponent_damage} damage.")
        print(f"{pokemon.name} has {pokemon.get_current_health()} HP left.")
        print("-" * 150)

    return not pokemon.is_defeated()


# MAIN
if __name__ == "__main__":
    # Initialize Stats File
    reset_stats_file()

    # Initialize Pokemon
    pokemons = [Pikachu(), Bulbasaur(), Squirtle(), Charmander()]
    pokemon_names = [pokemon.name for pokemon in pokemons]
    used_moves = set()  # Set to store unique moves used

    print("Welcome to Pokemon Battle!")
    print("Choose your Pokemon, but beware—you'll face the others!")
    print("-" * 150)

    # Start game
    if not validate_continue("Ready to start? (Y/N): "):
        print("Thank you for playing!")
        exit()

    print("Choose your Pokemon:")
    for index, name in enumerate(pokemon_names, 1):
        print(f"{index}. {name}")

    user_choice = validate_input("Your choice (1-4): ", range(1, 5))
    user_pokemon = pokemons[user_choice - 1]
    print(f"\nYou chose {user_pokemon.name}! Let the battles begin!")
    print("-" * 150)

    # Opponent Pokemon List
    opponents = [pokemon for pokemon in pokemons if pokemon.name != user_pokemon.name]
    random.shuffle(opponents)

    # Battles
    for index, opponent in enumerate(opponents, start= 1):
        user_pokemon.reset_health()
        opponent.reset_health()

        battle_name = f"Battle {index}: {user_pokemon.name} vs {opponent.name}"
        print(f"\nStarting {battle_name}")
        user_won = battle(user_pokemon, opponent, used_moves)
        
        if user_won:
            print(f"Congratulations! {user_pokemon.name} defeated {opponent.name}!\n")
            # Check if this is the last opponent
            if index == len(opponents):
                print("You defeated all opponents! You are the Pokemon Champion!")
                break
        else:
            print(f"Game Over! {opponent.name} defeated {user_pokemon.name}. Better luck next time!")
            break

        # Ask to continue only if there are remaining opponents
        if not validate_continue("Do you want to continue to the next battle? (Y/N): "):
            print("Thank you for playing! See you next time.")
            break

    # Display moves and stats used
    print("\nUnique Moves Used in Battle:", ", ".join(used_moves))
    display_pokemon_stats()

