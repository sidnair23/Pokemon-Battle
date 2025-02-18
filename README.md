# Pokemon-Battle

## Short Summary
This is a project I did for Boston University course MET CS 521: Information Structures with Python. The agenda is to create a command line Pokemon Battle game much like Pokemon Red.

## Detailed Summary
The premise is straightforward. You select one of the four Pokemons:
	1) Pikachu - Electric Type
	2) Bulbasaur - Grass Type
	3) Charmander - Fire Type
	4) Squirtle - Water Type

You then battle other Pokemon you did not choose, each with unique moves, strengths, and weaknesses against your chosen Pokemon.

Your choice of Pokemon can fare better or worse against the competing Pokemon based on the type. Each type has strengths and weaknesses over other types. For example, the Grass-type has advantages over the Water type, the Water-type has advantages over the Fire-type, and the Fire-type has advantages over the Grass-type. Electric-type has an advantage over water but a disadvantage regarding grass. 

Each Pokemon has four total moves they can use:
	1) General Moves: They do not suffer any penalties based on type. Conversely, they do not benefit from any advantages.
	2) Type-Specific Moves: These moves are specific to the Pokemon. For Pikachu, these are Thunder Shock and Shock Wave.

Three factors determine the effective hitpoint (i.e. power of the move):
  1) Base Strength of the move
	2) Probability of the move having full damage (more substantial moves may have lower chances to give full damage) 
	3) Type advantage/disadvantage: 25% increase or decrease in the over-hit point. 
	Final formula:
  #### RoundUp(Base Strength*Base Move Hitting Probability)*(0.75/1/1.25)
	
As an example, in a battle between Bulbasaur and Charmander, if Bulbasaur uses Seed bomb, the final hit point will be: (30*(0.65))*(0.75) = 14.625 = 15; where 30 is the base strength, 0.65 is the modifier, i.e., 65% of the base strength will be hit, and 0.75 is the type disadvantage. As such, assuming this was the first move, Charmander will suffer 15 (round up) damage on its base strength of 50 leaving health as 35.

A typical program will go as follows:
  1) The program will display a welcome message and prompt the user to select one of the four Pokemons 
	2) The user selects one of the four Pokemon, and the program initiates the battle
	3) The user selects the moves available to the Pokemon, and the program calculates the hitpoints based on the specifics of the move and applies the damage to the opponent. 
	4) Similarly, the opponent program chooses a random move, and its hitpoint is applied to the user's Pokemon.
	5) If the user wins the current battle, The user can continue to the next battle or quit.
	6) If the user continues, the user's Pokemon will regain its full health before the next battle
	7) If the user loses the battle, the program quits and passes a ‘Thank you for playing message.’
	8) If the user wins all the battles, a final congrats message will be sent out. 
	9) After the end of the competition, the game will display a log file of health resets and end HP after each round and a unique list of moves used. 
