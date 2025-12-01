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

def count_zeros(commands):
    count = 0
    pos = 50
    for command in commands:
        pos = pos + command
        if pos % 100 == 0:
            count += 1
    return count

def main():
    commands = get_commands()
    print(count_zeros(commands))
            
main()