pub fn part1(input: &str) -> i32 {
    let mut part1_password: i32 = 0;
    let dial_size: i32 = 100;
    let mut current_pos: i32 = 50;
    let s: Vec<&str> = parse_input(input);
    for c in s {
        let direction: &str = &c[..1];
        let distance: i32 = c[1..].parse().unwrap();

        if direction == "R" {
            current_pos = (current_pos + distance) % dial_size;
        } else  {
            current_pos = (current_pos - distance) % dial_size;
        }
        if current_pos == 0 {
            part1_password += 1;
        }

    }
    part1_password
}

pub fn parse_input(input: &str) -> Vec<&str> {
    input.trim().split('\n').collect()
}


pub fn part2(input: &str) -> i32 {
    let dial_size: i32 = 100;
    
    let mut current_pos: i32 = 50;
    let mut part2_password: i32 = 0;
    
    let s: Vec<&str> = parse_input(input);

    for c in s {
        let direction: &str = &c[..1];
        let distance: i32 = c[1..].parse().unwrap();

        let start_pos: i32 = current_pos;
        
        let mut hits_during_rotation: i32 = 0;
        
        if direction == "R" {
            hits_during_rotation = (start_pos + distance) / dial_size;

        } else if direction == "L" {
            if start_pos == 0 {
                hits_during_rotation = distance / dial_size;
            }   
            else {
                if distance >= start_pos {
                    hits_during_rotation = ((distance - start_pos) / dial_size) + 1;
                }       
                else {
                    hits_during_rotation = 0;
                }       
            }       
        }
        part2_password += hits_during_rotation;

        if direction == "R" {
            current_pos = (current_pos + distance).rem_euclid(dial_size);
        }
        else if direction == "L" {
            current_pos = (current_pos - distance).rem_euclid(dial_size);
        }   
    }   
        
    part2_password
}
