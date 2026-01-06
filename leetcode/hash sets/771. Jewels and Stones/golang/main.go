/*
------------------------------
------------------------------

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

------------------------------
------------------------------
*/

package main

import (
	"fmt"
)

func numJewelsInStones(jewels string, stones string) int {
	makeSet := func(str string) map[rune]struct{} {
		s := make(map[rune]struct{})
		for _, char := range str {
			s[char] = struct{}{}
		}
		return s
	}

	jewSet := makeSet(jewels)
	ans := 0

	for _, s := range stones {
		if _, exists := jewSet[s]; exists {
			ans++
		}
	}

	return ans
}

func main() {
	jewels := "aA"
	stones := "aAAbbbb"
	fmt.Println(numJewelsInStones(jewels, stones))
}
