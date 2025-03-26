from functools import *
def moves (x,step = 0):
    if step == 0:
        return [(x + 2,1), (x + 5,2), (x + 12,3), ( x * 2,4)]
    if step == 1:
        return [ (x + 5, 2), (x + 12, 3), (x * 2, 4)]
    if step == 2:
        return [(x + 2, 1), (x + 12, 3), (x * 2, 4)]
    if step == 3:
        return [(x + 2, 1), (x + 5, 2),  (x * 2, 4)]
    if step == 4:
        return [(x + 2, 1), (x + 5, 2), (x + 12, 3)]


@lru_cache(None)
def game(x,step = 0):
    if x >= 121:
        return 'W'
    if any([game(m,step) == 'W' for m,step in moves  (x,step)]):
        return 'S1'
    if all([game (m,step ) == 'S1' for m,step  in moves (x,step)]) :
        return 'D1'
    if any([game (m,step ) == 'D1' for m,step  in moves (x,step)]):
        return 'S2'
    if all([game(m,step ) in ('S1','S2') for m,step  in moves (x,step)]):
        return 'D2'
    if any([game (m,step ) == 'D2' for m,step in moves (x,step)]):
        return 'S3'
    if all([game(m,step ) in ('S1','S2','S3') for m,step in moves (x,step)]):
        return 'D3'

for s in range (1,121):
        if game(s) == 'D1':
            print('19.', s) #31
        if game(s) == 'S2':
            print('20.', s)
        if game(s) == 'D1':
            print('21.', s)