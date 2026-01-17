package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var ans []int
	o := map[int]int{}
	for i, v := range nums {
		d := target - v
		if idx, ok := o[d]; ok {
			ans = []int{i, idx}
		}
		o[v] = i
	}
	return ans
}
func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))
}
