##
##===============================================
##  Benjamin Zhao (20901647)
##  CS 116 Spring 2021
##  Assignment 10, Problem Bidding
##===============================================
##

from a10q1 import *
import check


class Bid:
    '''
    Fields:
       value (Str)
       suit (anyof Str None)
    Requires:
       value is one of "1", "2", "3", "4", "5", "6", "7",
           "pass", "double", "redouble"
       suit is one of "C", "D", "H", "S", "NT" or None
       If value is non-numeric, then suit must be None
    '''

    value_rank = ["pass","1","2","3","4","5","6","7","double","redouble"]

    num_rank = ["1", "2", "3", "4", "5", "6", "7"]

    suit_rank = [None,"C","D","H","S","NT"]

    def __init__(self, bid_value, bid_suit):
        '''
        Initialized a valid Bridge bid.

        Effects: Mutates self

        __init__: Bid Str (anyof Str None) -> None
        Requires: Conditions from Fields above are met.
        '''

        self.value = bid_value
        self.suit = bid_suit

        pass



    def __repr__(self):
        '''
        Returns a representation of a Card object

        __repr__: Card -> Str
        '''
        if self.suit == None:
            return "{0.value}".format(self)
        return "{0.value}{0.suit}".format(self)

    def __eq__(self, other):
        '''
        Returns True if self and other have equal values and suits
        and False otherwise

        __eq__: Bid Any -> Bool
        '''
        return ((self.value == other.value) and (self.suit == other.suit))
        pass

    def __lt__(self, other):

        '''
        Returns True if both self and other are numeric bids and
        self is a bid that comes before other. False otherwise

        __lt__: Bid Any -> Bool
        '''

        #if(self.value.isnumeric() and other.value.isnumeric()):

        if(self==other):
            return False
        else:
            if(self.value in Bid.value_rank and other.value in Bid.value_rank):
                if Bid.value_rank.index(other.value) > Bid.value_rank.index(self.value):
                    return True
                elif Bid.value_rank.index(other.value) == Bid.value_rank.index(self.value):
                    if Bid.suit_rank.index(other.suit) > Bid.suit_rank.index(self.suit):
                        return True
                else:
                    return False
            else:
                return False

    pass

def valid_bid(bids, new_bid):
    '''
    Returns True if new_bid is allowed in a Bridge
    game given the previous bids in bids. False otherwise

    valid_bid: (listof Bid) Bid -> Bool
    Requires:
       For all k from 0 to len(bids) - 1,
         valid_bid(bids[:k], bids[k]) => True

    Examples:
       valid_bid([],Bid("pass", None)) => True
       valid_bid([Bid("pass", None), Bid("pass", None),
                   Bid("pass", None)], Bid("pass", None))
                    => True
       valid_bid([Bid("1", "C"), Bid("pass", None),
                   Bid("pass", None), Bid("pass", None)],
                    Bid("pass", None)) => False
       valid_bid([Bid("7", "NT")], Bid("2", "H")) => False
       valid_bid([Bid("1", "C"), Bid("pass", None)],
                   Bid("double", None)) => False
       valid_bid([Bid("1", "C"), Bid("pass", None),
                   Bid("pass", None)], Bid("double", None))
                     => True
    '''


    if len(bids) == 4:
        return False

    if len(bids) == 0:
        return new_bid.value not in ['double', 'redouble']

    maximum_bid = bids[0]

    for i in range(len(bids)):
        bid = bids[i]
        print(bids)
        print(Bid.value_rank.index(bid.value))
        print("FUCK")
        if(0<Bid.value_rank.index(bid.value)<8):
            if(bid > maximum_bid):
                maximum_bid = bid
        elif(Bid.value_rank.index(bid.value)==8):
            #Double must be following a numeric bid
            print("In!!!!")
            if not (0<Bid.value_rank.index(bids[i-1].value)<8):

                return False
        elif(Bid.value_rank.index(bid.value)==8):
            #ReDouble must be following a dobule
            if not (Bid.value_rank.index(bids[i-1].value)==8):
                return False


    if(new_bid > maximum_bid):
        return True
    elif Bid.value_rank.index(new_bid.value) == 0:
        return True
    else:
        return False

    '''
    if len(bids) == 0:
        return new_bid.value not in ['double', 'redouble']
    if new_bid.value == 'double':
        return not ((len(bids) == 1 and bids[0].value == 'pass') or (len(bids) >= 2 and bids[len(bids)-2].value in\
                                                                     Bid.num_rank))
    if new_bid.value == 'redouble':
        return not ((len(bids) ==1) or (len(bids) >= 2 and ((bids[len(bids)-2].value in Bid.Numeric_value and \
                                                             bids[len(bids)-3].value == 'double'))))
    if new_bid.value in Bid.value_rank:
        return (bids[len(bids)-1] < new_bid or bids[len(bids)-1].value in ['pass', 'double', 'redouble']) and \
               (bids[len(bids)-2] < new_bid or bids[len(bids)-2].value in ['pass', 'double', 'redouble']) and \
               (bids[len(bids)-3] < new_bid or bids[len(bids)-3].value in ['pass', 'double', 'redouble'])
    if len(bids) >= 4 and all([i.value == 'pass' for i in bids[l-3:len(bids)]]):
        return False
    return True
    pass
    '''


def bidding_complete(bids):
    '''
    Returns True if bids represents a complete contract and False otherwise

    bidding_complete: (listof Bid) -> Bool
    Requires:
       For all k from 0 to len(bids) - 1,
         valid_bid(bids[:k], bids[k]) => True

    Examples:
       bidding_complete([Bid("pass", None), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)]) => True
       bidding_complete([Bid("1", "C"), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)]) => True
       bidding_complete([Bid("1", "C"), Bid("3", "NT"),
                  Bid("pass", None), Bid("pass", None)]) => False
    '''

    for i in range(len(bids)-1):
        valid = valid_bid(bids[0:i],bids[i+1])
        if valid == False:
            return False
    return True

    pass


def contract(bids):
    '''
    Returns the contract to be played, including any doubling
    or redoubling that occurred.

    contract: (listof Bid) -> (list Bid (anyof Bid None))
    Requires:
       For all k from 0 to len(bids) - 1,
         valid_bid(bids[:k], bids[k]) => True
       bidding_complete(bids) => True

    Examples:
       contract([Bid("pass", None), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)])
                    => [Bid("pass", None), None]
       contract([Bid("1", "C"), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)])
                    => [Bid("1", "C"), None]
       contract([Bid("1", "C"), Bid("double", None),
                  Bid("pass", None), Bid("pass", None),
                  Bid("pass", None)])
                    => [Bid("1", "C"), Bid("double", None)]
       contract([Bid("1", "C"), Bid("double", None),
                  Bid("redouble", None), Bid("pass", None),
                  Bid("pass", None),  Bid("pass", None)])
                   => [Bid("1", "C"), Bid("redouble", None)]
       contract([Bid("1", "C"), Bid("double", None),
                  Bid("redouble", None), Bid("1", "S"),
                  Bid("pass", None), Bid("pass", None),
                  Bid("pass", None)]) => [Bid("1", "S"), None]
    '''
    ##YOUR CODE GOES HERE

    maximum_bid = []
    maximum_bid.append(bids[0])
    doubling_bids = []
    passing_bids = []

    for bid in bids:
        if(bid > maximum_bid[0]):
            maximum_bid[0] = bid
        elif(Bid.value_rank.index(bid.value)>=8):
            doubling_bids.append(bid)
        else:
            passing_bids.append(bid)
    if(len(passing_bids)==len(bids)):
        return None
    return maximum_bid + doubling_bids


    pass



##PROVIDED FUNCTIONS BELOW - DO NOT CHANGE

def declarer(starting_team, bids):
    '''
    Returns who the declarer is given the starting_team
    and the bids. Returns None if all passed contract.

    declarer: Str (listof Bid) -> (anyof Str None)
    Requires:
       starting_team is one of "North", "East", "South" or "West"
       For all k from 0 to len(bids) - 1,
         valid_bid(bids[:k], bids[k]) => True
       bidding_complete(bids) => True

    Examples:
       declarer("North", [Bid("pass", None), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)]) => None
       declarer("North", [Bid("1", "C"), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)]) => "North"
       declarer("North", [Bid("1", "C"), Bid("2", "C"),
                  Bid("3", "C"), Bid("pass", None),
                  Bid("pass", None), Bid("pass", None)]) => "North"
    '''
    all_pass = [Bid("pass", None)]*len(bids)
    if all_pass == bids:
        print("ALL PAAA")
        return None
    deal_contract = contract(bids)
    players = ["North", "East", "South", "West"]
    winning_team = None
    cur_dir = starting_team
    for i in bids:
        if i == deal_contract[0]:
            winning_team = cur_dir
        cur_dir = players[(players.index(cur_dir) + 1) % len(players)]

    winning_team = [winning_team,
                    players[(players.index(winning_team) + 2) % len(players)]]
    cur_dir = starting_team
    for i in bids:
        if i.suit == deal_contract[0].suit and cur_dir in winning_team:
            return cur_dir
        cur_dir = players[(players.index(cur_dir) + 1) % len(players)]



def bidding_bootstrap(deck = []):
    '''
    Performs a deal and bidding sequence for Bridge.
    Bids should be made of the format #S, pass, double or redouble
    where # is a number from 1 to 7 and S is a suit C, D, H, S, NT.

    bidding_bootstrap: [(listof Nat)] -> (list Player Player Player Player)
    Requires:
       1 <= deck[i] <= 52 for all indices i.
    '''
    SUITS = ['C', 'D', 'H', 'S']
    players = deal_bootstrap(deck) #From a10q1
    invalid_response = "Invalid response."
    invalid_bid_response = "Invalid bid."
    bid_prompt = "Please enter a valid bid for {0}: "
    odd_bids = ['pass', 'double', 'redouble']
    bids = []
    num_players = len(players)
    starting_player = num_players - 1
    while not bidding_complete(bids):
        print("{0}'s hand: ".format(players[starting_player].name))
        display_hand(players[starting_player].hand)
        bid = input(bid_prompt.format(players[starting_player].name))

        def good_bid_input(bid):
            '''
            Local helper function to determine a good bid

            good_bid_input: Str -> Bool
            '''
            num = bid[0]
            suit = bid[1:]
            if bid in odd_bids:
                return True
            elif num not in ['1', '2', '3', '4', '5', '6', '7'] or \
                    suit not in SUITS:
                return False
            return True

        while not good_bid_input(bid):
            print(invalid_response)
            print("{0}'s hand: ".format(players[starting_player].name))
            display_hand(players[starting_player].hand)
            bid = input(bid_prompt.format(players[starting_player].name))
        if bid in odd_bids:
            bid = Bid(bid, None)
        else:
            num = bid[0]
            suit = bid[1:]
            bid = Bid(num, suit)
        if not valid_bid(bids, bid):
            print(invalid_bid_response)
        else:
            bids.append(bid)
            starting_player = (starting_player + 1) % num_players
    return [players, bids]


## Examples for __eq__
c = Bid("1", "C")
d = Bid("1", "D")
e = Bid("1", "C")
f = Bid("pass", None)
check.expect("Test unequal", c == d, False)
check.expect("Test equal", c == e, True)
check.expect("Test against pass", c == f, False)

## Examples for __lt__
check.expect("Test lt true", c < d, True)
check.expect("Test lt false", c < e, False)
check.expect("Test lt pass", c < f, False)

## Examples for Valid Bid

check.expect("Test on empty", valid_bid([],Bid("pass", None)), True)
check.expect("Test on empty double", valid_bid([],Bid("double", None)), False)
check.expect("Test on empty redouble",
             valid_bid([],Bid("redouble", None)), False)
check.expect("Test all pass",
             valid_bid([Bid("pass", None), Bid("pass", None),
                        Bid("pass", None)], Bid("pass", None)), True)
check.expect("Test passes after bid",
             valid_bid([Bid("1", "C"), Bid("pass", None),
                        Bid("pass", None), Bid("pass", None)],
                       Bid("pass", None)), False)
check.expect("Test bid after max", valid_bid([Bid("7", "NT")],
                                             Bid("2", "H")), False)
check.expect("Test invalid double",
             valid_bid([Bid("1", "C"), Bid("pass", None)],
                       Bid("double", None)), False)
check.expect("Test valid double",
             valid_bid([Bid("1", "C"), Bid("pass", None), Bid("pass", None)],
                       Bid("double", None)), True)

## Examples contract`


check.expect("Test all pass",
             contract([Bid("pass", None), Bid("pass", None),
                       Bid("pass", None), Bid("pass", None)]),
             [Bid("pass", None), None])


check.expect("Test simple contract",
             contract([Bid("1", "C"), Bid("pass", None),
                       Bid("pass", None), Bid("pass", None)]) ,
             [Bid("1", "C"), None])

check.expect("Test simple doubled",
             contract([Bid("1", "C"), Bid("double", None),
                       Bid("pass", None), Bid("pass", None),
                       Bid("pass", None)]) ,
             [Bid("1", "C"), Bid("double", None)])

check.expect("Test simple redoubled",
             contract([Bid("1", "C"), Bid("double", None),
                       Bid("redouble", None), Bid("pass", None),
                       Bid("pass", None),  Bid("pass", None)]) ,
             [Bid("1", "C"), Bid("redouble", None)])

check.expect("Test simple redoubled rebid",
             contract([Bid("1", "C"), Bid("double", None),
                       Bid("redouble", None), Bid("1", "S"),
                       Bid("pass", None), Bid("pass", None),
                       Bid("pass", None)]),
             [Bid("1", "S"), None])

## Examples Declarer

check.expect("Test all pass",
             declarer("North",
                      [Bid("pass", None), Bid("pass", None),
                       Bid("pass", None), Bid("pass", None)]),
             None)

check.expect("Test Simple 1C",
             declarer("North", [Bid("1", "C"), Bid("pass", None),
                                Bid("pass", None), Bid("pass", None)]), "North")

check.expect("Test Simple 3C",
             declarer("North", [Bid("1", "C"), Bid("2", "C"),
                                Bid("3", "C"), Bid("pass", None),
                                Bid("pass", None), Bid("pass", None)]), "North")


## Examples bidding_complete

check.expect("Example empty", bidding_complete([]), False)
check.expect("Example all-pass",
             bidding_complete([Bid("pass", None), Bid("pass", None),
                               Bid("pass", None), Bid("pass", None)]), True)
check.expect("Example bid three pass",
             bidding_complete([Bid("1", "C"), Bid("pass", None),
                               Bid("pass", None), Bid("pass", None)]), True)
check.expect("Example incomplete",
             bidding_complete([Bid("1", "C"), Bid("3", "NT"),
                               Bid("pass", None), Bid("pass", None)]), False)