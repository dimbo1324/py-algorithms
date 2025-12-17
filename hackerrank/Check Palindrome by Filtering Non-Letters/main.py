def isAlphabeticPalindrome(code):
    new_str = code.strip().replace(" ", "").lower()
    a = list("".join(symbol for symbol in new_str if symbol.isalpha()))
    l = len(a)

    for i in range(0, l):
        if a[i] != a[l - i - 1]:
            return 0

    return 1


if __name__ == "__main__":
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
