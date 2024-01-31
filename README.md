# flet-blackjack
Blackjack made with python and flet

## Roadmap
Deck Handling:
- [x] Use a standard 52-card deck or multiple decks shuffled together.
- [x] Implement proper shuffling techniques to ensure randomness.

Card Values:
- [ ] Aces can be worth 1 or 11, depending on the hand's total.
- [x] Face cards (Jack, Queen, King) are each worth 10.
- [x] Number cards are worth their face value.

Game Logic:
- [ ] Implement the basic actions: Hit, Stand, Double Down, and Split (if allowing splits).
- [x] Deal two initial cards to the player and the dealer, with one of the dealer's cards hidden.
- [ ] Check for natural blackjack (an Ace and a 10-value card) for both the player and the dealer.

Player's Decisions:
- [x] Allow the player to hit (take another card) until they choose to stand or they bust (exceed 21).
- [ ] Implement the option for the player to double down (double their original bet) on their first two cards, usually allowed when the initial two cards total 9, 10, or 11.
- [ ] If applicable, allow the player to split identical cards into two separate hands.

Dealer's Actions:
- [ ] The dealer typically hits until their hand totals 17 or higher.
- [ ] Implement rules for the dealer to stand on a "hard 17" and hit on a "soft 17."

Winning Conditions:
- [ ] Player wins if their hand is closer to 21 than the dealer's without busting.
- [ ] Dealer wins if the player busts or if the dealer's hand is closer to 21.
- [ ] A tie (push) occurs if both the player and dealer have the same total.

Betting:
- [ ] Allow the player to place bets before each round.
- [ ] Handle payouts according to standard blackjack rules (e.g., 1:1 for a regular win, 3:2 for a blackjack).

User Interface:
- [x] Create a user-friendly interface that displays the player's hand, the dealer's visible card, and relevant game information.
- [x] Provide clear buttons for the player's actions (Hit, Stand, Double Down, Split).

Scoring and Statistics:
- [ ] Keep track of the player's balance, wins, losses, and ties.
- [ ] Provide feedback on the outcome of each round.

Testing:
- [ ] Test the game thoroughly to ensure that all rules are implemented correctly.
- [ ] Check for edge cases and handle them gracefully.
