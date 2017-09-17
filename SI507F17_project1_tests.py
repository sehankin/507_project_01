# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

# BEGIN TESTS

# I worked on this assignment with Tyler Hoff and Jacob Haspiel.
# We went through code_description_507F17project1.txt and wrote output
# English-language descriptions of what tests to run,
# occasionally making code-y notes such as "create a card object and
# save it to a variable."  My code-code, however, is my own,
# with two exceptions:
# 1. Jacob's try/except workaround for assertRaises() errors,
# which I appropriated because I wanted those tests to fail
# when an error is raised, and there's no assertNotRaises()
# 2. Tyler explained to me why my show_song tests couldn't recognize
# a Song object, and to type helper_functions.Song.


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
        test_deck_cards = test_deck.__str__()
        test_deck_split = test_deck_cards.split("\n")
        self.assertEqual(len(test_deck_split), 52, "Testing that the string produced by the string method of Deck instance test_deck is 52 lines long")
    # does the Deck string include the desired strings
    def test_does_deck_string_include_number_cards(self):
        test_deck = Deck()
        test_deck_cards = test_deck.__str__()
        self.assertEqual("2 of Diamonds" in test_deck_cards, True, "Testing that the string '2 of Diamonds' is in the Deck string")
    def test_does_deck_string_include_face_cards_right(self):
        test_deck = Deck()
        test_deck_cards = test_deck.__str__()
        self.assertEqual("Queen of Spades" in test_deck_cards, True, "Testing that the string 'Queen of Spades' is in the Deck string")
    def test_does_deck_string_include_face_cards_wrong(self):
        test_deck = Deck()
        test_deck_cards = test_deck.__str__()
        self.assertEqual("12 of Spades" in test_deck_cards, False, "Testing that the string '12 of Spades' is not in the Deck string")

# test suite of class Deck methods
class test_class_deck_methods(unittest.TestCase):
    # does the method pop_card reduce length of list self.cards by 1
    def test_pop_card_method_1_time(self):
        test_deck = Deck()
        test_deck.pop_card()
        self.assertEqual(len(test_deck.cards), 51, "Testing that the method pop_card reduces the length of the list test_deck.cards by 1")
    # does the method pop_card reduce length of list self.cards by 1 each time you do it
    def test_pop_card_method_10_times(self):
        test_deck = Deck()
        i = 1
        while i < 11:
            test_deck.pop_card()
            i = i + 1
        self.assertEqual(len(test_deck.cards), 42, "Testing that the method pop_card called 10 times reduces the length of the list test_deck.cards by 10")
    def test_pop_card_method_20_times(self):
        test_deck = Deck()
        i = 1
        while i < 21:
            test_deck.pop_card()
            i = i + 1
        self.assertEqual(len(test_deck.cards), 32, "Testing that the method pop_card called 20 times reduces the length of the list test_deck.cards by 20")
    def test_pop_card_method_52_times(self):
        test_deck = Deck()
        i = 1
        while i < 53:
            test_deck.pop_card()
            i = i + 1
        self.assertEqual(len(test_deck.cards), 0, "Testing that the method pop_card called 52 times reduces the length of the list test_deck.cards by 52, resulting in an empty deck of 0 cards")
    def test_pop_card_method_on_empty_deck(self):
        test_deck = Deck()
        i = 1
        while i < 53:
            test_deck.pop_card()
            i = i + 1
        try:
            test_deck.pop_card()
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that the method pop_card raises an error when called on an empty deck")

    # without input, does the method pop_card remove the "top" card (i.e. last in the list self.cards)
    def test_pop_card_no_input(self):
        test_deck = Deck()
        test_deck_list = test_deck.cards
        old_top_card = test_deck_list[-1]
        test_deck.pop_card()
        new_top_card = test_deck_list[-1]
        self.assertEqual(old_top_card == new_top_card, False, "Testing that without input, the pop_card method removes the 'top' card from the deck (i.e. the last element in the list test_deck.cards)")
    # with input, does the method pop_card remove the inputted card
    def test_pop_card_input_0(self):
        test_deck = Deck()
        test_deck_list = test_deck.cards
        old_card_0 = test_deck_list[0]
        test_deck.pop_card(0)
        new_card_0 = test_deck_list[0]
        self.assertEqual(old_card_0 == new_card_0, False, "Testing that with an input of 0, the pop_card method removes the first element in the list test_deck.cards (i.e. the 'bottom' card)")
    def test_pop_card_input_15(self):
        test_deck = Deck()
        test_deck_list = test_deck.cards
        old_card_15 = test_deck_list[15]
        test_deck.pop_card(15)
        new_card_15 = test_deck_list[15]
        self.assertEqual(old_card_15 == new_card_15, False, "Testing that with an input of 15, the pop_card method removes the 15th element (under zero index) in the list test_deck.cards")
    def test_pop_card_input_30(self):
        test_deck = Deck()
        test_deck_list = test_deck.cards
        old_card_30 = test_deck_list[30]
        test_deck.pop_card(30)
        new_card_30 = test_deck_list[30]
        self.assertEqual(old_card_30 == new_card_30, False, "Testing that with an input of 30, the pop_card method removes the 30th element (under zero index) in the list test_deck.cards")
    # does the method shuffle change the order of the cards
    def test_shuffle(self):
        test_deck = Deck()
        deck_before_shuffle = test_deck.cards
        deck_before_shuffle_strings = []
        for card_object in deck_before_shuffle:
            deck_before_shuffle_strings.append(card_object.__str__())
            test_deck.shuffle()
        deck_after_shuffle = test_deck.cards
        deck_after_shuffle_strings = []
        for card_object in deck_after_shuffle:
            deck_after_shuffle_strings.append(card_object.__str__())
        self.assertEqual(deck_before_shuffle_strings == deck_after_shuffle_strings, False, "Testing that the shuffle method changes the order of test_deck.cards by seeing whether lists of card strings (NOT objects) are the same before and after shuffling")
    # if you replace_card a card already in the deck, does it work (it shouldn't)
    def test_replace_card_on_full_deck(self):
        test_deck = Deck()
        card_53 = Card() # 2 of Diamonds
        test_deck.replace_card(card_53)
        self.assertEqual(len(test_deck.cards), 52, "Testing that the replace_card method doesn't add a card to a full deck")
    def test_remove_known_card_from_deck_and_try_to_replace_with_different_card(self):
        test_deck = Deck()
        i = 0
        while i < 52:
            for card_object in test_deck.cards:
                if card_object.__str__() == "3 of Diamonds":
                    three_of_diamonds_index = test_deck.cards.index(card_object)
            i = i + 1
        test_deck.pop_card(three_of_diamonds_index)
        extra_2_of_diamonds = Card()
        test_deck.replace_card(extra_2_of_diamonds)
        self.assertEqual(len(test_deck.cards), 51, "Testing that after using the pop_card method to remove a known card (here, the 3 of Diamonds) from Deck instance test_deck, attempting to replace_card a card still in test_deck (here, the 2 of Diamonds) won't work, and the list test_deck.cards will still have length 51")
    # if you pop_card a specific card from the list self.cards, can you replace_card it
    def test_remove_known_card_from_deck_and_try_to_replace_with_same_card(self):
        test_deck = Deck()
        i = 0
        while i < 52:
            for card_object in test_deck.cards:
                if card_object.__str__() == "2 of Diamonds":
                    two_of_diamonds_index = test_deck.cards.index(card_object)
            i = i + 1
        test_deck.pop_card(two_of_diamonds_index)
        extra_2_of_diamonds = Card()
        test_deck.replace_card(extra_2_of_diamonds)
        self.assertEqual(len(test_deck.cards), 52, "Testing that after using the pop_card method to remove a known card (here, the 2 of Diamonds) from Deck instance test_deck, attempting to replace_card that same card will work, and the list test_deck.cards will have length 52")
    # if you sort_cards a full deck, is the list self.cards sorted by suit
    def test_sort_cards_with_full_deck(self):
        test_deck = Deck()
        test_deck.sort_cards()
        for card_object in test_deck.cards:
            if test_deck.cards.index(card_object) < 13:
                self.assertEqual(card_object.suit, "Diamonds", "Testing that using the sort_card method on a full deck, the first 13 cards (indices 0-12) in the list test_deck.cards all have self.suit 'Diamonds'")
            elif test_deck.cards.index(card_object) > 12 and test_deck.cards.index(card_object) < 26:
                self.assertEqual(card_object.suit, "Clubs", "Testing that using the sort_card method on a full deck, the second 13 cards (indices 13-25) in the list test_deck.cards all have self.suit 'Clubs'")
            elif test_deck.cards.index(card_object) > 25 and test_deck.cards.index(card_object) < 39:
                self.assertEqual(card_object.suit, "Hearts", "Testing that using the sort_card method on a full deck, the third 13 cards (indices 26-38) in the list test_deck.cards all have self.suit 'Hearts'")
            elif test_deck.cards.index(card_object) > 38:
                self.assertEqual(card_object.suit, "Spades", "Testing that using the sort_card method on a full deck, the last 13 cards (indices 39-51) in the list test_deck.cards all have self.suit 'Spades'")
    # if you sort_cards a non-full deck, is the list self.cards sorted by suit
    def test_sort_cards_with_one_known_card_removed_from_deck(self):
        test_deck = Deck()
        i = 0
        while i < 52:
            for card_object in test_deck.cards:
                if card_object.__str__() == "2 of Diamonds":
                    two_of_diamonds_index = test_deck.cards.index(card_object)
            i = i + 1
        test_deck.pop_card(two_of_diamonds_index)
        test_deck.sort_cards()
        for card_object in test_deck.cards:
            if test_deck.cards.index(card_object) < 12:
                self.assertEqual(card_object.suit, "Diamonds", "Testing that using the sort_card method on a full deck, the first 13 cards (indices 0-11) in the list test_deck.cards all have self.suit 'Diamonds'")
            elif test_deck.cards.index(card_object) > 11 and test_deck.cards.index(card_object) < 25:
                self.assertEqual(card_object.suit, "Clubs", "Testing that using the sort_card method on a full deck, the next 13 cards (indices 12-24) in the list test_deck.cards all have self.suit 'Clubs'")
            elif test_deck.cards.index(card_object) > 24 and test_deck.cards.index(card_object) < 38:
                self.assertEqual(card_object.suit, "Hearts", "Testing that using the sort_card method on a full deck, the next 13 cards (indices 25-37) in the list test_deck.cards all have self.suit 'Hearts'")
            elif test_deck.cards.index(card_object) > 37:
                self.assertEqual(card_object.suit, "Spades", "Testing that using the sort_card method on a full deck, the last 13 cards (indices 38-5) in the list test_deck.cards all have self.suit 'Spades'")
    # if you deal_hand with a given integer input, is the length of the list self.cards reduced by that input (i.e. hand size)
    # N.B. I rewrote the tests of hand sizes greater than 27 to give me
    # FAILs instead of ERRORs.  The original tests are still there,
    # but commented out.
    def test_deal_hand_0(self):
        test_deck = Deck()
        test_deck.deal_hand(0)
        self.assertEqual(len(test_deck.cards), 52, "Testing that after using the deal_hand method with an input of 0 on a full deck, the length of the list test_deck remains 52")
    def test_deal_hand_5_once(self):
        test_deck = Deck()
        test_deck.deal_hand(5)
        self.assertEqual(len(test_deck.cards), 47, "Testing that after using the deal_hand method once with an input of 5 on a full deck, the length of the list test_deck is 47")
    def test_deal_hand_5_five_times(self):
        test_deck = Deck()
        i = 1
        while i < 6:
            test_deck.deal_hand(5)
            i = i + 1
        self.assertEqual(len(test_deck.cards), 27, "Testing that after using the deal_hand method five times with an input of 5 on a full deck, the length of the list test_deck is 27")
    #def test_deal_hand_5_ten_times_original(self):
    #    test_deck = Deck()
    #    i = 1
    #    while i < 11:
    #        test_deck.deal_hand(5)
    #        i = i + 1
    #    self.assertEqual(len(test_deck.cards), 2, "Testing that after using the deal_hand method ten times with an input of 5 on a full deck, the length of the list test_deck is 2")
    def test_deal_hand_5_ten_times(self):
        test_deck = Deck()
        try:
            i = 1
            while i < 11:
                test_deck.deal_hand(5)
                i = i + 1
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that attempting to use the deal_hand method ten times with an input of 5 on a full deck raises an error")
    #def test_deal_hand_52_original(self):
    #    test_deck = Deck()
    #    test_deck.deal_hand(52)
    #    self.assertEqual(len(test_deck.cards), 0, "Testing that after using the deal_hand method once with an input of 52 on a full deck, the length of the list test_deck is 0")
    def test_deal_hand_52(self):
        test_deck = Deck()
        try:
            test_deck.deal_hand(52)
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that attempting to use the deal_hand method with an input of 52 on a full deck raises an error")
    # hand of 40
    #def test_deal_hand_40_original(self):
    #    test_deck = Deck()
    #    test_deck.deal_hand(40)
    #    self.assertEqual(len(test_deck.cards), 12, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 12")
    def test_deal_hand_40(self):
        test_deck = Deck()
        try:
            test_deck.deal_hand(40)
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that attempting to use the deal_hand method with an input of 40 on a full deck raises an error")
    # hand of 30
    #def test_deal_hand_30_original(self):
    #    test_deck = Deck()
    #    test_deck.deal_hand(30)
    #    self.assertEqual(len(test_deck.cards), 22, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 22")
    def test_deal_hand_30(self):
        test_deck = Deck()
        try:
            test_deck.deal_hand(30)
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that attempting to use the deal_hand method with an input of 30 on a full deck raises an error")
    # hand of 20
    def test_deal_hand_20(self):
        test_deck = Deck()
        test_deck.deal_hand(20)
        self.assertEqual(len(test_deck.cards), 32, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 32")
    # hand of 25
    def test_deal_hand_25(self):
        test_deck = Deck()
        test_deck.deal_hand(25)
        self.assertEqual(len(test_deck.cards), 27, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 27")
    # hand of 26
    def test_deal_hand_26(self):
        test_deck = Deck()
        test_deck.deal_hand(26)
        self.assertEqual(len(test_deck.cards), 26, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 26")
    # hand of 27
    #def test_deal_hand_27_original(self):
    #    test_deck = Deck()
    #    test_deck.deal_hand(27)
    #    self.assertEqual(len(test_deck.cards), 25, "Testing that after using the deal_hand method once with an input of 40 on a full deck, the length of the list test_deck is 25")
    def test_deal_hand_27(self):
        test_deck = Deck()
        try:
            test_deck.deal_hand(27)
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that attempting to use the deal_hand method with an input of 27 on a full deck raises an error")
    # hand of 53
    def test_deal_hand_53(self):
        test_deck = Deck()
        try:
            test_deck.deal_hand(53)
            no_error = True
        except:
            no_error = False
        self.assertEqual(no_error, True, "Testing that if the deal_hand method is called 53 times on a full deck, it raises an error")

    # does deal_hand function return a list whose length is the hand
    def test_deal_hand_returns_list(self):
        test_deck = Deck()
        hand = test_deck.deal_hand(7)
        self.assertEqual(len(hand), 7, "Testing that using the deal_hand method once with an input of 7 on a full deck returns a list of length 7")
    # are the elements in the list Card objects
    def test_deal_hand_returns_list_of_card_objects(self):
        test_deck = Deck()
        hand = test_deck.deal_hand(7)
        for element in hand:
            self.assertEqual(type(element), Card, "Testing that the elements in the list returned by the deal_hand method are Card objects")
    # are those Card objects absent from the deck
    def test_deal_hand_removes_card_objects_from_deck(self):
        test_deck = Deck()
        hand = test_deck.deal_hand(7)
        test_deck_strings = []
        for deck_card_object in test_deck.cards:
            test_deck_strings.append(deck_card_object.__str__())
        for hand_card_object in hand:
            hand_card_string = hand_card_object.__str__()
            self.assertEqual(hand_card_string not in test_deck_strings, True, "Testing that the Card objects in the list returned by the deal_hand method are removed from the test_deck")

# test suite of function play_war_game
class test_function_play_war_game(unittest.TestCase):
    # does the function play_war_game return a tuple
    def test_if_function_play_war_game_returns_a_tuple(self):
        war_game = play_war_game(testing=True)
        self.assertEqual(type(war_game), type(("tup1", "tup2")), "Testing that the function play_war_game returns a tuple")
    # is the length of the tuple 3
    def test_if_function_play_war_game_returns_a_tuple_of_length_3(self):
        war_game = play_war_game(testing=True)
        self.assertEqual(len(war_game), 3, "Testing that the function play_war_game returns a tuple of length 3")
    # is tup[0] of type string
    def test_if_element_0_of_war_game_tuple_is_of_type_string(self):
        war_game = play_war_game(testing=True)
        self.assertEqual(type(war_game[0]), type("str"), "Testing that element 0 of the tuple returned by the function play_war_game is a string")
    # is the string one of "Player1", "Player2", "Tie"
    def test_if_element_0_of_war_game_tuple_is_an_approved_string(self):
        war_game = play_war_game(testing=True)
        approved_strings = ["Player1", "Player2", "Tie"]
        self.assertEqual(war_game[0] in approved_strings, True, "Testing that element 0 of the tuple returned by the function play_war_game is one of 'Player1', 'Player2', 'Tie'")
    # are tup[1] and tup[2] of type integer
    def test_if_elements_1_and_2_of_war_game_tuple_are_integers(self):
        war_game = play_war_game(testing=True)
        self.assertEqual(type(war_game[1]), type(1), "Testing that element 1 of the tuple returned by the function play_war_game is of type integer")
        self.assertEqual(type(war_game[2]), type(1), "Testing that element 2 of the tuple returned by the function play_war_game is of type integer")
    # are tup[1] and tup[2] between 0 and 52, inclusive
    def test_if_elements_1_and_2_of_war_game_tuple_are_integers_between_0_and_52(self):
        war_game = play_war_game(testing=True)
        self.assertEqual(war_game[1] >= 0 and war_game[1] <= 52, True, "Testing that element 1 of the tuple returned by the function play_war_game is an integer between 0 and 52, inclusive")
        self.assertEqual(war_game[2] >= 0 and war_game[1] <= 52, True, "Testing that element 2 of the tuple returned by the function play_war_game is an integer between 0 and 52, inclusive")
    # if (e.g.) tup[0] is "Player 1", is tup[1] > tup[2]
    def test_if_play_war_game_scores_match_winner(self):
        war_games = ["war_game_1", "war_game_2", "war_game_3", "war_game_4", "war_game_5"]
        for war_game in war_games:
            war_game = play_war_game(testing=True)
            if war_game[1] > war_game[2]:
                self.assertEqual(war_game[0], "Player1", "Testing that if the integer element 1 of the tuple returend by the function play_war_game is greater than the integer element 2, then element 0 is the string 'Player1' (meaning that Player 1 won the game)")
            elif war_game[2] > war_game[1]:
                self.assertEqual(war_game[0], "Player2", "Testing that if the integer element 2 of the tuple returend by the function play_war_game is greater than the integer element 1, then element 0 is the string 'Player2' (meaning that Player 2 won the game)")
            elif war_game[1] == war_game[2]:
                self.assertEqual(war_game[0], "Tie", "Testing that if the integer elements 1 and 2 of the tuple returned by the function play-war_game are equal, then element 0 is the string 'Tie' (meaning that the two players tied the game)")

# test suite of function show_song
class test_function_show_song(unittest.TestCase):
    # does the show_song function return a Song object, with or without input
    def test_if_show_song_without_input_returns_a_song_object(self):
        dummy_song = show_song()
        self.assertIsInstance(dummy_song, helper_functions.Song, "Testing that the function show_song returns an instance of class Song if no input is given")
    def test_if_show_song_with_input_returns_a_song_object(self):
        chandelier_song = show_song("chandelier")
        self.assertIsInstance(chandelier_song, helper_functions.Song, "Testing that the function show_song returns an instance of class Song if input is given")

if __name__ == "__main__":
    unittest.main(verbosity=2)
