def winConditions(dead):
    if 'Tanner' in dead:
        return 'Tanner Wins!!!'
    if 'Werewolf' in dead:
        return 'Town Wins!!!'
    if 'Werewolf' not in dead:
        return 'Werewolfs Wins!!!'