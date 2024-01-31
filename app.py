from itertools import product
import flet as ft
import random
import time


#funuction for generating deck
def generate_deck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    
    deck = {}
    card_id = 1

    for rank, suit in product(ranks, suits):
        card_name = f'{rank} of {suit}'
        value = get_card_value(rank)
        deck[card_id] = [card_name] + value
        card_id += 1

    return deck

#function for getting card values
def get_card_value(rank):
    if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return [int(rank)]
    elif rank in ['Jack', 'Queen', 'King']:
        return [10]
    elif rank == 'Ace':
        return [1, 11]

CARDS = generate_deck()

p1CARD = []
dCARD = []
hitCARD = []


#helper function to build containers
def build_container(name, color):
    return ft.Container(
        content=ft.Text(name),
        bgcolor=color,
        padding=15,
    )

#helper function to build buttons
def build_button(name, color, callbac=None):
    if callbac is None:
        button = ft.ElevatedButton(
            name,
            bgcolor=color,
        )
    else:
        button = ft.ElevatedButton(
            name,
            bgcolor=color,
            on_click=callbac
        )    
    return button

#function to "deal cards" to the players
def deal_cards(cards, num_players, cards_per_player):
    return [[cards.pop(card) for card in random.sample(range(1, 53), cards_per_player)] for _ in range(num_players)]

p1CARD, dCARD = deal_cards(CARDS, 2, 2)

p1TOTAL = float(p1CARD[0][1]) + float(p1CARD[1][1])
dTOTAL = float(dCARD[0][1]) + float(dCARD[1][1])

#main function
def app(page: ft.Page):

    def again_2():
        global CARDS, p1CARD, dCARD, hitCARD, p1TOTAL, dTOTAL

        # Generate a new deck
        CARDS = generate_deck()

        # Deal new cards to the player and dealer
        p1CARD, dCARD = deal_cards(CARDS, 2, 2)

        # Clear hit cards
        hitCARD = []

        #  Reset the player and dealer total values
        p1TOTAL = float(p1CARD[0][1]) + float(p1CARD[1][1])
        dTOTAL = float(dCARD[0][1]) + float(dCARD[1][1])

        # Update UI elements to reflect the new game state
        p1c1.content.value = p1CARD[0][0]
        p1c2.content.value = p1CARD[1][0]
        dc1.content.value = dCARD[0][0]
        dc2.content.value = ""

        # Reset pColumn1
        pColumn1.content.controls.clear()
        pColumn1.content.controls.append(ft.Text(("Player One"), size=16))
        pColumn1.content.controls.append(p1c1)
        pColumn1.content.controls.append(p1c2)
        pColumn1.content.controls.append(p1HIT_BUTTON)
        pColumn1.content.controls.append(p1STAND_BUTTON)
        
        # Clear winner message
        winner.content.value = ""

        # Update the page
        page.update()

    def countdown():
        time.sleep(4)
        winner.content.value = "5"
        page.update()
        time.sleep(1)
        winner.content.value = "4"
        page.update()
        time.sleep(1)
        winner.content.value = "3"
        page.update()
        time.sleep(1)
        winner.content.value = "2"
        page.update()
        time.sleep(1)
        winner.content.value = "1"
        page.update()
        time.sleep(1)

    #player cards
    p1c1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p1c2 = build_container(p1CARD[1][0], ft.colors.BLUE)

    dc1 = build_container(dCARD[0][0], ft.colors.BLUE)
    dc2 = build_container("", ft.colors.BLUE)

    winner = build_container("", ft.colors.BLACK)

    #function to decide who wins
    def checkcards():

        if p1TOTAL == dTOTAL:
            winner.content.value = "Tie"
        elif p1TOTAL == 21:
            winner.content.value = "Player One Wins (21)"
        elif dTOTAL == 21:
            winner.content.value = "Dealer Wins (21)"
        elif p1TOTAL > dTOTAL:
            winner.content.value = "Player One Wins (> dealer)"
        elif dTOTAL > p1TOTAL:
            winner.content.value = "Dealer Wins (> player)"

        dc2.content.value = dCARD[1][0]
        page.update() 
        countdown()
        again_2()
    
    #function for when p1 hits 
    def p1HIT_BUTTON(e):

        global p1TOTAL

        new_card_info = CARDS.pop(random.choice(list(CARDS.keys())))
        hitCARD.insert(0, new_card_info)
        new_card = build_container(hitCARD[0][0], ft.colors.BLUE)
        pColumn1.content.controls.insert(-2, new_card)
        p1TOTAL += int(hitCARD[0][1])
        if p1TOTAL > 21:
            winner.content.value = "Player One busts, Dealer Wins"
            dc2.content.value = dCARD[1][0]
            page.update()
            countdown()
            again_2()
        elif p1TOTAL == 21:
            winner.content.value = "Player One got blackjack"
            dc2.content.value = dCARD[1][0]
            page.update()
            countdown()
            again_2()


        page.update()


    #function for when p1 stands
    def p1STAND_BUTTON(e):

        checkcards()

        page.update()
        

    p1HIT_BUTTON = build_button("HIT", ft.colors.GREEN, callbac=p1HIT_BUTTON)
    p1STAND_BUTTON = build_button("STAND", ft.colors.GREEN, callbac=p1STAND_BUTTON)
    
    #layout
    pColumn1 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player One"), size=16),
                        p1c1,
                        p1c2,
                        p1HIT_BUTTON,
                        p1STAND_BUTTON,
                    ],
                ),
            )

    #layout
    pColumn2 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Dealer"), size=16),
                        dc1,
                        dc2,
                    ],
                ),
            )

    #layout
    pColumns = ft.Container(
                content=ft.Row(
                    [
                        pColumn1,
                        pColumn2,
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=400,
                ),
            )

    #layouot
    winnerROW = ft.Container(
        content=ft.Row(
            [
                winner,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )

    #function to start game
    def start_button(e):
        page.update()
        page.add(
            pColumns,
            winnerROW,
        )

    #function to restart the game
    def again(e):
        global CARDS, p1CARD, dCARD, hitCARD, p1TOTAL, dTOTAL

        # Generate a new deck
        CARDS = generate_deck()

        # Deal new cards to the player and dealer
        p1CARD, dCARD = deal_cards(CARDS, 2, 2)

        # Clear hit cards
        hitCARD = []

        #  Reset the player and dealer total values
        p1TOTAL = float(p1CARD[0][1]) + float(p1CARD[1][1])
        dTOTAL = float(dCARD[0][1]) + float(dCARD[1][1])

        # Update UI elements to reflect the new game state
        p1c1.content.value = p1CARD[0][0]
        p1c2.content.value = p1CARD[1][0]
        dc1.content.value = dCARD[0][0]
        dc2.content.value = ""

        # Reset pColumn1
        pColumn1.content.controls.clear()
        pColumn1.content.controls.append(ft.Text(("Player One"), size=16))
        pColumn1.content.controls.append(p1c1)
        pColumn1.content.controls.append(p1c2)
        pColumn1.content.controls.append(p1HIT_BUTTON)
        pColumn1.content.controls.append(p1STAND_BUTTON)
        
        # Clear winner message
        winner.content.value = ""

        # Update the page
        page.update()

    page.add(
        ft.FilledButton(
            "play", 
            on_click=start_button,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
            ), 
        ft.FilledButton(
            "again",
            on_click=again,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
            ),
    )

ft.app(target=app, view=ft.AppView.WEB_BROWSER)