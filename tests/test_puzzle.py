""" Unit tests for the mini_game module. """

# Write unit tests for the mini_game module
# import the unittest module
import unittest

# import the mini_game module
from mini_game import main as mini_game


# define a class called TestPuzzle
class TestMiniGame(unittest.TestCase):
    """TestMiniGame class."""

    # define a test for the determine_outcome function
    def test_determine_outcome(self):
        """Test determine_outcome function."""
        # assert that the determine_outcome function returns the expected result
        self.assertEqual(mini_game.determine_outcome("rock", "scissors"), "You win!")
        self.assertEqual(mini_game.determine_outcome("paper", "rock"), "You win!")
        self.assertEqual(mini_game.determine_outcome("scissors", "paper"), "You win!")
        self.assertEqual(mini_game.determine_outcome("lizard", "paper"), "You win!")
        self.assertEqual(mini_game.determine_outcome("lizard", "spock"), "You win!")
        self.assertEqual(mini_game.determine_outcome("spock", "rock"), "You win!")
        self.assertEqual(mini_game.determine_outcome("rock", "paper"), "Computer wins!")
        self.assertEqual(
            mini_game.determine_outcome("paper", "scissors"), "Computer wins!"
        )
        self.assertEqual(
            mini_game.determine_outcome("scissors", "rock"), "Computer wins!"
        )
        self.assertEqual(
            mini_game.determine_outcome("lizard", "scissors"), "Computer wins!"
        )
        self.assertEqual(
            mini_game.determine_outcome("spock", "paper"), "Computer wins!"
        )
        self.assertEqual(mini_game.determine_outcome("rock", "rock"), "Tie!")
        self.assertEqual(mini_game.determine_outcome("paper", "paper"), "Tie!")
        self.assertEqual(mini_game.determine_outcome("scissors", "scissors"), "Tie!")
        self.assertEqual(mini_game.determine_outcome("lizard", "lizard"), "Tie!")
        self.assertEqual(mini_game.determine_outcome("spock", "spock"), "Tie!")
