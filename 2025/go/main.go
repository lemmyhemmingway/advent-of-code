package main

import (
	"aoc2025/day1"
	"aoc2025/day2"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Usage: go run main.go <day>")
	}

	day := os.Args[1]
	inputPath := filepath.Join("..", "inputs", fmt.Sprintf("day0%s.txt", day))
	input, err := os.ReadFile(inputPath)
	if err != nil {
		log.Fatalf("Could not read %s: %v", inputPath, err)
	}

	inputStr := string(input)

	switch day {
	case "1":
		fmt.Printf("Part 1: %s\n", day1.Part1(inputStr))
		fmt.Printf("Part 2: %s\n", day1.Part2(inputStr))
	case "2":
		fmt.Printf("Part 1: %s\n", day2.Part1(inputStr))
		fmt.Printf("Part 2: %s\n", day2.Part2(inputStr))
	default:
		log.Fatalf("Day %s not implemented", day)
	}
}

