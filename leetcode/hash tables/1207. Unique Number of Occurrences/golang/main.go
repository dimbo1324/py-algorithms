package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	makeSet := func(arr []int) map[int]struct{} {
		s := map[int]struct{}{}
		for _, v := range arr {
			s[v] = struct{}{}
		}
		return s
	}
	makeCount := func(arr []int) map[int]int {
		m := map[int]int{}
		for _, v := range arr {
			m[v]++
		}
		return m
	}

	c := makeCount(arr)
	e := []int{}
	for _, v := range c {
		e = append(e, v)
	}
	return len(makeSet(e)) == len(c)
}

func main() {
	arr := []int{1, 2}
	fmt.Println(uniqueOccurrences(arr))
}
