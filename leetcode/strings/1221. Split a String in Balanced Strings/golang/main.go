package main

import (
	"fmt"
	"strings"
)

func balancedStringSplit(s string) int {
	ans := 0
	if strings.Count(s, "L") == strings.Count(s, "R") {
		balance := 0
		for _, c := range s {
			if string(c) == "R" {
				balance++
			} else {
				balance--
			}
			if balance == 0 {
				ans++
			}
		}
	}

	return ans
}
func main() {
	fmt.Println(balancedStringSplit("RLRRLLRLRL"))
}
