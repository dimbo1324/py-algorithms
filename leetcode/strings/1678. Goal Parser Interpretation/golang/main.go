package main

import "fmt"

func interpret(command string) string {
	ans, tmp := "", ""

	for _, v := range command {
		tmp += string(v)
		if tmp == "G" {
			ans += "G"
			tmp = ""
			continue
		}

		if tmp == "()" {
			ans += "o"
			tmp = ""
			continue
		}

		if tmp == "(al)" {
			ans += "al"
			tmp = ""
			continue
		}
	}

	return ans
}
func main() {
	fmt.Println(interpret("G()(al)"))
}
