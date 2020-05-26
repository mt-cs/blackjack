# blackjack

This is a simply Python program that simulates a simplified version of the game of Blackjack between two virtual players. As you can see, this is not really Blackjack, but a very simplified version! So you Blackjack afficinadoes out there will just have to bear with it!

The cards have the following values:
- Numeric cards are assigned the value they have printed on them. For example, the value of the 2 of spades is 2, and the value of the 5 of diamonds is 5.
- Jacks, queens, and kings are valued at 10.
- Aces are valued at 1 or 11, depending on the player’s choice.

The program should deal cards arbitrarily and at the same time to each player until one player’s hand is worth more than 21 points. When that happens, the other player is the winner. (It is possible that both players’ hands will simultaneously exceed 21 points, in which case neither player wins.)

If a player is dealt an ace, the program should decide the value of the card according to the following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. In that case, the ace will be worth 1 point.
