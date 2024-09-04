pubs = []
names = set()  # Using a set for O(1) membership checks
for _ in range(n):
    pub = tuple(input().strip().split())
    pubs.append(pub)

# Sort pubs first by score in descending order, then by name
pubs.sort(key=lambda x: (-int(x[1]), x[0]))

# Iterate over pubs and print unique pub names
for pub in pubs:
    if pub[0] not in names:
        print(*pub)
        names.add(pub[0])
