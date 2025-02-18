import unittest
from Pikachu import Pikachu
import os

class TestPokemon(unittest.TestCase):
    def setUp(self):
        '''
        Clean up the stats file before tests
        '''
        if os.path.exists("pokemon_stats.txt"):
            os.remove("pokemon_stats.txt")

    def test_take_damage_updates_health(self):
        '''
        Test the take damage method for Pikachu
        '''
        pikachu = Pikachu()
        pikachu.take_damage(20)
        self.assertEqual(pikachu.get_current_health(), 40)

    def test_file_created_on_damage(self):
        '''
        Test that the stats are being correctly stored for Pikachu
        '''
        pikachu = Pikachu()
        pikachu.take_damage(10)
        self.assertTrue(os.path.exists("pokemon_stats.txt"))
        with open("pokemon_stats.txt", "r") as file:
            content = file.read()
        self.assertIn("Pikachu", content)

if __name__ == "__main__":
    unittest.main()
