package main

import (
	"fmt"
)

func differenceOfSums(n int, m int) int {
	ans := 0

	for i := 0; i <= n; i++ {
		if i%m > 0 {
			ans += i
		} else {
			ans -= i
		}
	}
	return ans
}
func main() {
	fmt.Println(differenceOfSums(10, 3))
}
