package day1

import (
	"fmt"
	"strconv"
	"strings"
)

func Part1(input string) string {
	// dial_size := 100
	dial := 50
	data := parse_input(input)
	for _, rotation := range data {
		direction := string(rotation[0])
		step := rotation[1:]
		s, err := strconv.Atoi(step)
		if err != nil {
			fmt.Errorf("Error convertin to int %v", err)
		}
		apply_rotation(direction, s, dial)
	}
	return ""
}

func apply_rotation(direction string, step, dial int) int {

	return dial
}

func Part2(input string) string {
	return "TODO"
}

func parse_input(input string) []string {
	return strings.Split(strings.TrimSpace(input), "\n")
}
