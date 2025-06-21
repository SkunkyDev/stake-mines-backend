import random

def generate_mines_layout(mines_count):
    all_tiles = list(range(25))
    random.shuffle(all_tiles)
    return all_tiles[:mines_count]