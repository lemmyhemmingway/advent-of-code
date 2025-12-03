package main

import (
	"flag"
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
	inputPath := filepath.Join("..", "inputs", fmt.Sprintf("day%s.txt", day))
	input, err := os.ReadFile(inputPath)
	if err != nil {
		log.Fatalf("Could not read %s: %v", inputPath, err)
	}

	inputStr := string(input)

	switch day {
	case "01":
		fmt.Printf("Part 1: %s\n", Day01Part1(inputStr))
		fmt.Printf("Part 2: %s\n", Day01Part2(inputStr))
	case "02":
		fmt.Printf("Part 1: %s\n", Day02Part1(inputStr))
		fmt.Printf("Part 2: %s\n", Day02Part2(inputStr))
	default:
		log.Fatalf("Day %s not implemented", day)
	}
}

// Day solutions
func Day01Part1(input string) string {
	return "TODO"
}

func Day01Part2(input string) string {
	return "TODO"
}

func Day02Part1(input string) string {
	return "TODO"
}

func Day02Part2(input string) string {
	return "TODO"
}
