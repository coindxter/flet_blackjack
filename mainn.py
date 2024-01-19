#import flet as ft
import random
import time

cards = { 

      1: ['Red 0', 1],
      2: ['Red 1', 2],
      3: ['Red 1', 2],
      4: ['Red 2', 3],
      5: ['Red 2', 3],
      6: ['Red 3', 4],
      7: ['Red 3', 4],
      8: ['Red 4', 5],
      9: ['Red 4', 5],
     10: ['Red 5', 6],
     11: ['Red 5', 6],
     12: ['Red 6', 7],
     13: ['Red 6', 7],
     14: ['Red 7', 8],
     15: ['Red 7', 8],
     16: ['Red 8', 9],
     17: ['Red 8', 9],
     18: ['Red 9', 10],
     19: ['Red 9', 10],
     20: ['Red Skip', 11],
     21: ['Red Skip', 11],
     22: ['Red Reverse', 12],
     23: ['Red Reverse', 12],
     24: ['Red +2', 13],
     25: ['Red +2', 13],

     26: ['Blue 0', 1],
     27: ['Blue 1', 2],
     28: ['Blue 1', 2],
     29: ['Blue 2', 3],
     30: ['Blue 2', 3],
     31: ['Blue 3', 4],
     32: ['Blue 3', 4],
     33: ['Blue 4', 5],
     34: ['Blue 4', 5],
     35: ['Blue 5', 6],
     36: ['Blue 5', 6],
     37: ['Blue 6', 7],
     38: ['Blue 6', 7],
     39: ['Blue 7', 8],
     40: ['Blue 7', 8],
     41: ['Blue 8', 9],
     42: ['Blue 8', 9],
     43: ['Blue 9', 10],
     44: ['Blue 9', 10],
     45: ['Blue Skip', 11],
     46: ['Blue Skip', 11],
     47: ['Blue Reverse', 12],
     48: ['Blue Reverse', 12],
     49: ['Blue +2', 13],
     50: ['Blue +2', 13],

     51: ['Green 0', 1],
     52: ['Green 1', 2],
     53: ['Green 1', 2],
     54: ['Green 2', 3],
     55: ['Green 2', 3],
     56: ['Green 3', 4],
     57: ['Green 3', 4],
     58: ['Green 4', 5],
     59: ['Green 4', 5],
     60: ['Green 5', 6],
     61: ['Green 5', 6],
     62: ['Green 6', 7],
     63: ['Green 6', 7],
     64: ['Green 7', 8],
     65: ['Green 7', 8],
     66: ['Green 8', 9],
     67: ['Green 8', 9],
     68: ['Green 9', 10],
     69: ['Green 9', 10],
     70: ['Green Skip', 11],
     71: ['Green Skip', 11],
     72: ['Green Reverse', 12],
     73: ['Green Reverse', 12],
     74: ['Green +2', 13],
     75: ['Green +2', 13],

     76: ['Yellow 0', 1],
     77: ['Yellow 1', 2],
     78: ['Yellow 1', 2],
     79: ['Yellow 2', 3],
     80: ['Yellow 2', 3],
     81: ['Yellow 3', 4],
     82: ['Yellow 3', 4],
     83: ['Yellow 4', 5],
     84: ['Yellow 4', 5],
     85: ['Yellow 5', 6],
     86: ['Yellow 5', 6],
     87: ['Yellow 6', 7],
     88: ['Yellow 6', 7],
     89: ['Yellow 7', 8],
     90: ['Yellow 7', 8],
     91: ['Yellow 8', 9],
     92: ['Yellow 8', 9],
     93: ['Yellow 9', 10],
     94: ['Yellow 9', 10],
     95: ['Yellow Skip', 11],
     96: ['Yellow Skip', 11],
     97: ['Yellow Reverse', 12],
     98: ['Yellow Reverse', 12],
     99: ['Yellow +2', 13],
    100: ['Yellow +2', 13],
    
    101: ['Wild +4', 14],
    102: ['Wild +4', 14],
    103: ['Wild +4', 14],
    104: ['Wild +4', 14],
     
    105: ['Wild', 15],
    106: ['Wild', 15],
    107: ['Wild', 15],
    108: ['Wild', 15],
    





}

random_numbers = []

for i in range(14):
    while True:
        random_number = random.randint(1, 108)
        if random_number not in random_numbers:
            break
    random_numbers.append(random_number)

def playerhand():
    p1CARD = []
    p1CARD1 = random_numbers[0]
    p1CARD2 = random_numbers[1]
    p1CARD3 = random_numbers[2]
    p1CARD4 = random_numbers[3]
    p1CARD5 = random_numbers[4]
    p1CARD6 = random_numbers[5]
    p1CARD7 = random_numbers[6]
    p1CARD.append(cards[p1CARD1])
    p1CARD.append(cards[p1CARD2])
    p1CARD.append(cards[p1CARD3])
    p1CARD.append(cards[p1CARD4])
    p1CARD.append(cards[p1CARD5])
    p1CARD.append(cards[p1CARD6])
    p1CARD.append(cards[p1CARD7])
    cards.pop(p1CARD1)
    cards.pop(p1CARD2)
    cards.pop(p1CARD3)
    cards.pop(p1CARD4)
    cards.pop(p1CARD5)
    cards.pop(p1CARD6)
    cards.pop(p1CARD7)

    p2CARD = []
    p2CARD1 = random_numbers[7]
    p2CARD2 = random_numbers[8]
    p2CARD3 = random_numbers[9]
    p2CARD4 = random_numbers[10]
    p2CARD5 = random_numbers[11]
    p2CARD6 = random_numbers[12]
    p2CARD7 = random_numbers[13]

    p2CARD.append(cards[p2CARD1])
    p2CARD.append(cards[p2CARD2])
    p2CARD.append(cards[p2CARD3])
    p2CARD.append(cards[p2CARD4])
    p2CARD.append(cards[p2CARD5])
    p2CARD.append(cards[p2CARD6])
    p2CARD.append(cards[p2CARD7])

    cards.pop(p2CARD1)
    cards.pop(p2CARD2)
    cards.pop(p2CARD3)
    cards.pop(p2CARD4)
    cards.pop(p2CARD5)
    cards.pop(p2CARD6)
    cards.pop(p2CARD7)



    return p1CARD, p2CARD, 

def build_container(name, color):
    return ft.Container(
        content=ft.Text(name),
        bgcolor=color,
        padding=15,
    )

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

def app(page: ft.Page):
    (p1CARD, p2CARD, river) = playerhand()

    count_text = ft.TextField(value="0")

    r1 = build_container("", ft.colors.BLUE)
    r2 = build_container("", ft.colors.BLUE)
    r3 = build_container("", ft.colors.BLUE)
    r4 = build_container("", ft.colors.BLUE)
    r5 = build_container("", ft.colors.BLUE)

    p1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p2 = build_container(p1CARD[1][0], ft.colors.BLUE)
    p3 = build_container(p2CARD[0][0], ft.colors.BLUE)
    p4 = build_container(p2CARD[1][0], ft.colors.BLUE)

    pot = build_container("0", ft.colors.BLACK)

    bank1 = build_container("100", ft.colors.GREEN)
    bank2 = build_container("100", ft.colors.GREEN)

    p1BET = ft.TextField(label="Bet")
    p2BET = ft.TextField(label="Bet")

    p1CALL = build_button("CALL", ft.colors.YELLOW)
    p2CALL = build_button("CALL", ft.colors.YELLOW)

    winner = build_container("", ft.colors.BLACK)

    def p1BET_BUTTON(e):
        sum1 = int(p1BET.value)
        sum2 = int(pot.content.value)
        sum3 = sum1 + sum2
        pot.content.value = str(sum3)
        sum4 = int(bank1.content.value)
        sum5 = sum4 - sum1
        bank1.content.value = str(sum5)
        page.update()

    def highcard():
        p1MAX =  max(p1CARD[0][1], p1CARD[1][1])
        p2MAX =  max(p2CARD[0][1], p2CARD[1][1])
        if p1MAX == p2MAX:
            p1MIN = min(p1CARD[0][1], p1CARD[1][1])
            p2MIN = min(p2CARD[0][1], p2CARD[1][1])
            if p1MIN > p2MIN:
                winner.content.value = "Player One Wins"
                sum1 = int(pot.content.value)
                sum2 = int(bank1.content.value)
                sum3 = sum1 + sum2
                bank1.content.value = str(sum3)
                page.update()
            else:
                winner.content.value = "Player Two Wins"
                sum1 = int(pot.content.value)
                sum2 = int(bank2.content.value)
                sum3 = sum1 + sum2
                bank2.content.value = str(sum3)
                page.update()
        elif p1MAX > p2MAX:
            winner.content.value = "Player One Wins"
            sum1 = int(pot.content.value)
            sum2 = int(bank1.content.value)
            sum3 = sum1 + sum2
            bank1.content.value = str(sum3)
            page.update()
        else:
            winner.content.value = "Player Two Wins"
            sum1 = int(pot.content.value)
            sum2 = int(bank2.content.value)
            sum3 = sum1 + sum2
            bank2.content.value = str(sum3)
            page.update()
              
    def p2BET_BUTTON(e):

        count = int(count_text.value) + 1
        count_text.value = str(count)

        sum1 = int(p2BET.value)
        sum2 = int(pot.content.value)
        sum3 = sum1 + sum2
        pot.content.value = str(sum3)
        sum4 = int(bank2.content.value)
        sum5 = sum4 - sum1
        bank2.content.value = str(sum5)
        if count == 1:
            r1.content.value = river[0][0]
        if count == 2:
            r2.content.value = river[1][0]
        if count == 3:
            r3.content.value = river[2][0]
        if count == 4:
            r4.content.value = river[3][0]
            r5.content.value = river[4][0]
            highcard()
 
        page.update()
        
    p1BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p1BET_BUTTON)
    p2BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p2BET_BUTTON)
    
    pColumn1 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player One"), size=16),
                        bank1,
                        p1,
                        p2,
                        p1BET,
                        p1BET_BUTTON,
                        #p1CALL,
                        #p1FOLD,
                    ],
                ),
            )

    pColumn2 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player Two"), size=16),
                        bank2,
                        p3,
                        p4,
                        p2BET,
                        p2BET_BUTTON,
                        #p2CALL,
                        #p2FOLD,
                    ],
                ),
            )

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

    river3 = ft.Container(
                content=ft.Row(
                    [
                        r1,
                        r2,
                        r3
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    river2 = ft.Container(
                content=ft.Row(
                    [
                        r4,
                        r5
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    riverPOT = ft.Container(
                content=ft.Row(
                    [
                        pot,
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    winnerROW = ft.Container(
        content=ft.Row(
            [
                winner,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )

    def start_button(e):
        page.controls.pop()
        page.update()
        page.add(
            river3,
            river2,
            riverPOT,
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
