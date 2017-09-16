## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

# I worked on this assignment with Tyler Hoff and Jacob Haspiel.
# We went through code_description_507F17project1.txt and wrote output
# English-language descriptions of what tests to run,
# occasionally making code-y notes such as "create a card object and
# save it to a variable."  My code-code, however, is my own.

# test suite of class Card class variables
class test_class_card_class_variables(unittest.TestCase):
    # is Card.suit_names of type list
    def test_is_suit_names_a_list(self):
        self.assertEqual(type(Card.suit_names), type(["el1", "el2"]), "Testing that the class variable Card.suit_names is of type list")
    # are the elements in the list Card.suit_names strings
    def test_are_elements_of_suit_names_strings(self):
        for element in Card.suit_names:
            self.assertEqual(type(element), type("s1"), "Testing that the elements of the list Card.suit_names are of type string")
    # are the elements in the list Card.suit_names the suit names
    def test_are_elements_of_suit_names_the_suit_names(self):
        suit_list = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for element in Card.suit_names:
            self.assertEqual(element in suit_list, True, "Testing that the elements of the list Card.suit_names are the suit names")
    # is Card.rank_levels of type list
    def test_is_rank_levels_a_list(self):
        self.assertEqual(type(Card.rank_levels), type(["el1", "el2"]), "Testing that the class variable Card.rank_levels is of type list")
    # is the length of the list Card.rank_levels 13
    def test_is_rank_levels_length_13(self):
        self.assertEqual(len(Card.rank_levels), 13, "Testing that the length of the list Card.rank_levels is 13")
    # are the elements in Card.rank_levels integers
    def test_are_elements_of_rank_levels_integers(self):
        for element in Card.rank_levels:
            self.assertEqual(type(element), type(1), "Testing that the elements of the list Card.rank_levels are of type integer")
    # are the elements in Card.rank_levels the integers 1-13
    def test_are_elements_of_rank_levels_1_through_13(self):
        list_of_1_through_13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for element in Card.rank_levels:
            self.assertEqual(element in list_of_1_through_13, True, "Testing that the elements of the list Card.rank_levels are the integers 1 through 13, inclusive")
    # is Card.faces of type dictionary
    def test_is_faces_a_dictionary(self):
        self.assertEqual(type(Card.faces), type({"a":1}), "Testing that the class variable Card.faces is a dictionary")
    # are there four key/value pairs in the dictionary Card.faces
    def test_that_faces_has_four_keys(self):
        self.assertEqual(len(Card.faces.keys()), 4, "Testing that the dictionary Card.faces has four keys, and thus four key/value pairs")
    # are the key/value pairs in the dictionary Card.faces 1:"Ace", etc.
    def test_that_faces_has_right_face_pairs(self):
        face_pairs_list = [(1, 'Ace'), (11, 'Jack'), (12, 'Queen'), (13, 'King')]
        for item in Card.faces.items():
            self.assertEqual(item in face_pairs_list, True, "Testing that the key/value pairs in the dictionary Card.faces are 1-Ace, 11-Jack, 12-Queen, and 13-King")

if __name__ == "__main__":
    unittest.main(verbosity=2)
