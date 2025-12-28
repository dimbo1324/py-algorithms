package main

import (
	"fmt"
)

func truncateSentence(s string, k int) string {
	spaces, target := 0, ' '
	for i, v := range s {
		if v == target {
			spaces++
		}
		if spaces == k {
			return s[:i]
		}
	}
	return s
}

func main() {
	s := "What is the solution to this problem"
	k := 4
	fmt.Println(truncateSentence(s, k))

}
