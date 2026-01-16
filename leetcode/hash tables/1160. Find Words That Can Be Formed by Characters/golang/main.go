package main

import (
	"fmt"
)

func countCharacters(words []string, chars string) int {
	ans := 0

	charsCnt := make(map[rune]int)
	for _, r := range chars {
		charsCnt[r]++
	}

	for _, w := range words {
		wordCnt := make(map[rune]int)
		ok := true

		for _, r := range w {
			wordCnt[r]++
			if wordCnt[r] > charsCnt[r] {
				ok = false
				break
			}
		}

		if ok {
			ans += len([]rune(w))
		}
	}

	return ans
}

func main() {
	words := []string{"cat", "bt", "hat", "tree"}
	chars := "atach"
	fmt.Println(countCharacters(words, chars))
}
