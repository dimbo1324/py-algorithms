/*
------------------------------
------------------------------

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

------------------------------
------------------------------
*/

package main

import "fmt"

func firstUniqChar(s string) int {
	d := make(map[rune]int)

	for _, ch := range s {
		d[ch]++
	}

	for i, ch := range s {
		if d[ch] == 1 {
			return i
		}
	}
	return -1
}

func main() {
	s := "leetcode"
	fmt.Println(firstUniqChar(s))

}
