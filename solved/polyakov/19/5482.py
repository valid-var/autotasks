from functools import lru_cache


def moves(h1, h2):
    return [(h1 + 2, h2), (h1, h2 + 2), (h1 * 2, h2), (h1, h2 * 2)]


@lru_cache(None)
def game(h1, h2):
    if h1 + h2 >= 231:
        return "W" # Победа
    if all([game(*n) == "W" for n in moves(h1, h2)]):
        return "P1" # Победил Петя 1ым ходом, потому что нет варианта на неудачу
    if (any([game(*n) == "W" for n in moves(h1, h2)]) and not all([game(*n) == "W" for n in moves(h1, h2)])
            or any([game(*n) == "P1" for n in moves(h1, h2)])):
        return "B1" # Победил Ваня 1ым ходом, потому что Петя может сделать неверный ход. P2 и B2 не отражают больше своей сути
    if any([game(*n) == "B1" for n in moves(h1, h2)]):
        return "P2" # Победил Петя 2ым ходом
    if all([game(*n) in ("P1", "P2") for n in moves(h1, h2)]):
        return "B2" # Победил Ваня 2ым ходом


for i in range(1, 214):
    result = game(17, i)
    print(i, result)
    # print(result)
    # if result == "B1":
    #     print(i)
    # if game(i) == "P2":
    #     print(i)
    #     print(game(i))
    # if game(i) == "B2":
    #     print(i)
    #     print(game(i))
