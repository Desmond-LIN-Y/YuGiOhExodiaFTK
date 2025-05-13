from os import stat
import re
from nbformat import write
import numpy as np

class State:
    def __init__(self, hand, deck, graveyard, field_spell, field, extra_deck, signal):
        self.hand = hand
        self.deck = deck
        self.graveyard = graveyard
        self.field_spell = field_spell
        self.field = field
        self.extra_deck = extra_deck
        self.signal = signal

class monster:
    '''
    monster cards
    '''
    priority = 0
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def play(self, x):
        return 0

        
class spell:
    '''spell cards'''
    def __init__(self, name, effect, priority):
        self.name = name
        self.effect = effect
        self.priority = priority
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def play(self, state):
        if self.effect(state):
            with open("gamelog.txt", "a") as o:
                o.write(f'I activated {str(self)}:\n')
                o.write(f"now my hands are {str(state.hand)}\n")
            return 1
        return 0
            

def draw(state):
    state.hand.append(state.deck.pop())

def search(state, x):
    state.deck.remove(x)
    state.hand.append(x)
    np.random.shuffle(state.deck)
    
def resolve(state,x):
    state.graveyard.append(x)
    state.hand.remove(x)
        
def magical_mallet(state):
    resolve(state, magical_mallet_card)
    x = len(state.hand)
    for i in range(x):
        state.deck.append(state.hand.pop())
    np.random.shuffle(state.deck)
    for i in range(x):
        draw(state)
    assert(len(state.hand) == x)
    return 1
    

def upstart_goblin(state):
    draw(state)
    resolve(state, upstart_goblin_card)
    return 1

def one_day_of_peace(state):
    draw(state)
    resolve(state, one_day_of_peace_card)
    return 1

def into_the_void(state):
    if len(state.hand) < 3:
        return 0
    draw(state)
    resolve(state, into_the_void_card)
    return 1

def chicken_game(state):
    draw(state)
    state.hand.remove(chicken_game_card)
    if state.field_spell:
        state.graveyard.append(state.field_spell.pop())
    state.field_spell.append(chicken_game_card)
    return 1

def terraforming(state):
    if chicken_game_card in state.deck:
        search(state, chicken_game_card)
    elif pesudo_space_card in state.deck:
        search(state, pesudo_space_card)
    else:
        return 0
    resolve(state, terraforming_card)
    return 1

def exodia_head(state):
    if exodia_left_hand_card in state.hand and exodia_left_leg_card in state.hand:
        if exodia_right_hand_card in state.hand and exodia_right_leg_card in state.hand:
            with open("gamelog.txt", "a") as o:
                o.write('FTK by Exodia')
            state.signal = 1
            return 1
    return 0

def cartoon_dict(state):
    if cartoon_dict_card in state.deck:
        search(state, cartoon_dict_card)
    elif cartoon_spellcaster_card in state.deck:
        search(state, cartoon_spellcaster_card)
    else:
        return 0
    resolve(state, cartoon_dict_card)
    return 1

def allure_of_darkness(state):
    if cartoon_spellcaster_card in state.hand:
        state.hand.remove(cartoon_spellcaster_card)
    elif sky_striker_renyi_card in state.hand:
        state.hand.remove(sky_striker_renyi_card)
    else:
        return 0
    draw(state)
    draw(state)
    resolve(state, allure_of_darkness_card)
    return 1

def reinforcement(state):
    if sky_striker_renyi_card in state.deck:
        search(state, sky_striker_renyi_card)
        resolve(state, reinforcement_card)
        return 1
    return 0

def sky_striker_drones(state):
    if sky_striker_mobilize_card in state.graveyard:
        state.extra_deck = 0
        state.graveyard.remove(sky_striker_mobilize_card)
        state.hand.append(sky_striker_mobilize_card)
        resolve(state, sky_striker_drones_card)
        return 1
    return 0

def sky_striker_mobilize(state):
    if sky_striker_drones_card in state.deck:
        search(state, sky_striker_drones_card)
    elif sky_striker_renyi_card in state.deck:
        search(state, sky_striker_renyi_card)
    else:
        return 0
    if len(state.graveyard) >= 3:
        draw(state)
    resolve(state, sky_striker_mobilize_card)
    return 1

def pesudo_space(state):
    if chicken_game_card in state.graveyard or chicken_game_card in state.field_spell:
        state.graveyard.append(state.field_spell.pop())
        state.field_spell.append(pesudo_space_card)
        state.graveyard.remove(chicken_game_card)
        draw(state)
        state.hand.remove(pesudo_space_card)
        return 1
    return 0

def Anchamoufrite(state):
    if state.extra_deck:
        return 0
    draw(state)
    state.hand.remove(Anchamoufrite_card)
    return 1

def spellbook_of_knowledge(state):
    if not(spellbook_of_secrets_card in state.hand) and not(spellbook_magician_of_prophecy_card in state.field):
        return 0
    if spellbook_of_secrets_card in state.hand:
        state.hand.remove(spellbook_of_secrets_card)
    else:
        state.graveyard.append(state.field.pop())
    draw(state)
    draw(state)
    resolve(state, spellbook_of_knowledge_card)
    return 1

def spellbook_of_secrets(state):
    if spellbook_magician_of_prophecy_card in state.deck:
        search(state, spellbook_magician_of_prophecy_card)
    elif spellbook_of_knowledge in state.deck:
        search(state, spellbook_of_knowledge_card)
    else:
        return 0
    resolve(state, spellbook_of_secrets_card)
    return 1

def spellbook_magician_of_prohecy(state):
    if spellbook_of_secrets_card in state.deck:
        search(state, spellbook_of_secrets_card)
    elif spellbook_of_knowledge_card in state.deck:
        search(state, spellbook_of_knowledge_card)
    else:
        return 0
    state.hand.remove(spellbook_magician_of_prophecy_card)
    state.field.append(spellbook_magician_of_prophecy_card)
    return 1

def contract_with_don_thousand(state):
    draw(state)
    state.hand.remove(contract_with_don_thousand_card)
    return 1

spellbook_magician_of_prophecy_card = spell('spellbook_magician_of_prohecy', spellbook_magician_of_prohecy, 8)
spellbook_of_knowledge_card = spell('spellbook_of_knowledge', spellbook_of_knowledge,4)
spellbook_of_secrets_card = spell('spellbook_of_secrets', spellbook_of_secrets, 13)

cartoon_dict_card = spell('cartoon_dictionary', cartoon_dict, 12)
cartoon_spellcaster_card = monster('cartoon_spellcaster_dark')
sky_striker_renyi_card = monster('sky_striker_renyi')
sky_striker_mobilize_card = spell('sky_striker_mobilize', sky_striker_mobilize, 3)
sky_striker_drones_card = spell('sky_striker_drones', sky_striker_drones, 4)

reinforcement_card = spell('reinforcement', reinforcement, 11)

chicken_game_card = spell('chicken_game', chicken_game, 5)
upstart_goblin_card = spell('upstart_goblin', upstart_goblin, 5)
into_the_void_card = spell('into_the_void', into_the_void,6)
one_day_of_peace_card = spell('one_day_of_peace', one_day_of_peace,5)

exodia_left_hand_card = monster('exodia_left_hand')
exodia_left_leg_card = monster('exodia_left_leg')
exodia_right_hand_card = monster('exodia_right_hand')
exodia_right_leg_card = monster('exodia_right_leg')

exodia_head_card = spell('exodia_head', exodia_head, 99)
allure_of_darkness_card = spell('allure_of_darkness', allure_of_darkness, 5)
pesudo_space_card = spell('pseudo_space', pesudo_space, 5)
Anchamoufrite_card = spell('anchamoufrite', Anchamoufrite, 6)
magical_mallet_card = spell('magical_mallet', magical_mallet, 1)
contract_with_don_thousand_card = spell('contract_with_don_thousand', contract_with_don_thousand, 2)
terraforming_card = spell('terraforming', terraforming, 10)

deck = [upstart_goblin_card, upstart_goblin_card, upstart_goblin_card, 
                into_the_void_card, into_the_void_card, into_the_void_card,
                exodia_head_card, exodia_left_hand_card, exodia_left_leg_card, exodia_right_hand_card, exodia_right_leg_card,
                terraforming_card, pesudo_space_card, pesudo_space_card,
                chicken_game_card, chicken_game_card, chicken_game_card,
                allure_of_darkness_card, allure_of_darkness_card, allure_of_darkness_card,
                cartoon_dict_card, cartoon_dict_card, cartoon_dict_card, cartoon_spellcaster_card,
                one_day_of_peace_card, reinforcement_card,
                sky_striker_renyi_card, sky_striker_renyi_card, sky_striker_renyi_card,
                sky_striker_mobilize_card, sky_striker_mobilize_card, sky_striker_drones_card,
                Anchamoufrite_card, magical_mallet_card, magical_mallet_card, magical_mallet_card,
                contract_with_don_thousand_card, 
                spellbook_of_knowledge_card, spellbook_of_secrets_card, spellbook_magician_of_prophecy_card]


def simulate(n):
    win = 0
    for i in range(n):
        np.random.seed(i)
        win += game()
        if i % 100 == 0:
            print(f'running {i}th simulation')
    with open("gamelog.txt", "a") as o:
        o.write(f'\n Empirical probability is {win/n}\n')
    
    return win/n

def game():
    with open("gamelog.txt", "a") as o:
        o.write('\nNew Exodia FTK simulation:\n')
    d = [upstart_goblin_card, upstart_goblin_card, upstart_goblin_card, 
                into_the_void_card, into_the_void_card, into_the_void_card,
                exodia_head_card, exodia_left_hand_card, exodia_left_leg_card, exodia_right_hand_card, exodia_right_leg_card,
                terraforming_card, pesudo_space_card, pesudo_space_card,
                chicken_game_card, chicken_game_card, chicken_game_card,
                allure_of_darkness_card, allure_of_darkness_card, allure_of_darkness_card,
                cartoon_dict_card, cartoon_dict_card, cartoon_dict_card, cartoon_spellcaster_card,
                one_day_of_peace_card, reinforcement_card,
                sky_striker_renyi_card, sky_striker_renyi_card, sky_striker_renyi_card,
                sky_striker_mobilize_card, sky_striker_mobilize_card, sky_striker_drones_card,
                Anchamoufrite_card, magical_mallet_card, magical_mallet_card, magical_mallet_card,
                contract_with_don_thousand_card, 
                spellbook_of_knowledge_card, spellbook_of_secrets_card, spellbook_magician_of_prophecy_card]
    state = State([], d, [], [], [], 1, 0)
    np.random.shuffle(state.deck)
    for i in range(5):
        draw(state)
    with open("gamelog.txt", "a") as o:
        o.write('Initial five cards are\n')
        o.write(f'{state.hand}\n')
    while True:
        state.hand = sorted(state.hand, reverse=True, key=lambda x: x.priority)
        played = 0
        for card in state.hand:
            if card.play(state):
                played += 1
                break
        if state.signal:
            break
        if not played:
            break
        if len(state.graveyard) >=3:
            sky_striker_mobilize_card.priority = 8 
    return state.signal

simulate(10000)