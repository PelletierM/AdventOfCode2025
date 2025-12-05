import sys

def get_map():
    map = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                row.append(char)
            map.append(row)
    return map

def is_valid_roll(map, pos):
    count = 0
    map_x= len(map[0])
    map_y = len(map)
    for x in range(pos[0] - 1, pos[0] + 2):
        if x >= 0 and x < map_x:
            for y in range(pos[1] - 1, pos[1] + 2):
                if not (x == pos[0] and y == pos[1]) and y >= 0 and y < map_y:
                    if map[y][x] == '@' or map[y][x] == 'x':
                        count += 1
    if count < 4:
        map[pos[1]][pos[0]] = 'x'
        return True
    return False

def count_valid_rolls(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != '.' and is_valid_roll(map, [x, y]):
                count += 1
    return count

def cleanup(map):
    count = 0
    for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == 'x':
                    map[y][x] = '.'
                    count += 1
    return count

def loop_through(map):
    count = 0
    while(count_valid_rolls(map) > 0):
        count += cleanup(map)
    return count

def main():
    map = get_map()
    print(loop_through(map))

main()