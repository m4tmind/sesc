s=set(input().split())
k=set(input().split())
print(*(sorted(set.intersection(s&k))))
