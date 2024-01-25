import flet as ft
import random

CARDS = { 

    1: ['Ace of Spades',13],
    2: ['2 of Spades', 2],
    3: ['3 of Spades', 3],
    4: ['4 of Spades', 4],
    5: ['5 of Spades', 5],
    6: ['6 of Spades', 6],
    7: ['7 of Spades', 7],
    8: ['8 of Spades', 8],
    9: ['9 of Spades', 9],
    10: ['10 of Spades', 10],
    11: ['Jack of Spades', 10],
    12: ['Queen of Spades', 10],
    13: ['King of Spades', 10],
    14: ['Ace of Hearts',13],
    15: ['2 of Hearts', 2],
    16: ['3 of Hearts', 3],
    17: ['4 of Hearts', 4],
    18: ['5 of Hearts', 5],
    19: ['6 of Hearts', 6],
    20: ['7 of Hearts', 7],
    21: ['8 of Hearts', 8],
    22: ['9 of Hearts', 9],
    23: ['10 of Hearts', 10],
    24: ['Jack of Hearts', 10],
    25: ['Queen of Hearts', 10],
    26: ['King of Hearts', 10],
    27: ['Ace of Clubs',13],
    28: ['2 of Clubs', 2],
    29: ['3 of Clubs', 3],
    30: ['4 of Clubs', 4],
    31: ['5 of Clubs', 5],
    32: ['6 of Clubs', 6],
    33: ['7 of Clubs', 7],
    34: ['8 of Clubs', 8],
    35: ['9 of Clubs', 9],
    36: ['10 of Clubs', 10],
    37: ['Jack of Clubs', 10],
    38: ['Queen of Clubs', 10],
    39: ['King of Clubs', 10],
    40: ['Ace of Diamonds',13],
    41: ['2 of Diamonds', 2],
    42: ['3 of Diamonds', 3],
    43: ['4 of Diamonds', 4],
    44: ['5 of Diamonds', 5],
    45: ['6 of Diamonds', 6],
    46: ['7 of Diamonds', 7],
    47: ['8 of Diamonds', 8],
    48: ['9 of Diamonds', 9],
    49: ['10 of Diamonds', 10],
    50: ['Jack of Diamonds', 10],
    51: ['Queen of Diamonds', 10],
    52: ['King of Diamonds', 10]

   
}

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

def deal_cards(cards, num_players, cards_per_player):
    return [[cards.pop(card) for card in random.sample(range(1, 53), cards_per_player)] for _ in range(num_players)]

p1CARD, dCARD = deal_cards(CARDS, 2, 2)

#main function
def app(page: ft.Page):


    #player cards
    p1c1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p1c2 = build_container(p1CARD[1][0], ft.colors.BLUE)

    dc1 = build_container(dCARD[0][0], ft.colors.BLUE)
    dc2 = build_container(dCARD[1][0], ft.colors.BLUE)

    winner = build_container("", ft.colors.BLACK)
     
    
    #function for when p1 hits 
    def p1HIT_BUTTON(e):

        new_card_info = CARDS.pop(random.choice(list(CARDS.keys())))
        hitCARD.insert(0, new_card_info)
        new_card = build_container(hitCARD[0][0], ft.colors.BLUE)
        pColumn1.content.controls.insert(-1, new_card)
        page.update()
        print(hitCARD)
        
    p1HIT_BUTTON = build_button("HIT", ft.colors.GREEN, callbac=p1HIT_BUTTON)
    
    #layout
    pColumn1 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player One"), size=16),
                        p1c1,
                        p1c2,
                        p1HIT_BUTTON,
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
        #page.controls.pop()
        page.update()
        page.add(
            pColumns,
            winnerROW,
        )
    
    page.add(
        ft.FilledButton(
            "play", 
            on_click=start_button,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
            ), 
    )

ft.app(target=app, view=ft.AppView.WEB_BROWSER)






