import math

def parse_input(rotations: str) -> list[str]:
    return [line.strip() for line in rotations.split('\n') if line.strip()]

def part1(rotations: str):
    DIAL_SIZE = 100
    current_pos = 50  
    rotation_lines = parse_input(rotations)
    part1_password = 0
    for rotation in rotation_lines:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'R':
            current_pos = (current_pos + distance) % DIAL_SIZE
        elif direction == 'L':
            current_pos = (current_pos - distance) % DIAL_SIZE
        
        if current_pos == 0:
            part1_password += 1
    return part1_password

def part2(rotations: str) -> int:
    DIAL_SIZE = 100
    
    current_pos = 50  
    part2_password = 0
    
    rotation_lines = parse_input(rotations)

    for rotation in rotation_lines:
        direction = rotation[0]
        distance = int(rotation[1:])

        start_pos = current_pos
        
        hits_during_rotation = 0
        
        if direction == 'R':
            hits_during_rotation = (start_pos + distance) // DIAL_SIZE

        elif direction == 'L':
            if start_pos == 0:
                hits_during_rotation = distance // DIAL_SIZE
            
            else:
                if distance >= start_pos:
                    hits_during_rotation = math.floor((distance - start_pos) / DIAL_SIZE) + 1
                else:
                    hits_during_rotation = 0

        part2_password += hits_during_rotation

        if direction == 'R':
            current_pos = (current_pos + distance) % DIAL_SIZE
        elif direction == 'L':
            current_pos = (current_pos - distance) % DIAL_SIZE
        
    return part2_password


