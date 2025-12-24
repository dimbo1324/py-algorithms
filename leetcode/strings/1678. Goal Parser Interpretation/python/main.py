class Solution:
    def interpret_1(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

    def interpret_2(self, command: str) -> str:
        ans, tmp = "", ""

        for c in command:
            tmp += c

            if tmp == "G":
                ans += "G"
                tmp = ""
                continue

            if tmp == "()":
                ans += "o"
                tmp = ""
                continue

            if tmp == "(al)":
                ans += "al"
                tmp = ""
                continue

        return ans
