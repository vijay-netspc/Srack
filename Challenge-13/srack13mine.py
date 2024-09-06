s = input().strip()
if len(s) == 1:
    print(-1)
else:
    first_ind = []
    ind = 1
    while 1:
        ind = s.find(s[0], ind)
        if ind == -1:
            break
        first_ind.append(ind)
        ind += 1
    for i in first_ind:
        if s[:len(s) - i] == s[i:]:
            print(len(s) - i)
            break
    else:
        print(-1)
