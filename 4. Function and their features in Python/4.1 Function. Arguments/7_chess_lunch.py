def can_eat(horse_pos, figure_pos):
    positions = [
        (horse_pos[0] + 2, horse_pos[1] + 1),
        (horse_pos[0] + 1, horse_pos[1] + 2),
        (horse_pos[0] - 1, horse_pos[1] + 2),
        (horse_pos[0] - 2, horse_pos[1] + 1),
        (horse_pos[0] - 2, horse_pos[1] - 1),
        (horse_pos[0] - 1, horse_pos[1] - 2),
        (horse_pos[0] + 1, horse_pos[1] - 2),
        (horse_pos[0] + 2, horse_pos[1] - 1)
    ]
    if figure_pos in positions:
        return True
    else:
        return False
