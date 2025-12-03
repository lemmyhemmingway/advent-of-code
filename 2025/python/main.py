import sys
import importlib

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <day>")
        sys.exit(1)
    
    day = sys.argv[1].zfill(2)
    
    input_path = None
    try:
        module = importlib.import_module(f"day{day}")
        input_path = f"../inputs/day{day}.txt"
        
        with open(input_path, "r") as f:
            input_data = f.read()
        
        print(f"Part 1: {module.part1(input_data)}")
        print(f"Part 2: {module.part2(input_data)}")
    
    except ModuleNotFoundError:
        print(f"Day {day} not implemented")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Input file {input_path} not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
