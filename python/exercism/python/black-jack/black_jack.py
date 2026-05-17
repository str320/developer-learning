"""Functions to help play and score a game of blackjack."""

def value_of_card(card):

    """Determine the scoring value of a card."""

    face_cards = ["J", "Q", "K"]

    if card.upper() in face_cards:
        return 10
        
    if card.upper() == "A":
        return 1

    return int(card)

def higher_card(card_one, card_two):

    """Determine which card has a higher value in the hand."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one

    if value_two > value_one:
        return card_two

    return card_one, card_two

def value_of_ace(card_one, card_two):

    """Calculate the most advantageous value for an upcoming ace card."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    value_cards = value_one + value_two

    ace_as_one = 1
    ace_as_eleven = 11

    if card_one.upper() == "A" or card_two.upper() == "A":
        return ace_as_one
    
    current_total = value_cards + ace_as_eleven

    if current_total <= 21:
        return ace_as_eleven
    
    return ace_as_one

def is_blackjack(card_one, card_two):

    """Determine if the hand is a 'natural' or 'blackjack'."""

    cards = [card_one.upper(), card_two.upper()]
    ten_cards = ['J', 'Q', 'K', "10"]
    ace = "A"

    has_ace = ace in cards
    has_ten_card = any(card in ten_cards for card in cards)

    return has_ace and has_ten_card

def can_split_pairs(card_one, card_two):

    """Determine if a player can split their hand into two hands."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two) 

    return value_one == value_two

def can_double_down(card_one, card_two):

    """Determine if a blackjack player can place a double down bet."""
    
    doubling = [9, 10, 11]

    total = value_of_card(card_one) + value_of_card(card_two) 

    return total in doubling