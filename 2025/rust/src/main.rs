use std::env;
use std::fs;

mod day01;
mod day02;
// mod dayXX;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 2 {
        eprintln!("Usage: aoc <day>");
        std::process::exit(1);
    }

    let day = &args[1];
    let input_path = format!("../inputs/day0{}.txt", day);
    let input = fs::read_to_string(&input_path)
        .unwrap_or_else(|_| panic!("Could not read {}", input_path));

    match day.as_str() {
        "1" => println!("Part 1: {}\nPart 2: {}", day01::part1(&input), day01::part2(&input)),
        "2" => println!("Part 1: {}\nPart 2: {}", day02::part1(&input), day02::part2(&input)),
        // "XX" => println!("Part 1: {}\nPart 2: {}", dayXX::part1(&input), dayXX::part2(&input)),
        _ => eprintln!("Day {} not implemented", day),
    }
}
