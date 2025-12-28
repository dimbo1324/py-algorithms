package main

import (
	"fmt"
	"strconv"
)

func fizzBuzz(n int) []string {
	ans := make([]string, 0, n)
	f, b, fb := "Fizz", "Buzz", "FizzBuzz"

	for i := 1; i <= n; i++ {
		is_f := i%3 == 0
		is_b := i%5 == 0

		if is_f && is_b {
			ans = append(ans, fb)
		} else if is_f {
			ans = append(ans, f)
		} else if is_b {
			ans = append(ans, b)
		} else {
			ans = append(ans, strconv.Itoa(i))
		}
	}
	return ans
}
func main() {
	n := 54324
	fmt.Println(fizzBuzz(n))
}
