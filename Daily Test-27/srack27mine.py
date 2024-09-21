n = int(input())
for h in range(0, 24):
    for m in range(0, 60):
        if (sum(1 for i in bin(h) if i=='1') + sum(1 for i in bin(m) if i=='1')) == n:
            print(f"{h:02d}:{m:02d}")
