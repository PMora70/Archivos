n = int(input())
animals = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    traits = set(parts[2:])
    animals.append(traits)

max_shared = 0

for i in range(n):
    for j in range(i + 1, n):
        shared = len(animals[i] & animals[j])  
        max_shared = max(max_shared, shared)

print(max_shared + 1)