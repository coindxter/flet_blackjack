import flet as ft
import random

CARDS = { 

    1: ['Ace of Spades',13, 1],
    2: ['2 of Spades', 1, 1],
    3: ['3 of Spades', 2, 1],
    4: ['4 of Spades', 3, 1],
    5: ['5 of Spades', 4, 1],
    6: ['6 of Spades', 5, 1],
    7: ['7 of Spades', 6, 1],
    8: ['8 of Spades', 7, 1],
    9: ['9 of Spades', 8, 1],
    10: ['10 of Spades', 9, 1],
    11: ['Jack of Spades', 10, 1],
    12: ['Queen of Spades', 11, 1],
    13: ['King of Spades', 12, 1],
    14: ['Ace of Hearts', 13, 2],
    15: ['2 of Hearts', 1, 2],
    16: ['3 of Hearts', 2, 2],
    17: ['4 of Hearts', 3, 2],
    18: ['5 of Hearts', 4, 2],
    19: ['6 of Hearts', 5, 2],
    20: ['7 of Hearts', 6, 2],
    21: ['8 of Hearts', 7, 2],
    22: ['9 of Hearts', 8, 2],
    23: ['10 of Hearts', 9, 2],
    24: ['Jack of Hearts', 10, 2],
    25: ['Queen of Hearts', 11, 2],
    26: ['King of Hearts', 12, 2],
    27: ['Ace of Clubs', 13, 3],
    28: ['2 of Clubs', 1, 3],
    29: ['3 of Clubs', 2, 3],
    30: ['4 of Clubs', 3, 3],
    31: ['5 of Clubs', 4, 3],
    32: ['6 of Clubs', 5, 3],
    33: ['7 of Clubs', 6, 3],
    34: ['8 of Clubs', 7, 3],
    35: ['9 of Clubs', 8, 3],
    36: ['10 of Clubs', 9, 3],
    37: ['Jack of Clubs', 10, 3],
    38: ['Queen of Clubs', 11, 3],
    39: ['King of Clubs', 12, 3],
    40: ['Ace of Diamonds', 13, 4],
    41: ['2 of Diamonds', 1, 4],
    42: ['3 of Diamonds', 2, 4],
    43: ['4 of Diamonds', 3, 4],
    44: ['5 of Diamonds', 4, 4],
    45: ['6 of Diamonds', 5, 4],
    46: ['7 of Diamonds', 6, 4],
    47: ['8 of Diamonds', 7, 4],
    48: ['9 of Diamonds', 8, 4],
    49: ['10 of Diamonds', 9, 4],
    50: ['Jack of Diamonds', 10, 4],
    51: ['Queen of Diamonds', 11, 4],
    52: ['King of Diamonds', 12, 4],

}


p1total = 0

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

#main function
def app(page: ft.Page):

    #player cards
    p1c1 = build_container(CARDS.pop(random.choice(list(CARDS.keys())))[0], ft.colors.BLUE)
    p1c2 = build_container(CARDS.pop(random.choice(list(CARDS.keys())))[0], ft.colors.BLUE)
    

    p2c1 = build_container(CARDS.pop(random.choice(list(CARDS.keys())))[0], ft.colors.BLUE)
    p2c2 = build_container(CARDS.pop(random.choice(list(CARDS.keys())))[0], ft.colors.BLUE)

    winner = build_container("", ft.colors.BLACK)
     
    
    #function for when p1 hits 
    def p1HIT_BUTTON(e):

        new_card = build_container(CARDS.pop(random.choice(list(CARDS.keys())))[0], ft.colors.BLUE)
        pColumn1.content.controls.insert(-1, new_card)
        page.update()
        
           
    
        






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
                        p2c1,
                        p2c2,
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






