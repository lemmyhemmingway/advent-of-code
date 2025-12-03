def part1(input_data: str) -> int:
    total = 0
    for d in parse_input(input_data):
        x, y = d.split("-")
        for num in range(int(x), int(y) + 1):
            str_num = str(num)
            if len(str_num) % 2 == 0 and str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]:
                    total += num
    return total

def part2(input_data: str) -> int:
    total = 0
    for d in parse_input(input_data):
        x, y = d.split("-")
        for num in range(int(x), int(y) + 1):
            if is_invalid(num):
                total += num
    return total

def is_invalid(num):
    s = str(num)
    n = len(s)
    for pattern_len in range(1, n // 2 + 1):
        pattern = s[:pattern_len]
        repeated = pattern * (n // pattern_len)
        if n % pattern_len == 0 and s == repeated:
            return True
    return False

def parse_input(input_data):
    return [x for x in input_data.strip().split(",")]
