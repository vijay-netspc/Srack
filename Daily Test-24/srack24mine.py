string = input().strip().split("*")

def decrypt(ch):
    if len(ch) < 3 and int(ch) < 26:
        return chr(int(ch) + ord('a'))
    return decrypt(ch[0]) + decrypt(ch[1:])

if len(string) == 1:
    for i in string[0]:
        print(decrypt(i), end="")
else:
    for i in string[:len(string)-1]:
        print(decrypt(i), end="")
    for i in string[-1]:
        print(decrypt(i), end="")
