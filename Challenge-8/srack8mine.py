n = int(input())
pubs = []
names = []
for i in range(n):
    pubs.append(tuple(input().strip().split()))
pubs.sort(key=lambda x: (-int(x[1]), x[0]))
for pub in pubs:
    if pub[0] not in names:
        print(*pub)
        names.append(pub[0])
