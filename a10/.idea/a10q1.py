##
##===============================================
##  Benjamin Zhao (20901647)
##  CS 116 Spring 2021
##  Assignment 10, Problem Dealing
##===============================================
##

from numpy import random
import check


class Card:
    '''
    Fields:
       value (Str)
       suit (Str)
    Requires:
       value is one of "A", "2", "3", "4", "5",
          "6", "7", "8", "9", "10", "J", "Q", "K"
       suit is one of "C", "D", "H", "S"
    '''
    val = list('A') + [str(n) for n in range(2, 11)] + list('JQK')
    suits = ['C', 'D', 'H', 'S']

    def __init__(self, val, st):
        '''
        Initialized a card from a standard deck of 52 cards
        with value val and suit st.

        Effects: Mutates self

        __init__: Card Str Str -> None
        Requires:
           value is one of "A", "2", "3", "4", "5",
            "6", "7", "8", "9", "10", "J", "Q", "K"
           suit is one of "C", "D", "H", "S"
        '''
        self.value = val
        self.suit = st
        pass

    def __eq__(self, other):
        '''
        Returns True if self and other have equal values and suits
        and False otherwise

        __eq__: Card Any -> Bool
        '''
        return ((self.value == other.value) and (self.suit == other.suit))
        pass

    def __repr__(self):
        '''
        Returns a representation of a Card object

        __repr__: Card -> Str
        '''
        s = "spades"
        if self.suit == "C":
            s = "clubs"
        elif self.suit == "D":
            s = "diamonds"
        elif self.suit == "H":
            s = "hearts"
        return "{0.value} of {1}".format(self, s)


class Player:
    '''
    Fields:
       name (Str)
       hand (listof Card)
    Requires:
       name is one of "North", "East", "South", "West"
       0 <= len(hand) <= 13
       Elements of hand do not repeat
    '''

    def __init__(self, player_name, player_hand):
        '''
        Initialize a valid Player with name player_name
        and hand player_hand
       h       1111111111119340000
        Effects: Mutates self

        __init__: Str (anyof Str None) -> None
        Requires: Conditions from Fields above are met.
        '''
        self.name = player_name
        self.hand = player_hand

    def __eq__(self, other):
        '''
        Returns True if self and other have equal names and hands
        and False otherwise. Note that the hands might not be
        in any sorted order and so comparison should return True
        if the hands contain the same cards even if in a different
        order.

        __eq__: Player Any -> Bool
        '''
        return ((self.name ==  other.name) and (self.hand == other.hand))
        pass


    def __repr__(self):
        '''
        Returns a representation of a Player object

        __repr__: Card -> Str
        '''
        return "Player: {0.name} Hand: {0.hand}".format(self)

    def play_card(self, card):
        '''
        Returns True if the card is in self's hand
        and removes it from their hand. False otherwise
        with no mutation.

        Effects:
           Mutates self.hand

        play_card: Player Card -> Bool

        Examples:
           p = Player("North", [Card("A", "C"),
                                Card("2", "C"), Card("3", "C")])
           p.play_card(Card("A", "C")) => True
           and p.hand is mutated to
           [Card("2", "C"), Card("3", "C")]

           p = Player("North", [Card("A", "C"),
                                Card("2", "C"), Card("3", "C")])
           p.play_card(Card("7", "C")) => False
           and p.hand is not mutated
        '''

        if card in self.hand:
            self.hand.remove(card)
            return True
        else:
            return False
        pass


    ##END OF CLASSES


def convert_to_card(n):
    '''
    Returns the card in the deck according to the
    transformation scheme described on this page
    for value n.

    convert_to_card: Nat -> Card
    Requires: 1 <= n <= 52

    Example:
       convert_to_card(1) => Card("A", "C")
       convert_to_card(52) => Card("K", "S")
    '''

    SUIT = None
    VALUE = None

    if 1 <= n <= 13:
        SUIT = 'C'
        VALUE = Card.val[n-1]
    elif 14 <= n <= 26:
        SUIT = 'D'
        VALUE = Card.val[n-14]
    elif 27 <= n <= 39:
        SUIT = 'H'
        VALUE = Card.val[n-27]
    elif 40 <= n <= 52:
        SUIT = 'S'
        VALUE = Card.val[n-40]

    ##print(SUIT)
    ##print(VALUE)
    return Card(VALUE,SUIT)

    #pass

def deal(cards, players):
    '''
    Deals the cards to the players. The cards should
    be dealt in order with the first player receiving the first
    card, the second player receiving the second card and so on.
    This should mutate players[k].hand for each k to receive the
    dealt cards

    Effects: Mutates players[k].hands for each k

    deal: (listof Card) (listof Players) -> None
    Requires: num_players > 1

    Examples:
       P = [Player("North", []), Player("East", []), Player("South", [])]
       deal([], P) => None
       and P is unchanged

       P = [Player("North", []), Player("East", [])]
       L = [Card("A", "C"), Card("2", "C"),
            Card("3", "C"), Card("4", "C")]
       deal(L, P) => None
       and P is mutated to
       P = [Player("North", [Card("A", "C"), Card("3", "C")]),
            Player("East", [Card("2", "C"), Card("4", "C")])]

       P = [Player("North", []), Player("East", []),
            Player("South", []), Player("West", [])]
       L = [Card("A", "C"), Card("2", "C"),
            Card("3", "C"), Card("4", "C") , Card("5", "C")]
       deal(L, P) => None
       and P is mutated to
       P = [Player("North", [Card("A", "C"), Card("5", "C")]),
            Player("East", [Card("2", "C")])
            Player("South", [Card("3", "C")])
            Player("West", [Card("4", "C")])]
    '''

    ##YOUR CODE GOES HERE

    num_players = len(players)
    num_cards = len(cards)

    if num_cards == 0 or num_players == 0:
        pass
    else:

        expected_num_of_cards_assigned_to_each_player = int(num_cards//num_players)

        for card_code in range(num_cards):
            players[card_code%num_players].hand.append(cards[card_code])

        #for player_code in range(num_players):
        #for card_code in range(expected_num_of_cards_assigned_to_each_player):
        #card_index = random.randint(0,len(cards))
        #print(card_index)
        #players[player_code].hand.append(cards[card_index])
        #cards.remove(cards[card_index])

    pass



def display_hand(hand):
    '''
    Displays a hand of cards in a nice format
-
    Effeects: Prints to the screen

    display_hand: (listof Card) -> None

    Example:
       display_hand([Card("A", "C"),
                     Card("10", "C"), Card("4", "S")]) => None
       and the following is printed:
       ♠ 4
       ♥ -
       ♦ -
       ♣ A 10
    '''
    ##YOUR CODE GOES HERE

    str = ""

    suit_symbol = ["♠","♥","♦", "♣"]
    suits = ['S', 'H', 'D', 'C']
    cards_by_suit = [],[],[],[]

    for card in hand:
        symbol_code = card.suit
        value = card.value
        #for symbol in suit_symbol:
        cards_by_suit[suits.index(symbol_code)].append(card)

    for i in range(len(suit_symbol)):
        str = suit_symbol[i]
        if(len(cards_by_suit[i])==0):
            str += " -"
        else:
            for i1 in range(len(cards_by_suit[i])):
                str += " " + cards_by_suit[i][i1].value
        print(str)
    pass

def shuffle(seed = None):
    '''
    Returns a list of 52 cards in random order based on the seed
    if provided.
    Note that the return type should be Card 52 times but for
    brevity we write this as (listof Card).

    shuffle: [(anyof Nat None)] -> (listof Card)
    '''
    num_cards = 52
    L = list(range(1, num_cards + 1))
    random.seed(seed)
    return list(map(convert_to_card, random.permutation(L)))


def deal_bootstrap(deck = []):
    '''
    Simulate a deal of a bridge game with North, East, South and West.
    Optional parameter deck should be a permutation of numbers from 1 to 52
    to be a proper simulation. Can have smaller size and repeats however if
    desired.

    deal_bootstrap: [(listof Nat)] -> (list Player Player Player Player)
    Requires:
       1 <= deck[i] <= 52 for all indices i
    '''
    invalid_response = "Invalid response."
    random_prompt = "Do you want to use a (r)andom deal or a (p)redefined deal? "
    random_seed = \
        "Do you want to use a fixed seed? Enter (n)o or a natural number: "
    dealer_prompt = "Who is the dealer? (N)orth, (E)ast, (S)outh, (W)est? "
    dealer_dict = {'N': 'North', 'S': 'South', 'E':'East', 'W': 'West'}
    PLAYERS = list(dealer_dict.values())


    random = input(random_prompt)
    while random not in ['r', 'p']:
        print(invalid_response)
        random = input(random_prompt)
    if random == 'r':
        s = input(random_seed)
        while s != 'n' and not s.isnumeric() and int(s) < 0:
            print(invalid_response)
            s = input(random_seed)
        if s == 'n':
            s = None
        else:
            s = int(s)
        deck = shuffle(s)
    else:
        deck = list(map(convert_to_card, deck))
    dealer = input(dealer_prompt)
    while dealer not in ['N', 'E', 'S', 'W']:
        print(invalid_response)
        dealer = input(dealer_prompt)
    dealer = dealer_dict[dealer]

    ##Dealer is last player in list to work with dealer:

    player_index = PLAYERS.index(dealer)
    player_names = PLAYERS[player_index + 1:] + PLAYERS[:player_index+1]
    player_list = list(map(lambda x: Player(x, []), player_names))

    deal(deck, player_list)
    return player_list



##Test for Card:

c = Card("A", "C")
check.expect("Test AC", c.value, "A")
check.expect("Test AC", c.suit, "C")

##Test for __eq__ for Card

c = Card("10", "C")
d = Card("7", "D")
e = Card("10", "C")
check.expect("Test not equal random", c == d, False)
check.expect("Test equal", c == e, True)

##Test __eq__ for Player

p1 = Player("North", [Card("A", "C"), Card("2", "C")])
p2 = Player("North", [Card("A", "C"), Card("2", "C")])
check.expect("Test equal basic", p1==p2, True)

p1 = Player("North", [Card("A", "C"), Card("2", "C")])
p2 = Player("South", [Card("A", "C"), Card("2", "C")])
check.expect("Test unequal name basic", p1==p2, False)

p1 = Player("North", [Card("A", "C"), Card("2", "C")])
p2 = Player("North", [Card("A", "C"), Card("3", "C")])
check.expect("Test unequal hand basic", p1==p2, False)


##Tests convert_to_card:


check.expect("Test AC", convert_to_card(1), Card("A", "C"))
check.expect("Test KS", convert_to_card(52), Card("K", "S"))

##Tests play_card:
p = Player("North", [Card("A", "C"),
                     Card("2", "C"), Card("3", "C")])
check.expect("Test play_card True", p.play_card(Card("A", "C")), True)
check.expect("Test play_card True Mutation", p, Player("North", [Card("2", "C"),
                                                                 Card("3", "C")]))

p = Player("North", [Card("A", "C"),
                     Card("2", "C"), Card("3", "C")])
check.expect("Test play_card False", p.play_card(Card("7", "C")), False)
check.expect("Test play_card False No Mutation", p, Player("North", [Card("A", "C"),
                                                                     Card("2", "C"),
                                                                     Card("3", "C")]))

##Tests deal:


P = [Player("North", []), Player("East", []), Player("South", [])]
check.expect("Test deal Simple", deal([], P), None)
check.expect("Test deal Simple no mutation", P,
             [Player("North", []), Player("East", []), Player("South", [])])

L = [Card("A", "C"), Card("2", "C"),
     Card("3", "C"), Card("4", "C")]
P = [Player("North", []), Player("East", [])]

check.expect("Test deal Simple", deal(L, P), None)
check.expect("Test deal Simple Mutation", P,
             [Player("North", [Card("A", "C"), Card("3", "C")]),
              Player("East", [Card("2", "C"), Card("4", "C")])] )

L = [Card("A", "C"), Card("2", "C"),
     Card("3", "C"), Card("4", "C") , Card("5", "C")]
P = [Player("North", []), Player("East", []),
     Player("South", []), Player("West", [])]

check.expect("Test deal Simple", deal(L, P), None)
check.expect("Test deal Simple Mutation", P,
             [Player("North", [Card("A", "C"), Card("5", "C")]),
              Player("East", [Card("2", "C")]),
              Player("South", [Card("3", "C")]),
              Player("West", [Card("4", "C")])])


##Test for display_hand

L = [Card("A", "C"), Card("10", "C"), Card("4", "S")]
check.set_print_exact("♠ 4", "♥ -", "♦ -","♣ A 10")
check.expect("Test example", display_hand(L), None)

