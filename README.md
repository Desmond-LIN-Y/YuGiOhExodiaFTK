# YuGiOhExodiaFTK

This package aims to calculate the average probability that an Exodia First Turn Kill is achieved.
An Exodia FTK is achieved when 5 exodia cards are in hand.
All cards are described as class objects, either a spell or a monster card(effect monsters are considered spell cards here. This may disrupt sky_striker_mobilize but it should be marginal).
The algorithm is simple, activate spell cards in according to their priority.
The deck contents contain mostly cards allowing players to draw/search cards from deck. 
