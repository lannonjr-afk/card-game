import random
#a
starter_deck = [
    {"name": "Strike", "cost": 1, "type": "attack", "value": 6},
    {"name": "Strike", "cost": 1, "type": "attack", "value": 6},
    {"name": "Heavy Hit", "cost": 2, "type": "attack", "value": 12},
    {"name": "Defend", "cost": 1, "type": "shield", "value": 5},
    {"name": "Heal Potion", "cost": 1, "type": "heal", "value": 4}
]

player_stats = {
    'hp': 15,
    'max_hp': 15,
    'energy': 3,
    'max_energy': 3,
    'shield': 0,
    'hand_size': 5
}

enemy_stats = {
    "hp": 40,
    "max_hp": 40,
    "shield": 0,
    "intent": random.randint(1, 10)
}

# Card Piles Setup
draw_pile = list(starter_deck)
random.shuffle(draw_pile)

hand = []
discard_pile = []  # Discard pile initialized empty

def draw_card():
    for i in range(5):
        if len(draw_pile) == 0:
            if len(discard_pile) == 0:
                print("No cards left to draw!")
                break
            
            draw_pile.extend(discard_pile)
            discard_pile.clear()
            random.shuffle(draw_pile)
            print("--> Discard pile shuffled back into draw pile!")

        card_drawn = draw_pile.pop()
        hand.append(card_drawn)

draw_card()

print("--- YOUR HAND ---")
for idx, card in enumerate(hand, 1):
    print(f"{idx} (Cost: {card['cost']}) - {card['type'].capitalize()}: {card['value']}")
