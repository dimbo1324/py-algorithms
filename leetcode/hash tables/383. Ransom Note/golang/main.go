package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	counts := make(map[rune]int)

	for _, char := range magazine {
		counts[char]++
	}

	for _, char := range ransomNote {
		counts[char]--
		if counts[char] < 0 {
			return false
		}
	}

	return true
}
func main() {
	ransomNote := "aa"
	magazine := "aab"
	fmt.Println(canConstruct(ransomNote, magazine))
}
