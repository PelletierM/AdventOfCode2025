import sys

def get_dict():
    dict = {"ranges": [], "ids": []}
    with open(sys.argv[1], "r") as f:
        for line in f:
            if line == "\n":
                break
            nums = [int(i) for i in line.split("-")]
            dict.get("ranges").append([nums[0], nums[1]])
        for line in f:
            dict.get("ids").append(int(line))
    return dict

def count_valid_ids(dict):
    count = 0
    for id in dict.get("ids"):
        for range in dict.get("ranges"):
            if id >= range[0] and id <= range[1]:
                count += 1
                break
    return count 

def main():
    dict = get_dict()
    print(count_valid_ids(dict))

main()