package main

import (
	"fmt"
)

func isPathCrossing(path string) bool {
	type point struct {
		x int
		y int
	}

	visCoords := make(map[point]struct{})

	x, y := 0, 0

	visCoords[point{x, y}] = struct{}{}

	for _, step := range path {
		switch step {
		case 'N':
			y++
		case 'S':
			y--
		case 'E':
			x++
		case 'W':
			x--
		}

		curPos := point{x, y}

		if _, exists := visCoords[curPos]; exists {
			return true
		}

		visCoords[curPos] = struct{}{}

	}
	return false
}

func main() {
	path := "NESWW"
	fmt.Println(isPathCrossing(path))
}
