import time

storage: list[list] = []

with open('26-101.txt', 'r') as file:
    number, min_diff = map(int, file.readline().split())
    for line in file.readlines():
        box_size = int(line)
        found_place = False
        for i, block in enumerate(storage):
            for j, box in enumerate(block):
                if box_size - box >= min_diff:
                    if j == 0 or block[j-1] - box_size >= min_diff:
                        storage[i].insert(j, box_size)
                        found_place = True
                        break
                if box - box_size >= min_diff:
                    if j == len(block) - 1 or box_size - block[j+1] >= min_diff:
                        storage[i].insert(j+1, box_size)
                        found_place = True
                        break
            if found_place:
                break

        if not found_place:
            storage.append([box_size])
        # print(storage)
        # time.sleep(3)

print(storage)
print(len(storage))

