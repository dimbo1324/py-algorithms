// Input: n = 234
// Output: 15
// Explanation:
// Product of digits = 2 * 3 * 4 = 24
// Sum of digits = 2 + 3 + 4 = 9
// Result = 24 - 9 = 15

package main

import (
	"fmt"
	"strconv"
)

func subtractProductAndSum(n int) int {
	a, m, s := 0, 1, strconv.Itoa(n)
	for i := 0; i < len(s); i++ {
		dig := int(s[i] - '0')
		m *= dig
		a += dig
	}
	return m - a
}

func main() {
	n := 234
	fmt.Println(subtractProductAndSum(n))
}
