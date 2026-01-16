def f(s):
    stack = []
    i = 0

    while i < len(s) and s[i] == 'a':
        stack.append('х')  # х - просто метка для подсчета, добавляем, если видим а и тд
        i += 1

    while i < len(s) and s[i] == 'b':
        stack.append('х')
        i += 1

    while i < len(s) and s[i] == 'c':
        if stack:
            stack.pop()
            i += 1
        else:
            return False

    return i == len(s) and not stack


tests = ["abcc", "aabccc", "abbccc", "abc", "aab", "ac"]
for t in tests:
    print(f"{t}: {f(t)}")