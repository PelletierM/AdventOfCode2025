import sys

def get_commands():
    commands = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            num = int(line[1:])
            if line.startswith("L"):
                num *= -1
            commands.append(num)
    return commands

def get_pos(pos):
    pos = pos % 100
    if pos < 0:
        pos = 100 - pos
    return pos

def count_zeros(commands):
    count = 0
    pos = 50
    for command in commands:
        new_pos = pos + command
        count += abs(int(new_pos / 100))
        if (pos != 0 and new_pos < 0) or new_pos == 0:
            count += 1
        pos = get_pos(new_pos)
    return count

def main():
    commands = get_commands()
    print(count_zeros(commands))
            
main()