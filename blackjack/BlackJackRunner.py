from Chip import Chip
from Deck import Deck
from Hand import Hand

playing = True


def show_card(player, dealer):
    print('player {}'.format(player))
    print('dealer {}\n\n'.format(dealer))


def take_bet(chip):
    while True:
        try:
            chip.bet = int(input('how many chips would you like to bet? '))
        except ValueError:
            print('Sorry provide numbers')
        else:
            if chip.bet > chip.total:
                print("Sorry you don't have enought chips! you have : {}".format(chip.total))
            else:
                break


def hit_hand(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing
    user_input = input('Hit or Stand? Enter h or s : ')

    if user_input[0].lower() == 'h':
        hit_hand(deck, hand)
    elif user_input[0].lower() == 's':
        print('Dealer chance')
        playing = False


def player_busted(player, dealer, chip):
    print('PLAYER BUSTED')
    chip.lose_bet()


def player_won(player, dealer, chip):
    print('PLAYER WON')
    chip.win_bet()


def dealer_busted(player, dealer, chip):
    print('DEALER BUSTED')
    chip.win_bet()


def dealer_won(player, dealer, chip):
    print('DEALER WON')
    chip.lose_bet()


def push(player, dealer):
    print('Dealer and player TIE! PUSH')


def play():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    player_chip = Chip()
    take_bet(player_chip)

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_card(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_card(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busted(player_hand, dealer_hand, player_chip)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit_hand(deck, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busted(player_hand, dealer_hand, player_chip)
        elif dealer_hand.value > player_hand.value:
            dealer_won(player_hand, dealer_hand, player_chip)
        elif dealer_hand.value < player_hand.value:
            player_won(player_hand, dealer_hand, player_chip)
        else:
            push(player_hand, dealer_hand)

    print('player total chips are at {}'.format(player_chip.total))


play()
