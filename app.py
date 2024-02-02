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
        return [1]

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
    try:
        return [[cards.pop(card) for card in random.sample(range(1, 53), cards_per_player)] for _ in range(num_players)]
    except KeyError:
        print("key error trying again")
        return deal_cards(CARDS, 2, 2) 

#deals cards to players
p1CARD, dCARD = deal_cards(CARDS, 2, 2)

p1TOTAL = float(p1CARD[0][1]) + float(p1CARD[1][1])
dTOTAL = float(dCARD[0][1]) + float(dCARD[1][1])

#main function
def app(page: ft.Page):

    #2nd function to restart the game
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
        pColumn1.content.controls.append(ft.Text((f"Total: {p1TOTAL}"), size=16)),
        pColumn1.content.controls.append(ft.Text(("Player One"), size=16))
        pColumn1.content.controls.append(p1c1)
        pColumn1.content.controls.append(p1c2)
        pColumn1.content.controls.append(p1HIT_BUTTON)
        pColumn1.content.controls.append(p1STAND_BUTTON)
        
        # Reset pColumn2
        pColumn2.content.controls.clear()
        pColumn2.content.controls.append(ft.Text(("Dealer"), size=16))
        pColumn2.content.controls.append(dc1)
        pColumn2.content.controls.append(dc2)
        
        # Clear winner message
        winner.content.value = ""

        # Update the page
        page.update()

    #countdown till next game
    def countdown():
        time.sleep(2)
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
        again_2()

    #aces are 1 or 11
    def aces_player1():

        global p1TOTAL

        for i in p1CARD:
            if i[1] == 1:
                if p1TOTAL + 10 > 21:
                    p1TOTAL += 0 
                elif p1TOTAL + 10 < 21:
                    p1TOTAL += 10
                    pColumn1.content.controls[0].value = f"Total: {p1TOTAL}"
                elif p1TOTAL + 10 == 21:
                    p1TOTAL += 10
                    pColumn1.content.controls[0].value = f"Total: {p1TOTAL}"
        page.update()
        
    #aces are 1 or 11
    def aces_dealer():

        global dTOTAL

        for i in dCARD:
            if i[1] == 1:
                if dTOTAL + 10 > 21:
                    return 
                elif dTOTAL + 10 < 21:
                    dTOTAL += 10
                    return True
                elif dTOTAL + 10 == 21:
                    dTOTAL += 10
                    return True


    #player cards
    p1c1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p1c2 = build_container(p1CARD[1][0], ft.colors.BLUE)

    dc1 = build_container(dCARD[0][0], ft.colors.BLUE)
    dc2 = build_container("", ft.colors.BLUE)

    winner = build_container("", ft.colors.BLACK)

    #function for deal hit/stand (automated)
    def dealer():
        
        global dTOTAL


        while dTOTAL < 16:
            if aces_dealer() == True:
                break
            new_card_info = CARDS.pop(random.choice(list(CARDS.keys())))
            hitCARD.insert(0, new_card_info)
            new_card = build_container(hitCARD[0][0], ft.colors.BLUE)
            pColumn2.content.controls.append(new_card)
            dTOTAL += int(hitCARD[0][1])
            page.update()
            time.sleep(1)

        dc2.content.value = dCARD[1][0]
        page.update()
        checkcards()
        
    #function to decide who wins
    def checkcards():
        global p1TOTAL, dTOTAL

        if p1TOTAL == dTOTAL:
            winner.content.value = "Tie"
        elif dTOTAL == 21:
            winner.content.value = "Dealer got Blackjack"
        elif dTOTAL > 21:
            winner.content.value = "Dealer busts, Player One Wins"
        elif dTOTAL > p1TOTAL:
            winner.content.value = "Dealer Wins"
        elif p1TOTAL > dTOTAL:
            winner.content.value = "Player One Wins (> dealer)" 

        page.update()
        countdown()

    #function for when p1 hits 
    def p1HIT_BUTTON(e):

        global p1TOTAL

        new_card_info = CARDS.pop(random.choice(list(CARDS.keys())))
        hitCARD.insert(0, new_card_info)
        new_card = build_container(hitCARD[0][0], ft.colors.BLUE)
        pColumn1.content.controls.insert(-2, new_card)
        p1TOTAL += int(hitCARD[0][1])
        page.update()
        pColumn1.content.controls[0].value = f"Total: {p1TOTAL}"
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

        aces_player1()
        dealer()
        
    p1HIT_BUTTON = build_button("HIT", ft.colors.GREEN, callbac=p1HIT_BUTTON)
    p1STAND_BUTTON = build_button("STAND", ft.colors.GREEN, callbac=p1STAND_BUTTON)
    
    #layout
    pColumn1 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text((f"Total: {p1TOTAL}"), size=16),
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
        pColumn1.content.controls.append(ft.Text((f"Total: {p1TOTAL}"), size=16)),
        pColumn1.content.controls.append(ft.Text(("Player One"), size=16))
        pColumn1.content.controls.append(p1c1)
        pColumn1.content.controls.append(p1c2)
        pColumn1.content.controls.append(p1HIT_BUTTON)
        pColumn1.content.controls.append(p1STAND_BUTTON)
        
        # Reset pColumn2
        pColumn2.content.controls.clear()
        pColumn2.content.controls.append(ft.Text(("Dealer"), size=16))
        pColumn2.content.controls.append(dc1)
        pColumn2.content.controls.append(dc2)



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