/*
------------------------------
------------------------------

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

------------------------------
------------------------------
*/

package main

import "fmt"

func sumOfUnique(nums []int) int {
	ans, d := 0, make(map[int]int)

	for _, n := range nums {
		d[n]++
	}

	for i, n := range d {
		if n == 1 {
			ans += i
		}
	}

	return ans
}

func main() {
	nums := []int{10}
	fmt.Println(sumOfUnique(nums))
}
