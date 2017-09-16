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

# test suite of class Card instance variables
class test_class_card_instance_variables(unittest.TestCase):
    # does an instance of class Card have the instance variable self.suit, and is self.suit of type string
    def test_that_test_default_card_has_string_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_default_card.suit), type("str"), "Testing that the Card instance test_default_card has an instance variable test_default_card.suit of type string")
    def test_that_test_number_card_has_string_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_number_card.suit), type("str"), "Testing that the Card instance test_number_card has an instance variable test_number_card.suit of type string")
    def test_that_test_face_card_has_string_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_face_card.suit), type("str"), "Testing that the Card instance test_face_card has an instance variable test_face_card.suit of type string")
    # does an instance of class Card have the instance variable self.rank, and is self.rank of type integer (for non-face cards) or string (for face cards)
    def test_that_test_default_card_has_integer_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_default_card.rank), type(1), "Testing that the Card instance test_default_card has an instance variable test_default_card.rank of type integer")
    def test_that_test_number_card_has_integer_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_number_card.rank), type(1), "Testing that the Card instance test_number_card has an instance variable test_number_card.rank of type integer")
    def test_that_test_face_card_has_string_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_face_card.rank), type("str"), "Testing that the Card instance test_face_card has an instance variable test_face_card.rank of type string")
    # does an instance of class Card have the instance variable self.rank_num, and is self.rank_num of type integer
    def test_that_test_default_card_has_integer_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_default_card.rank_num), type(1), "Testing that the Card instance test_default_card has an instance variable test_default_card.rank_num of type integer")
    def test_that_test_number_card_has_integer_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_number_card.rank_num), type(1), "Testing that the Card instance test_number_card has an instance variable test_number_card.rank_num of type integer")
    def test_that_test_face_card_has_integer_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(type(test_face_card.rank_num), type(1), "Testing that the Card instance test_face_card has an instance variable test_face_card.rank_num of type integer")
    # does an instance of class Card without inputs given have as its instance variables the correct defaults (2 of Diamonds, i.e. self.suit is "Diamonds," self.rank is 2, and self.rank_num is 2)
    def test_that_test_default_card_has_correct_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_default_card.suit, "Diamonds", "Testing that the Card instance test_default_card has an instance variable test_default_card.suit whose value is the string 'Diamonds'")
    def test_that_test_default_card_has_correct_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_default_card.rank, 2, "Testing that the Card instance test_default_card has an instance variable test_default_card.rank whose value is the integer 2")
    def test_that_test_default_card_has_correct_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_default_card.rank_num, 2, "Testing that the Card instance test_default_card has an instance variable test_default_card.rank_num whose value is the integer 2")
    # does an instance of class Card with inputs given have as its instance variables the correct suit and rank
    def test_that_test_number_card_has_correct_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_number_card.suit, "Hearts", "Testing that the Card instance test_number_card has an instance variable test_number_card.suit whose value is the string 'Hearts'")
    def test_that_test_number_card_has_correct_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_number_card.rank, 7, "Testing that the Card instance test_number_card has an instance variable test_number_card.rank whose value is the integer 7")
    def test_that_test_number_card_has_correct_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_number_card.rank_num, 7, "Testing that the Card instance test_number_card has an instance variable test_number_card.rank_num whose value is the integer 7")
    def test_that_test_face_card_has_correct_suit(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_face_card.suit, "Spades", "Testing that the Card instance test_face_card has an instance variable test_face_card.suit whose value is Spades")
    def test_that_test_face_card_has_correct_rank(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_face_card.rank, "Queen", "Testing that the Card instance test_face_card has an instance variable test_face_card.rank whose value is the string 'Queen'")
    def test_that_test_face_card_has_correct_rank_num(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_face_card.rank_num, 12, "Testing that the Card instance test_face_card has an instance variable test_face_card.rank_num whose value is the integer 12")
    # does the string method print what it should
    def test_of_test_default_card_string_method(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_default_card.__str__(), "2 of Diamonds", "Testing that the string method of test_default_card prints the string '2 of Diamonds'")
    def test_of_test_number_card_string_method(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_number_card.__str__(), "7 of Hearts", "Testing that the string method of test_number_card prints the string '7 of Hearts'")
    def test_of_test_face_card_string_method(self):
        test_default_card = Card() # no input; should be 2 of Diamonds
        test_number_card = Card(2, 7) # should be 7 of Hearts
        test_face_card = Card(3, 12) # should be Queen of Spades
        self.assertEqual(test_face_card.__str__(), "Queen of Spades", "Testing that the string method of test_face_card prints the string 'Queen of Spades'")

# test suite of class Deck constructor
class test_class_deck_constructor(unittest.TestCase):
    # is the instance variable self.cards a list
    def test_is_instance_variable_cards_a_list(self):
        test_deck = Deck()
        self.assertEqual(type(test_deck.cards), type(["el1", "el2"]), "Testing that the instance variable test_deck.cards is of type list")
    # is the length of the list self.cards 52
    def test_is_instance_variable_cards_len_52(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.cards), 52, "Testing that the length of the list test_deck.cards is 52")
    # are the elements in the list self.cards Card objects
    def test_are_elements_of_instance_variable_cards_card_objects(self):
        test_deck = Deck()
        test_card = Card()
        for card in test_deck.cards:
            self.assertEqual(type(card), type(test_card), "Testing that each element of the list test_deck.cards is a Card object")
    # does the string method create a string
    def test_does_deck_string_method_create_a_string(self):
        test_deck = Deck()
        self.assertEqual(type(test_deck.__str__()), type("str"), "Testing that the string method of Deck instance test_deck produces a string")
    # is the string produced by the string method 52 lines
    def test_does_deck_string_method_create_a_52_line_string(self):
        test_deck = Deck()
        test_deck_split = test_deck_split("\n")
        self.assertEqual(len(test_deck_split), 52, "Testing that the string produced by the string method of Deck instance test_deck is 52 lines long")
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
