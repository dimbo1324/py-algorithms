// Input: n = 234
// Output: 15
// Explanation:
// Product of digits = 2 * 3 * 4 = 24
// Sum of digits = 2 + 3 + 4 = 9
// Result = 24 - 9 = 15

package main

import (
	"fmt"
)

func subtractProductAndSum(n int) int {

	divmod := func(a, b int) (int, int) {
		return a / b, a % b
	}

	a, m := 0, 1

	for n > 0 {
		newN, d := divmod(n, 10)
		n = newN
		a += d
		m *= d
	}

	return m - a
}

func main() {
	n := 234
	fmt.Println(subtractProductAndSum(n))
}
