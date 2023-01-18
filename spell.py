hand = []
graveyard = []
deck = []
field = []
class spell:
    def __init__(self, name, effect,requirement):
        self.name = name
        self.effect = effect
        self.requirement = requirement

    def play(self):
        if self.requirement:
            self.effect()
    
    def __str__(self):
        return self.name
        
def upstart_goblin():
    hand.append(deck.pop())
    graveyard.append(upstart_goblin_card)
    hand.remove(upstart_goblin_card)

def into_the_void():
    hand.append(deck.pop())
    graveyard.append(into_the_void_card)
    hand.remove(into_the_void_card)

upstart_goblin_card = spell('upstart_goblin', upstart_goblin, True)
into_the_void_card = spell('into_the_void', into_the_void, len(hand)>=3)

hand=[into_the_void_card]
deck = [upstart_goblin_card]
into_the_void_card.play()
print(hand[0])
print(deck[0])
print(graveyard)