def count_ones(num):
    return bin(num).count('1')

n = int(input())
hour_counts = [count_ones(h) for h in range(24)]
minute_counts = [count_ones(m) for m in range(60)]

times = [f"{h:02d}:{m:02d}" for h in range(24) for m in range(60) 
         if hour_counts[h] + minute_counts[m] == n]

for time in times:
    print(time)
