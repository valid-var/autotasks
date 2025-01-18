from functools import lru_cache


def moves(h: int):
    return h * 3, h + 3, h + 6


@lru_cache(None)
def game(h: int):
    if h >= 132:
        return "W" # Победа
    if any([game(n) == "W" for n in moves(h)]):
        return "P1" # Победил Петя 1ым ходом
    if all([game(n) == "P1" for n in moves(h)]):
        return "B1" # Победил Ваня 1ым ходом
    if any([game(n) == "B1" for n in moves(h)]):
        return "P2" # Победил Петя 2ым ходом
    if all([game(n) == "P1" or game(n) == "P2" for n in moves(h)]):
        return "B2" # Победил Ваня 2ым ходом


for i in range(1, 131):
    if game(i) == "B1":
        print(i)
        print(game(i))
    if game(i) == "P2":
        print(i)
        print(game(i))
    if game(i) == "B2":
        print(i)
        print(game(i))

